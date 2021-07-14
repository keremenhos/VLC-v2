#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: keremenhos
# GNU Radio version: 3.8.3.0

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
from gnuradio import blocks
import numpy
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import epy_block_0
import math,cmath,numpy

from gnuradio import qtgui

class nono2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "nono2")

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
        self.sps = sps = 2
        self.span = span = 4
        self.samp_rate = samp_rate = 1000000
        self.filt_len = filt_len = span*sps+1
        self.rrrc = rrrc = firdes.root_raised_cosine(1.35, samp_rate,samp_rate/sps, 0.1, filt_len)
        self.freq = freq = 0.25
        self.dat_len = dat_len = 100
        self.quad = quad = numpy.multiply(rrrc,numpy.sin(numpy.array(range(filt_len))*2*math.pi*freq))
        self.inph = inph = numpy.multiply(rrrc,numpy.cos(numpy.array(range(filt_len))*2*math.pi*freq))
        self.frame_len = frame_len = dat_len*filt_len

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_2 = qtgui.time_sink_c(
            128, #size
            1, #samp_rate
            "", #name
            2 #number of inputs
        )
        self.qtgui_time_sink_x_2.set_update_time(10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
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


        for i in range(4):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_win)
        self._freq_range = Range(0, 0.5, 0.01, 0.25, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Frequency', "counter_slider", float)
        self.top_layout.addWidget(self._freq_win)
        self.fir_filter_xxx_1_0 = filter.fir_filter_fff(1, numpy.flip(inph))
        self.fir_filter_xxx_1_0.declare_sample_delay(0)
        self.fir_filter_xxx_1 = filter.fir_filter_fff(1, inph)
        self.fir_filter_xxx_1.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(1, numpy.flip(quad))
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(1, quad)
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.epy_block_0 = epy_block_0.blk(example_param=1.0)
        self.blocks_vector_insert_x_0_0 = blocks.vector_insert_f([0]*filt_len, filt_len+1, 0)
        self.blocks_vector_insert_x_0 = blocks.vector_insert_f([0]*filt_len, filt_len+1, 0)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_gr_complex, 1, 100, "data_len")
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 1, filt_len+1, filt_len-2)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_random_source_x_0_0 = blocks.vector_source_i(list(map(int, numpy.random.randint(0, 4, dat_len))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_1, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_vector_insert_x_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_vector_insert_x_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_2, 1))
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_keep_m_in_n_0, 0))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.fir_filter_xxx_1_0, 0))
        self.connect((self.blocks_vector_insert_x_0, 0), (self.fir_filter_xxx_1, 0))
        self.connect((self.blocks_vector_insert_x_0_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_float_to_complex_1, 1))
        self.connect((self.fir_filter_xxx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.fir_filter_xxx_1_0, 0), (self.blocks_float_to_complex_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "nono2")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_filt_len(self.span*self.sps+1)
        self.set_rrrc(firdes.root_raised_cosine(1.35, self.samp_rate, self.samp_rate/self.sps, 0.1, self.filt_len))

    def get_span(self):
        return self.span

    def set_span(self, span):
        self.span = span
        self.set_filt_len(self.span*self.sps+1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_rrrc(firdes.root_raised_cosine(1.35, self.samp_rate, self.samp_rate/self.sps, 0.1, self.filt_len))
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)

    def get_filt_len(self):
        return self.filt_len

    def set_filt_len(self, filt_len):
        self.filt_len = filt_len
        self.set_frame_len(self.dat_len*self.filt_len)
        self.set_inph(numpy.multiply(self.rrrc,numpy.cos(numpy.array(range(self.filt_len))*2*math.pi*self.freq)))
        self.set_quad(numpy.multiply(self.rrrc,numpy.sin(numpy.array(range(self.filt_len))*2*math.pi*self.freq)))
        self.set_rrrc(firdes.root_raised_cosine(1.35, self.samp_rate, self.samp_rate/self.sps, 0.1, self.filt_len))
        self.blocks_keep_m_in_n_0.set_offset(self.filt_len-2)
        self.blocks_keep_m_in_n_0.set_n(self.filt_len+1)

    def get_rrrc(self):
        return self.rrrc

    def set_rrrc(self, rrrc):
        self.rrrc = rrrc
        self.set_inph(numpy.multiply(self.rrrc,numpy.cos(numpy.array(range(self.filt_len))*2*math.pi*self.freq)))
        self.set_quad(numpy.multiply(self.rrrc,numpy.sin(numpy.array(range(self.filt_len))*2*math.pi*self.freq)))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_inph(numpy.multiply(self.rrrc,numpy.cos(numpy.array(range(self.filt_len))*2*math.pi*self.freq)))
        self.set_quad(numpy.multiply(self.rrrc,numpy.sin(numpy.array(range(self.filt_len))*2*math.pi*self.freq)))

    def get_dat_len(self):
        return self.dat_len

    def set_dat_len(self, dat_len):
        self.dat_len = dat_len
        self.set_frame_len(self.dat_len*self.filt_len)

    def get_quad(self):
        return self.quad

    def set_quad(self, quad):
        self.quad = quad
        self.fir_filter_xxx_0.set_taps(self.quad)
        self.fir_filter_xxx_0_0.set_taps(numpy.flip(self.quad))

    def get_inph(self):
        return self.inph

    def set_inph(self, inph):
        self.inph = inph
        self.fir_filter_xxx_1.set_taps(self.inph)
        self.fir_filter_xxx_1_0.set_taps(numpy.flip(self.inph))

    def get_frame_len(self):
        return self.frame_len

    def set_frame_len(self, frame_len):
        self.frame_len = frame_len





def main(top_block_cls=nono2, options=None):

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
