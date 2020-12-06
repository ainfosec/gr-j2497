#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: J2497 Demod Method3
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
import math
from gnuradio import blocks
import pmt
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import j2497
from gnuradio import qtgui

class j2497_demod_method3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "J2497 Demod Method3")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("J2497 Demod Method3")
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

        self.settings = Qt.QSettings("GNU Radio", "j2497_demod_method3")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samples = samples = 50000
        self.samp_rate = samp_rate = 1000000
        self.if_peak_threshold = if_peak_threshold = 1
        self.if_peak_offset = if_peak_offset = 106
        self.amp_threshold = amp_threshold = 0.5

        ##################################################
        # Blocks
        ##################################################
        self._if_peak_threshold_range = Range(0, 10, 0.1, 1, 200)
        self._if_peak_threshold_win = RangeWidget(self._if_peak_threshold_range, self.set_if_peak_threshold, 'IF Peak Threshold', "counter_slider", float)
        self.top_grid_layout.addWidget(self._if_peak_threshold_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._if_peak_offset_range = Range(0, 200, 1, 106, 200)
        self._if_peak_offset_win = RangeWidget(self._if_peak_offset_range, self.set_if_peak_offset, 'IF Peak Offset', "counter_slider", int)
        self.top_grid_layout.addWidget(self._if_peak_offset_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._amp_threshold_range = Range(0, 10, 0.1, 0.5, 200)
        self._amp_threshold_win = RangeWidget(self._amp_threshold_range, self.set_amp_threshold, 'Amplitude Threshold', "counter_slider", float)
        self.top_grid_layout.addWidget(self._amp_threshold_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_1 = qtgui.time_sink_f(
            100000, #size
            1, #samp_rate
            "Instantaneous Frequency", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1.set_y_axis(0, 10)

        self.qtgui_time_sink_x_0_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1.enable_tags(True)
        self.qtgui_time_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_1.enable_stem_plot(False)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_1_win)
        self.j2497_J2497_decoder_0 = j2497.J2497_decoder(if_peak_threshold,if_peak_offset,False,6972)
        self.fir_filter_xxx_1 = filter.fir_filter_fff(1, 10*[0.1])
        self.fir_filter_xxx_1.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(1, [.25, .25, .25, .25])
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(amp_threshold, amp_threshold, 0)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_float * 1, False)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 1)
        self.blocks_file_source_0_1_0_1 = blocks.file_source(gr.sizeof_gr_complex*1, '', False, 0, 0)
        self.blocks_file_source_0_1_0_1.set_begin_tag(pmt.PMT_NIL)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 5)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_burst_tagger_0 = blocks.burst_tagger(gr.sizeof_gr_complex)
        self.blocks_burst_tagger_0.set_true_tag('burst',True)
        self.blocks_burst_tagger_0.set_false_tag('burst',False)
        self.analog_quadrature_demod_cf_0_0 = analog.quadrature_demod_cf(1)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.j2497_J2497_decoder_0, 'out'), (self.blocks_message_debug_0, 'print'))
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.blocks_burst_tagger_0, 0), (self.analog_quadrature_demod_cf_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.fir_filter_xxx_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_burst_tagger_0, 0))
        self.connect((self.blocks_file_source_0_1_0_1, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_burst_tagger_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.j2497_J2497_decoder_0, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.qtgui_time_sink_x_0_0_1, 0))
        self.connect((self.fir_filter_xxx_1, 0), (self.blocks_threshold_ff_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "j2497_demod_method3")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samples(self):
        return self.samples

    def set_samples(self, samples):
        self.samples = samples

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_if_peak_threshold(self):
        return self.if_peak_threshold

    def set_if_peak_threshold(self, if_peak_threshold):
        self.if_peak_threshold = if_peak_threshold

    def get_if_peak_offset(self):
        return self.if_peak_offset

    def set_if_peak_offset(self, if_peak_offset):
        self.if_peak_offset = if_peak_offset

    def get_amp_threshold(self):
        return self.amp_threshold

    def set_amp_threshold(self, amp_threshold):
        self.amp_threshold = amp_threshold
        self.blocks_threshold_ff_0.set_hi(self.amp_threshold)
        self.blocks_threshold_ff_0.set_lo(self.amp_threshold)



def main(top_block_cls=j2497_demod_method3, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
