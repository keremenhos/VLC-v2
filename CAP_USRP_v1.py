#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: CAP_USRP_v1
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
from PyQt5.QtCore import QObject, pyqtSlot
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
from gnuradio.qtgui import Range, RangeWidget
import epy_block_1
import math,cmath,numpy

from gnuradio import qtgui

class CAP_USRP_v1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "CAP_USRP_v1")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("CAP_USRP_v1")
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

        self.settings = Qt.QSettings("GNU Radio", "CAP_USRP_v1")

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
        self.sps = sps = 4
        self.span = span = 4
        self.samp_rate = samp_rate = 1000000
        self.fram_len = fram_len = 4096
        self.filt_len = filt_len = span*sps+1
        self.rrrc = rrrc = firdes.root_raised_cosine(numpy.sqrt(sps*2), samp_rate,samp_rate/sps, 0.1, filt_len)
        self.freq = freq = 0.25
        self.dat_len = dat_len = fram_len//filt_len
        self.M = M = 4
        self.quad = quad = numpy.multiply(rrrc,numpy.sin(numpy.array(range(filt_len))*2*math.pi*freq))
        self.inph = inph = numpy.multiply(rrrc,numpy.cos(numpy.array(range(filt_len))*2*math.pi*freq))
        self.frame_len = frame_len = (dat_len*filt_len)
        self.Data_0 = Data_0 = [3,3,2,2,0,0,1,1,0,0,3,3,1,2,1,1,0,1,3,3,0,2,2,2,1,3,3,2,3,2,3,0,0,0,1,3,0,2,1,3,1,3,3,3,2,2,2,1,0,2,1,2,0,1,0,0,1,0,1,1,1,1,2,1,2,2,2,3,3,3,2,0,0,3,2,0,2,0,2,3,2,1,2,3,1,1,2,1,1,2,2,0,3,1,1,1,3,2,0,1,2,3,3,1,1,3,0,1,0,2,3,1,0,2,2,2,2,2,1,3,3,1,0,3,3,3,1,3,0,1,2,0,1,0,2,1,1,3,3,1,1,1,2,1,1,1,2,0,0,3,2,0,3,3,0,1,2,1,3,0,2,2,0,2,2,1,0,3,2,2,0,3,1,2,1,3,0,3,3,3,0,2,3,1,0,2,2,0,2,1,2,2,0,3,2,0,1,3,2,3,1,1,2,3,0,1,1,2,3,2,2,2,1,0,0,0,1,3,1,3,1,2,1,1,1,1,1,3,2,2,2,2,1,2,3,0,1,0,2,2]
        self.Data = Data = numpy.random.randint(M,size=dat_len)

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_1_2 = qtgui.time_sink_c(
            256, #size
            samp_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1_2.set_update_time(0.1)
        self.qtgui_time_sink_x_1_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_2.enable_tags(True)
        self.qtgui_time_sink_x_1_2.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, 'pck')
        self.qtgui_time_sink_x_1_2.enable_autoscale(False)
        self.qtgui_time_sink_x_1_2.enable_grid(False)
        self.qtgui_time_sink_x_1_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_2.enable_control_panel(False)
        self.qtgui_time_sink_x_1_2.enable_stem_plot(False)


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


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_1_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_2_win = sip.wrapinstance(self.qtgui_time_sink_x_1_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_2_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._freq_range = Range(0, 0.5, 0.05, 0.25, 200)
        self._freq_win = RangeWidget(self._freq_range, self.set_freq, 'Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._freq_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        # Create the options list
        self._M_options = [4, 16, 64, 256, 1024]
        # Create the labels list
        self._M_labels = ['4', '16', '64', '256', '1024']
        # Create the combo box
        # Create the radio buttons
        self._M_group_box = Qt.QGroupBox('Modulation Order' + ": ")
        self._M_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._M_button_group = variable_chooser_button_group()
        self._M_group_box.setLayout(self._M_box)
        for i, _label in enumerate(self._M_labels):
            radio_button = Qt.QRadioButton(_label)
            self._M_box.addWidget(radio_button)
            self._M_button_group.addButton(radio_button, i)
        self._M_callback = lambda i: Qt.QMetaObject.invokeMethod(self._M_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._M_options.index(i)))
        self._M_callback(self.M)
        self._M_button_group.buttonClicked[int].connect(
            lambda i: self.set_M(self._M_options[i]))
        self.top_grid_layout.addWidget(self._M_group_box, 3, 1, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_center_freq(0, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        # No synchronization enforced.
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
        self.qtgui_time_sink_x_3 = qtgui.time_sink_f(
            8192, #size
            samp_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_3.set_update_time(0.10)
        self.qtgui_time_sink_x_3.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_3.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_3.enable_tags(True)
        self.qtgui_time_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, 'pck')
        self.qtgui_time_sink_x_3.enable_autoscale(False)
        self.qtgui_time_sink_x_3.enable_grid(False)
        self.qtgui_time_sink_x_3.enable_axis_labels(True)
        self.qtgui_time_sink_x_3.enable_control_panel(False)
        self.qtgui_time_sink_x_3.enable_stem_plot(False)


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
                self.qtgui_time_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_3_win = sip.wrapinstance(self.qtgui_time_sink_x_3.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_3_win)
        self.fir_filter_xxx_1_0 = filter.fir_filter_fff(1, numpy.flip(inph))
        self.fir_filter_xxx_1_0.declare_sample_delay(0)
        self.fir_filter_xxx_0_0 = filter.fir_filter_fff(1, numpy.flip(quad))
        self.fir_filter_xxx_0_0.declare_sample_delay(0)
        self.epy_block_1 = epy_block_1.blk(frame_length=frame_len)
        self.digital_corr_est_cc_0 = digital.corr_est_cc([0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0], 1, 509, 0.05, digital.THRESHOLD_ABSOLUTE)
        self.blocks_vector_source_x_1 = blocks.vector_source_f(range(frame_len), True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_f([0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0], True, 1, [])
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_float*1, 'packet_len', 0)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_float * 1, False)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_stream_to_tagged_stream_2 = blocks.stream_to_tagged_stream(gr.sizeof_float, 1, frame_len, 'pck')
        self.blocks_stream_to_tagged_stream_1 = blocks.stream_to_tagged_stream(gr.sizeof_float, 1, frame_len, 'packet_len')
        self.blocks_stream_to_tagged_stream_1.set_max_output_buffer(8192)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_float, 1, 510, 'packet_len')
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(1/(frame_len-1))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(1)
        self.blocks_keep_m_in_n_1 = blocks.keep_m_in_n(gr.sizeof_float, frame_len, fram_len, 0)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 1, filt_len, filt_len-2)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_1 = blocks.complex_to_float(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_float_1, 0), (self.epy_block_1, 0))
        self.connect((self.blocks_complex_to_float_1, 0), (self.qtgui_time_sink_x_3, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_keep_m_in_n_0, 0))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.qtgui_time_sink_x_1_2, 0))
        self.connect((self.blocks_keep_m_in_n_1, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_stream_to_tagged_stream_1, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_1, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_stream_to_tagged_stream_2, 0), (self.fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_2, 0), (self.fir_filter_xxx_1_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_stream_to_tagged_stream_2, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_vector_source_x_1, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.digital_corr_est_cc_0, 0), (self.blocks_complex_to_float_1, 0))
        self.connect((self.epy_block_1, 0), (self.blocks_keep_m_in_n_1, 0))
        self.connect((self.fir_filter_xxx_0_0, 0), (self.blocks_float_to_complex_1, 1))
        self.connect((self.fir_filter_xxx_1_0, 0), (self.blocks_float_to_complex_1, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.digital_corr_est_cc_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "CAP_USRP_v1")
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
        self.qtgui_time_sink_x_1_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_3.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_fram_len(self):
        return self.fram_len

    def set_fram_len(self, fram_len):
        self.fram_len = fram_len
        self.set_dat_len(self.fram_len//self.filt_len)
        self.blocks_keep_m_in_n_1.set_n(self.fram_len)

    def get_filt_len(self):
        return self.filt_len

    def set_filt_len(self, filt_len):
        self.filt_len = filt_len
        self.set_dat_len(self.fram_len//self.filt_len)
        self.set_frame_len((self.dat_len*self.filt_len))
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
        self.set_Data(numpy.random.randint(self.M,size=self.dat_len))
        self.set_frame_len((self.dat_len*self.filt_len))

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Data(numpy.random.randint(self.M,size=self.dat_len))
        self._M_callback(self.M)

    def get_quad(self):
        return self.quad

    def set_quad(self, quad):
        self.quad = quad
        self.fir_filter_xxx_0_0.set_taps(numpy.flip(self.quad))

    def get_inph(self):
        return self.inph

    def set_inph(self, inph):
        self.inph = inph
        self.fir_filter_xxx_1_0.set_taps(numpy.flip(self.inph))

    def get_frame_len(self):
        return self.frame_len

    def set_frame_len(self, frame_len):
        self.frame_len = frame_len
        self.blocks_keep_m_in_n_1.set_m(self.frame_len)
        self.blocks_multiply_const_vxx_1.set_k(1/(self.frame_len-1))
        self.blocks_stream_to_tagged_stream_1.set_packet_len(self.frame_len)
        self.blocks_stream_to_tagged_stream_1.set_packet_len_pmt(self.frame_len)
        self.blocks_stream_to_tagged_stream_2.set_packet_len(self.frame_len)
        self.blocks_stream_to_tagged_stream_2.set_packet_len_pmt(self.frame_len)
        self.blocks_vector_source_x_1.set_data(range(self.frame_len), [])
        self.epy_block_1.frame_length = self.frame_len

    def get_Data_0(self):
        return self.Data_0

    def set_Data_0(self, Data_0):
        self.Data_0 = Data_0

    def get_Data(self):
        return self.Data

    def set_Data(self, Data):
        self.Data = Data





def main(top_block_cls=CAP_USRP_v1, options=None):

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
