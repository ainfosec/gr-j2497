#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: J2497 Demod Method2
# Generated: Tue Jul 28 16:17:30 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from scipy.signal import chirp
import J2497
import numpy as np
import sip
import sys
from gnuradio import qtgui


class j2497_demod_method2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "J2497 Demod Method2")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("J2497 Demod Method2")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "j2497_demod_method2")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1000000
        self.whole_chirp = whole_chirp = (np.hstack((chirp(np.linspace(0,63E-6,63E-6*samp_rate),f0=203E3,f1=400E3,t1=63E-6,phi=0,method='linear')*1,chirp(np.linspace(63E-6,67E-6,4E-6*samp_rate),f0=400E3,f1=100E3,t1=67E-6,phi=0,method='linear')*1,chirp(np.linspace(67E-6,100E-6,33E-6*samp_rate),f0=100E3,f1=203E3,t1=100E-6,phi=-90,method='linear')*1)))[::-1]
        self.plot_samples = plot_samples = 300000
        self.chirp_section = chirp_section = np.hstack((chirp(np.linspace(0E-6,33E-6,33E-6*samp_rate),f0=203E3,f1=203E3,t1=33E-6,phi=-90,method='linear')*1))[::-1]

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
        	plot_samples, #size
        	1, #samp_rate
        	"Correlation Result", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-1, 210)

        self.qtgui_time_sink_x_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_win)
        self.fir_filter_xxx_1_0_0_0_0 = filter.fir_filter_fff(1, (10*[0.1]))
        self.fir_filter_xxx_1_0_0_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_1_0_0_0 = filter.fir_filter_fff(1, (10*[0.1]))
        self.fir_filter_xxx_1_0_0_0.declare_sample_delay(0)
        self.fft_filter_xxx_0_0 = filter.fft_filter_ccc(1, (whole_chirp), 1)
        self.fft_filter_xxx_0_0.declare_sample_delay(0)
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, (chirp_section), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_file_source_0_1_0_1 = blocks.file_source(gr.sizeof_gr_complex*1, '', False)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 135-30)
        self.blocks_complex_to_mag_squared_0_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.analog_rail_ff_0 = analog.rail_ff(200, 5000)
        self.J2497_j2497_tagger_0 = J2497.j2497_tagger()
        self.J2497_j2497_decoder_for_tagger_0 = J2497.j2497_decoder_for_tagger(True,6972)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.J2497_j2497_decoder_for_tagger_0, 'out'), (self.blocks_message_debug_0, 'print'))
        self.connect((self.J2497_j2497_tagger_0, 0), (self.fft_filter_xxx_0, 0))
        self.connect((self.analog_rail_ff_0, 0), (self.J2497_j2497_tagger_0, 1))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.fir_filter_xxx_1_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0_0, 0), (self.fir_filter_xxx_1_0_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.J2497_j2497_tagger_0, 0))
        self.connect((self.blocks_file_source_0_1_0_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.fft_filter_xxx_0_0, 0))
        self.connect((self.fft_filter_xxx_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.fft_filter_xxx_0_0, 0), (self.blocks_complex_to_mag_squared_0_0_0, 0))
        self.connect((self.fir_filter_xxx_1_0_0_0, 0), (self.analog_rail_ff_0, 0))
        self.connect((self.fir_filter_xxx_1_0_0_0_0, 0), (self.J2497_j2497_decoder_for_tagger_0, 0))
        self.connect((self.fir_filter_xxx_1_0_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "j2497_demod_method2")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_whole_chirp((np.hstack((chirp(np.linspace(0,63E-6,63E-6*self.samp_rate),f0=203E3,f1=400E3,t1=63E-6,phi=0,method='linear')*1,chirp(np.linspace(63E-6,67E-6,4E-6*self.samp_rate),f0=400E3,f1=100E3,t1=67E-6,phi=0,method='linear')*1,chirp(np.linspace(67E-6,100E-6,33E-6*self.samp_rate),f0=100E3,f1=203E3,t1=100E-6,phi=-90,method='linear')*1)))[::-1])
        self.set_chirp_section(np.hstack((chirp(np.linspace(0E-6,33E-6,33E-6*self.samp_rate),f0=203E3,f1=203E3,t1=33E-6,phi=-90,method='linear')*1))[::-1])
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_whole_chirp(self):
        return self.whole_chirp

    def set_whole_chirp(self, whole_chirp):
        self.whole_chirp = whole_chirp
        self.fft_filter_xxx_0_0.set_taps((self.whole_chirp))

    def get_plot_samples(self):
        return self.plot_samples

    def set_plot_samples(self, plot_samples):
        self.plot_samples = plot_samples

    def get_chirp_section(self):
        return self.chirp_section

    def set_chirp_section(self, chirp_section):
        self.chirp_section = chirp_section
        self.fft_filter_xxx_0.set_taps((self.chirp_section))


def main(top_block_cls=j2497_demod_method2, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
