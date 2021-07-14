#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Kerem
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
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio import zeromq
from gnuradio.qtgui import Range, RangeWidget
import epy_block_0
import epy_block_1
import epy_block_3
import epy_block_4
import epy_block_5
import epy_module_0  # embedded python module
import math,cmath,numpy, random, time

from gnuradio import qtgui

class kerem(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Kerem")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Kerem")
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

        self.settings = Qt.QSettings("GNU Radio", "kerem")

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
        self.sps = sps = 8
        self.span = span = 8
        self.samp_rate = samp_rate = 1.25e6
        self.fram_len = fram_len = 4096
        self.filt_len = filt_len = span*sps+1
        self.rrrc = rrrc = firdes.root_raised_cosine(numpy.sqrt(sps*2), samp_rate,samp_rate/sps, 0.1, filt_len)
        self.freq = freq = 0.25
        self.dat_len = dat_len = (fram_len//filt_len)
        self.M = M = 16
        self.thresh = thresh = 0.05
        self.quad = quad = numpy.multiply(rrrc,numpy.sin(numpy.array(range(filt_len))*2*math.pi*freq))
        self.inph = inph = numpy.multiply(rrrc,numpy.cos(numpy.array(range(filt_len))*2*math.pi*freq))
        self.frame_len = frame_len = dat_len*filt_len
        self.TT = TT = 1
        self.P = P = 0
        self.Data = Data = numpy.array(numpy.random.randint(M,size=dat_len))

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            4096, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, 0.0, 0, 'pck')
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not False)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            4096, #size
            "", #name
            1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.1)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 0, 'pck')
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(True)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 0, 0, 2, 1)
        for r in range(0, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_range = Range(0, 0.5, 0.05, 0.25, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._thresh_range = Range(0.0001, 0.1, 0.0005, 0.05, 200)
        self._thresh_win = RangeWidget(self._thresh_range, self.set_thresh, 'thresh', "counter_slider", float)
        self.top_layout.addWidget(self._thresh_win)
        self._TT_range = Range(0.3, 2, 0.01, 1, 200)
        self._TT_win = RangeWidget(self._TT_range, self.set_TT, 'TT', "counter_slider", float)
        self.top_layout.addWidget(self._TT_win)
        _P_check_box = Qt.QCheckBox('Print BER')
        self._P_choices = {True: 1, False: 0}
        self._P_choices_inv = dict((v,k) for k,v in self._P_choices.items())
        self._P_callback = lambda i: Qt.QMetaObject.invokeMethod(_P_check_box, "setChecked", Qt.Q_ARG("bool", self._P_choices_inv[i]))
        self._P_callback(self.P)
        _P_check_box.stateChanged.connect(lambda i: self.set_P(self._P_choices[bool(i)]))
        self.top_layout.addWidget(_P_check_box)
        self.zeromq_pull_source_0 = zeromq.pull_source(gr.sizeof_gr_complex, 1, 'tcp://192.168.1.36:50241', 100, False, -1)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            '',
        )
        self.uhd_usrp_sink_0.set_center_freq(0, 0)
        self.uhd_usrp_sink_0.set_gain(0, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        # No synchronization enforced.
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 30000)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, 'corr_est')
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


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


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.fir_filter_xxx_1_0 = filter.fir_filter_fff(1, numpy.flip(inph))
        self.fir_filter_xxx_1_0.declare_sample_delay(0)
        self.fir_filter_xxx_1 = filter.fir_filter_fff(1, inph)
        self.fir_filter_xxx_1.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(1, numpy.flip(quad))
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.fir_filter_xxx_0 = filter.fir_filter_fff(1, quad)
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.epy_block_5 = epy_block_5.blk(data=Data, M=M, display_BER=P, num_bits=1e6)
        self.epy_block_4 = epy_block_4.blk(M=M)
        self.epy_block_3 = epy_block_3.blk(data=Data, M=M, ttt=TT)
        self.epy_block_1 = epy_block_1.blk(frame_length=fram_len)
        self.epy_block_0 = epy_block_0.blk(M=M)
        self.digital_corr_est_cc_0 = digital.corr_est_cc([-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,-1,1,1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,1,-1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,1,1,1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,1,1,-1,1,-1,-1,1,1,-1,1,-1,1,1,1,-1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,1,1,1,1,1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,-1,-1,-1,-1], 1, 509, thresh, digital.THRESHOLD_ABSOLUTE)
        self.blocks_vector_source_x_0_0 = blocks.vector_source_i(Data, True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_f([-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,-1,1,1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,1,-1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,1,1,1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,1,1,-1,1,-1,-1,1,1,-1,1,-1,1,1,1,-1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,1,1,1,1,1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,-1,-1,-1,-1], True, 1, [])
        self.blocks_vector_insert_x_0_0 = blocks.vector_insert_f([0]*(filt_len-1), filt_len, 0)
        self.blocks_vector_insert_x_0 = blocks.vector_insert_f([0]*(filt_len-1), filt_len, 0)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_float*1, 'packet_len', 0)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_float * 1, False)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_stream_to_tagged_stream_2 = blocks.stream_to_tagged_stream(gr.sizeof_float, 1, frame_len, 'pck')
        self.blocks_stream_to_tagged_stream_1 = blocks.stream_to_tagged_stream(gr.sizeof_float, 1, frame_len, 'packet_len')
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_float, 1, 510, 'packet_len')
        self.blocks_keep_m_in_n_1 = blocks.keep_m_in_n(gr.sizeof_float, frame_len, fram_len, 0)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 1, filt_len, filt_len-2)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_float_1 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_stream_to_tagged_stream_1, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_vector_insert_x_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_vector_insert_x_0_0, 0))
        self.connect((self.blocks_complex_to_float_1, 0), (self.epy_block_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_keep_m_in_n_0, 0))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.epy_block_3, 0))
        self.connect((self.blocks_keep_m_in_n_1, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_1, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_stream_to_tagged_stream_2, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_2, 0), (self.fir_filter_xxx_1_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_2, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_stream_to_tagged_stream_2, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_vector_insert_x_0, 0), (self.fir_filter_xxx_1, 0))
        self.connect((self.blocks_vector_insert_x_0_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.epy_block_0, 0))
        self.connect((self.digital_corr_est_cc_0, 0), (self.blocks_complex_to_float_1, 0))
        self.connect((self.digital_corr_est_cc_0, 1), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.epy_block_1, 0), (self.blocks_keep_m_in_n_1, 0))
        self.connect((self.epy_block_3, 0), (self.epy_block_4, 0))
        self.connect((self.epy_block_3, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.epy_block_4, 0), (self.epy_block_5, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_float_to_complex_1, 1))
        self.connect((self.fir_filter_xxx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.fir_filter_xxx_1_0, 0), (self.blocks_float_to_complex_1, 0))
        self.connect((self.zeromq_pull_source_0, 0), (self.digital_corr_est_cc_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "kerem")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_filt_len(self.span*self.sps+1)
        self.set_rrrc(firdes.root_raised_cosine(numpy.sqrt(self.sps*2), self.samp_rate, self.samp_rate/self.sps, 0.1, self.filt_len))

    def get_span(self):
        return self.span

    def set_span(self, span):
        self.span = span
        self.set_filt_len(self.span*self.sps+1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_rrrc(firdes.root_raised_cosine(numpy.sqrt(self.sps*2), self.samp_rate, self.samp_rate/self.sps, 0.1, self.filt_len))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_fram_len(self):
        return self.fram_len

    def set_fram_len(self, fram_len):
        self.fram_len = fram_len
        self.set_dat_len((self.fram_len//self.filt_len))
        self.blocks_keep_m_in_n_1.set_n(self.fram_len)
        self.epy_block_1.frame_length = self.fram_len

    def get_filt_len(self):
        return self.filt_len

    def set_filt_len(self, filt_len):
        self.filt_len = filt_len
        self.set_dat_len((self.fram_len//self.filt_len))
        self.set_frame_len(self.dat_len*self.filt_len)
        self.set_inph(numpy.multiply(self.rrrc,numpy.cos(numpy.array(range(self.filt_len))*2*math.pi*self.freq)))
        self.set_quad(numpy.multiply(self.rrrc,numpy.sin(numpy.array(range(self.filt_len))*2*math.pi*self.freq)))
        self.set_rrrc(firdes.root_raised_cosine(numpy.sqrt(self.sps*2), self.samp_rate, self.samp_rate/self.sps, 0.1, self.filt_len))
        self.blocks_keep_m_in_n_0.set_offset(self.filt_len-2)
        self.blocks_keep_m_in_n_0.set_n(self.filt_len)

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
        self.set_Data(numpy.array(numpy.random.randint(self.M,size=self.dat_len)))
        self.set_frame_len(self.dat_len*self.filt_len)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Data(numpy.array(numpy.random.randint(self.M,size=self.dat_len)))
        self.epy_block_0.M = self.M
        self.epy_block_3.M = self.M
        self.epy_block_4.M = self.M

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh
        self.digital_corr_est_cc_0.set_threshold(self.thresh)

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
        self.blocks_keep_m_in_n_1.set_m(self.frame_len)
        self.blocks_stream_to_tagged_stream_1.set_packet_len(self.frame_len)
        self.blocks_stream_to_tagged_stream_1.set_packet_len_pmt(self.frame_len)
        self.blocks_stream_to_tagged_stream_2.set_packet_len(self.frame_len)
        self.blocks_stream_to_tagged_stream_2.set_packet_len_pmt(self.frame_len)

    def get_TT(self):
        return self.TT

    def set_TT(self, TT):
        self.TT = TT
        self.epy_block_3.ttt = self.TT

    def get_P(self):
        return self.P

    def set_P(self, P):
        self.P = P
        self._P_callback(self.P)
        self.epy_block_5.display_BER = self.P

    def get_Data(self):
        return self.Data

    def set_Data(self, Data):
        self.Data = Data
        self.blocks_vector_source_x_0_0.set_data(self.Data, [])
        self.epy_block_3.data = self.Data





def main(top_block_cls=kerem, options=None):

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
