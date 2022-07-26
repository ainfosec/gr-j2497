# gr-j2497

The gr-j2497 out-of-tree module contains flow graphs with custom blocks for reading PLC4TRUCKS traffic.

The master branch is compatible with GNU Radio 3.7 and the maint-3.8 branch is compatible with GNU Radio 3.8.

This project is an implementation of a J2497 (PLC4TRUCKS) receiver that can be used with any GNU Radio SDR capable of receiving 100 kHz - 400 kHz. For RTL-SDR and others, this will require an upconverter.

The custom blocks send UDP packets that are compatible with the `j1708_logger.py` script for https://github.com/TruckHacking/py-hv-networks and the `j1708dump.py` command of https://github.com/TruckHacking/plc4trucksduck, e.g. you can dump PLC traffic with `j1708dump.py --interface=plc` while running the flow graphs in `/examples`.


# Prerequisites

```
sudo apt-get install python-scipy
```


# Installation
```
cd gr-j2497
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig
```


# Usage

Run the flow graphs in `/examples` with GNU Radio Companion to view messages in the console panel. If enabled on the decoder blocks, view the decoded output over UDP with a network sniffer (e.g. Wireshark) or with the `j1708dump.py --interface=plc` command of https://github.com/TruckHacking/plc4trucksduck.

* Method 1:
  * Correlates J2497 signal with a reference signal
  * Works best with 203 kHz as the reference
  * Ignores the ASK preamble
  * Works better than phase-angle measurements in moderate to high noise environments

* Method 2:
  * Correlates J2497 signal with a complete chirp reference signal to detect burst start and stop
  * Correlates with 203 kHz snippet to decode 0's and 1's in the body PSK
  * Ignores the ASK preamble
  * Works good in medium levels of noise

* Method 3:
  * Uses Quadrature Demod block and measures the phase-angle of the signal
  * Keys in on phase discontinuities between chirps to decode the body PSK
  * Ignores the ASK preamble


# License

MIT License

Copyright (c) 2019, 2020 Assured Information Security, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

