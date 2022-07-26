#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MIT License
# 
# Copyright (c) 2019, 2020 Assured Information Security, Inc.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 

import numpy, scipy
from gnuradio import gr
import pmt
import time

class encoder(gr.sync_block):
    """
    docstring for block encoder
    """
    def __init__(self, mid, data, interval, filepath_preamble, filepath_data, sample_rate):
        gr.sync_block.__init__(self,
            name="J2497_encoder",
            in_sig=[],
            out_sig=[numpy.complex64])
            
        self.preamble_chirp_data = scipy.fromfile(open(filepath_preamble), dtype=scipy.complex64)  
        self.data_chirp_data = scipy.fromfile(open(filepath_data), dtype=scipy.complex64)  
        self.replay_data = numpy.zeros(0,numpy.complex64)
        self.transmit = False
        self.replay_index = 0
        self.replay_stop_index = 0
        self.sample_rate = sample_rate/1000000 #8
        self.mid = bin(int(mid,16))[2:].zfill(8)[::-1]  # 0x0A -> 01010000
        self.mid_hex = mid
        self.data = bin(int(data,16))[2:].zfill(len(data)*4)[::-1]
        self.data_hex = data
        self.interval = interval
        self.timer = time.time()        
        self.count = 0

    def work(self, input_items, output_items):
        #in0 = input_items[0]
        in0 = 0
        out = output_items[0]
        
        # Rough Interval Timer
        if time.time() > (self.timer + self.interval):
            self.timer = time.time()
            self.count = self.count + 1
            self.generateMsg()
        
        # Transmit
        if self.transmit is True:
            
            # Begin
            if self.replay_index + len(out) > self.replay_stop_index:
                out[:] = numpy.append(self.replay_data[self.replay_index:self.replay_stop_index], numpy.zeros(len(out)-(self.replay_stop_index-self.replay_index)))
                self.transmit = False
            else:
                out[:] = self.replay_data[self.replay_index:self.replay_index + len(out)]
                self.replay_index = self.replay_index + len(out)
                    
        # Do Nothing
        else:
            out[:] = in0
            
        return len(output_items[0])
        
    def generateMsg(self):
        """ Generates the IQ data for the J2497 message.
        """
        # Extract Input Data
        #print("Handle Message")
        body = self.mid + self.data
        mid = self.mid
        
        # Construct Preamble
        preamble = "00" + mid + "1"
        
        # Construct Data Portion
        data = "11111"  # Sync
        for n in range(0,len(body)):            
            # Start Bit
            if n%8 == 0:
                data = data + "0"
                                               
            # Data Bit
            data = data + body[n]
            
            # Stop Bit
            if n%8 == 7:
                data = data + "1"
        
        # Calculate Checksum
        checksum = 0
        for n in range(0,len(body),8):
            checksum = checksum + int(body[n:n+8][::-1],2)
                    
        # Two's Complement
        binint = int("{0:b}".format(checksum))             # Convert to binary
        flipped = ~binint                                  # Flip the bits
        flipped += 1                                       # Add one (two's complement method)
        intflipped=int(str(flipped),2)                     # Back to int
        intflipped = ((intflipped + (1 << 8)) % (1 << 8))  # Over to binary
        intflipped = '{0:08b}'.format(intflipped)          # Format to one byte
        checksum = intflipped[::-1]                        # Swap bit order
        #print "CHECKSUM: " + str(checksum)

        # Append Checksum and End of Msg
        data = data + "0" + checksum + "1" + "111111"
        data_len = len(data)
        data_len_samples = self.sample_rate*100*data_len  # 100 us per bit/chirp    
        try:
            print('Message #' + str(int(self.count)) + ': ' + data + ' | MID: 0x' + self.mid_hex + ' | Data: 0x' + self.data_hex + ' | Checksum: 0x' + '%0*X' % (2,int(checksum[::-1],2)) )
        except:
            print('Message #' + str(int(self.count)) + ': ' + data)
        
        # Create the Preamble Signal
        self.replay_data = numpy.zeros(0,numpy.complex64)
        for n in preamble:
            # 0 = Chirp
            if n == "0":
                self.replay_data = numpy.append(self.replay_data, self.preamble_chirp_data)
                
                # Expects a 100 us Preamble Chirp
                if len(self.preamble_chirp_data) == self.sample_rate*100:
                    self.replay_data = numpy.append(self.replay_data, numpy.zeros(int(self.sample_rate*14),numpy.complex64))  # Zero for the extra 14 us
                    #phase_offset = 80
                    #self.replay_data = numpy.append(self.replay_data, self.replay_data[phase_offset-14:phase_offset])
            
            # 1 = Silence
            else:
                self.replay_data = numpy.append(self.replay_data,numpy.zeros(int(self.sample_rate*114),numpy.complex64))
        
        # Append the Data Signal
        for n in data:
            if n == "1":
                self.replay_data = numpy.append(self.replay_data, self.data_chirp_data) 
            else:
                self.replay_data = numpy.append(self.replay_data, self.data_chirp_data * -1) 
        
        # Begin to Transmit
        self.replay_index = 0
        self.replay_stop_index = len(self.replay_data)
        self.transmit = True        
                

