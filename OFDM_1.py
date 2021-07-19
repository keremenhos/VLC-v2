#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: OFDM_1
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
import sip
from gnuradio import blocks
from gnuradio import digital
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
import epy_block_0
import epy_block_1
import epy_block_2
import epy_block_3
import epy_block_4
import epy_module_0  # embedded python module
import math,cmath,numpy, random, time

from gnuradio import qtgui

class OFDM_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "OFDM_1")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("OFDM_1")
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

        self.settings = Qt.QSettings("GNU Radio", "OFDM_1")

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
        self.pilot_sc = pilot_sc = 36
        self.null = null = 35
        self.data_sc = data_sc = 36
        self.ppsc = ppsc = numpy.arange(-1*((data_sc+pilot_sc)//(pilot_sc*2)),((data_sc+pilot_sc)/2),((data_sc+pilot_sc)/pilot_sc))[numpy.arange(-1*((data_sc+pilot_sc)//(pilot_sc*2)),((data_sc+pilot_sc)/2),((data_sc+pilot_sc)/pilot_sc))>0].astype(int)+1+(null//2)
        self.pck_len = pck_len = 4096
        self.fft_len = fft_len = 128
        self.spf = spf = (pck_len-510)//fft_len
        self.pilot_symbols = pilot_symbols = numpy.array(numpy.random.randint(2,size=pilot_sc//2))*2 -1
        self.pdsc = pdsc = numpy.delete((numpy.arange((data_sc+pilot_sc)//2)+1+(null//2)),((numpy.arange((data_sc+pilot_sc)//2)+1+(null//2))[:, None] == ppsc).argmax(axis=0))
        self.M = M = 16
        self.samp_rate = samp_rate = 1250000
        self.psc = psc = numpy.sort(list(ppsc*-1) + list(ppsc))
        self.ps = ps = list(numpy.flip(pilot_symbols)) + list(pilot_symbols)
        self.guard = guard = fft_len-null-data_sc-pilot_sc
        self.dsc = dsc = numpy.sort(list(pdsc*-1) + list(pdsc))
        self.corr_thresh = corr_thresh = 0.04
        self.TX_GAIN = TX_GAIN = 34
        self.P = P = 0
        self.Data = Data = numpy.array(numpy.random.randint(M,size=(data_sc//2)*spf))

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            spf*(data_sc//2), #size
            "", #name
            1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "Sym#")
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 0, 0, 2, 2)
        for r in range(0, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._corr_thresh_range = Range(0.01, 0.1, 0.005, 0.04, 200)
        self._corr_thresh_win = RangeWidget(self._corr_thresh_range, self.set_corr_thresh, 'corr_thresh', "counter_slider", float)
        self.top_layout.addWidget(self._corr_thresh_win)
        self._TX_GAIN_range = Range(1, 100, 1, 34, 200)
        self._TX_GAIN_win = RangeWidget(self._TX_GAIN_range, self.set_TX_GAIN, 'TX_GAIN', "counter_slider", float)
        self.top_layout.addWidget(self._TX_GAIN_win)
        _P_check_box = Qt.QCheckBox('Print BER')
        self._P_choices = {True: 1, False: 0}
        self._P_choices_inv = dict((v,k) for k,v in self._P_choices.items())
        self._P_callback = lambda i: Qt.QMetaObject.invokeMethod(_P_check_box, "setChecked", Qt.Q_ARG("bool", self._P_choices_inv[i]))
        self._P_callback(self.P)
        _P_check_box.stateChanged.connect(lambda i: self.set_P(self._P_choices[bool(i)]))
        self.top_layout.addWidget(_P_check_box)
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
        self.fft_vxx_0_0 = fft.fft_vcc(fft_len, True, [], True, 1)
        self.fft_vxx_0 = fft.fft_vcc(fft_len, False, [], True, 1)
        self.epy_block_4 = epy_block_4.blk(M=M)
        self.epy_block_3 = epy_block_3.blk(data=Data, M=M, display_BER=P, num_bits=1e6)
        self.epy_block_2 = epy_block_2.blk(M=M, data_subcarrier=data_sc, pilot_subcarrier=pilot_sc, null_subcarrier=null, guard_subcarrier=guard, fft_size=fft_len, pilot_symbols=pilot_symbols, symbols_per_frame=spf)
        self.epy_block_1 = epy_block_1.blk(frame_length=pck_len)
        self.epy_block_0 = epy_block_0.blk(data=Data, M=M, data_subcarrier=data_sc, pilot_subcarrier=pilot_sc, null_subcarrier=null, guard_subcarrier=guard, fft_size=fft_len, pilot_symbols=pilot_symbols, spf=spf)
        self.digital_ofdm_carrier_allocator_cvc_0 = digital.ofdm_carrier_allocator_cvc( fft_len, ((dsc) ,), ((psc),), ((ps),), [], "frame_len", True)
        self.digital_corr_est_cc_0 = digital.corr_est_cc([-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,-1,1,1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,1,-1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,1,1,1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,1,1,-1,1,-1,-1,1,1,-1,1,-1,1,1,1,-1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,1,1,1,1,1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,-1,-1,-1,-1], 1, 509, corr_thresh, digital.THRESHOLD_ABSOLUTE)
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_len)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_len)
        self.blocks_vector_source_x_0_1 = blocks.vector_source_f([-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,-1,-1,1,1,1,-1,1,-1,1,-1,1,1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,1,1,1,1,-1,-1,1,1,1,1,-1,-1,-1,1,-1,1,1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,1,-1,-1,1,1,-1,-1,1,1,1,-1,1,-1,-1,-1,1,1,1,1,1,-1,1,1,1,1,-1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,1,1,1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,1,1,-1,-1,1,1,-1,1,1,-1,1,1,1,1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,1,1,-1,1,-1,1,1,1,1,-1,-1,1,-1,-1,1,-1,1,1,1,-1,-1,1,1,1,-1,-1,-1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,-1,-1,1,1,1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,1,-1,1,1,1,1,1,-1,1,-1,1,1,-1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,1,-1,1,1,-1,1,1,-1,1,-1,1,1,-1,-1,-1,-1,-1,1,-1,1,1,1,-1,1,1,1,1,1,-1,-1,-1,1,1,1,1,-1,-1,1,1,-1,1,-1,-1,1,1,-1,1,-1,1,1,1,-1,-1,-1,1,1,-1,1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,-1,1,-1,-1,1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,-1,-1,-1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,1,1,1,1,1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,1,1,1,-1,1,1,-1,-1,1,-1,1,1,1,1,-1,1,1,-1,-1,-1,-1,1,1,-1,1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,-1,-1,-1,-1], True, 1, [])
        self.blocks_tagged_stream_mux_1 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, 'packet_len', 0)
        self.blocks_tag_gate_1 = blocks.tag_gate(gr.sizeof_gr_complex * 1, False)
        self.blocks_tag_gate_1.set_single_key("sym")
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_float * 1, False)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_len)
        self.blocks_stream_to_tagged_stream_3 = blocks.stream_to_tagged_stream(gr.sizeof_gr_complex, fft_len, 1, 'sym')
        self.blocks_stream_to_tagged_stream_1 = blocks.stream_to_tagged_stream(gr.sizeof_gr_complex, 1, fft_len*spf, "packet_len")
        self.blocks_stream_to_tagged_stream_0_0_0_0_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_gr_complex, 1, data_sc, "frame_len")
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_float, 1, 510, 'packet_len')
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(1/TX_GAIN)
        self.blocks_keep_m_in_n_1 = blocks.keep_m_in_n(gr.sizeof_float, fft_len*spf, pck_len, 1)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_1 = blocks.complex_to_float(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_float_1, 0), (self.epy_block_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_tagged_stream_mux_1, 0))
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_1, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_stream_to_tagged_stream_1, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0_0_0_0_0, 0), (self.digital_ofdm_carrier_allocator_cvc_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_1, 0), (self.blocks_tagged_stream_mux_1, 1))
        self.connect((self.blocks_stream_to_tagged_stream_3, 0), (self.blocks_vector_to_stream_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_float_to_complex_1, 0))
        self.connect((self.blocks_tag_gate_1, 0), (self.epy_block_4, 0))
        self.connect((self.blocks_tag_gate_1, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_tagged_stream_mux_1, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_vector_source_x_0_1, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.epy_block_2, 0))
        self.connect((self.digital_corr_est_cc_0, 0), (self.blocks_complex_to_float_1, 0))
        self.connect((self.digital_ofdm_carrier_allocator_cvc_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_stream_to_tagged_stream_0_0_0_0_0_0, 0))
        self.connect((self.epy_block_1, 0), (self.blocks_keep_m_in_n_1, 0))
        self.connect((self.epy_block_2, 0), (self.blocks_tag_gate_1, 0))
        self.connect((self.epy_block_4, 0), (self.epy_block_3, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_stream_to_tagged_stream_3, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.digital_corr_est_cc_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "OFDM_1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_pilot_sc(self):
        return self.pilot_sc

    def set_pilot_sc(self, pilot_sc):
        self.pilot_sc = pilot_sc
        self.set_guard(self.fft_len-self.null-self.data_sc-self.pilot_sc)
        self.set_pdsc(numpy.delete((numpy.arange((self.data_sc+self.pilot_sc)//2)+1+(self.null//2)),((numpy.arange((self.data_sc+self.pilot_sc)//2)+1+(self.null//2))[:, None] == self.ppsc).argmax(axis=0))
        )
        self.set_pilot_symbols(numpy.array(numpy.random.randint(2,size=self.pilot_sc//2))*2 -1)
        self.set_ppsc(numpy.arange(-1*((self.data_sc+self.pilot_sc)//(self.pilot_sc*2)),((self.data_sc+self.pilot_sc)/2),((self.data_sc+self.pilot_sc)/self.pilot_sc))[numpy.arange(-1*((self.data_sc+self.pilot_sc)//(self.pilot_sc*2)),((self.data_sc+self.pilot_sc)/2),((self.data_sc+self.pilot_sc)/self.pilot_sc))>0].astype(int)+1+(self.null//2))
        self.epy_block_0.pilot_subcarrier = self.pilot_sc

    def get_null(self):
        return self.null

    def set_null(self, null):
        self.null = null
        self.set_guard(self.fft_len-self.null-self.data_sc-self.pilot_sc)
        self.set_pdsc(numpy.delete((numpy.arange((self.data_sc+self.pilot_sc)//2)+1+(self.null//2)),((numpy.arange((self.data_sc+self.pilot_sc)//2)+1+(self.null//2))[:, None] == self.ppsc).argmax(axis=0))
        )
        self.set_ppsc(numpy.arange(-1*((self.data_sc+self.pilot_sc)//(self.pilot_sc*2)),((self.data_sc+self.pilot_sc)/2),((self.data_sc+self.pilot_sc)/self.pilot_sc))[numpy.arange(-1*((self.data_sc+self.pilot_sc)//(self.pilot_sc*2)),((self.data_sc+self.pilot_sc)/2),((self.data_sc+self.pilot_sc)/self.pilot_sc))>0].astype(int)+1+(self.null//2))
        self.epy_block_0.null_subcarrier = self.null

    def get_data_sc(self):
        return self.data_sc

    def set_data_sc(self, data_sc):
        self.data_sc = data_sc
        self.set_Data(numpy.array(numpy.random.randint(self.M,size=(self.data_sc//2)*self.spf)))
        self.set_guard(self.fft_len-self.null-self.data_sc-self.pilot_sc)
        self.set_pdsc(numpy.delete((numpy.arange((self.data_sc+self.pilot_sc)//2)+1+(self.null//2)),((numpy.arange((self.data_sc+self.pilot_sc)//2)+1+(self.null//2))[:, None] == self.ppsc).argmax(axis=0))
        )
        self.set_ppsc(numpy.arange(-1*((self.data_sc+self.pilot_sc)//(self.pilot_sc*2)),((self.data_sc+self.pilot_sc)/2),((self.data_sc+self.pilot_sc)/self.pilot_sc))[numpy.arange(-1*((self.data_sc+self.pilot_sc)//(self.pilot_sc*2)),((self.data_sc+self.pilot_sc)/2),((self.data_sc+self.pilot_sc)/self.pilot_sc))>0].astype(int)+1+(self.null//2))
        self.blocks_stream_to_tagged_stream_0_0_0_0_0_0.set_packet_len(self.data_sc)
        self.blocks_stream_to_tagged_stream_0_0_0_0_0_0.set_packet_len_pmt(self.data_sc)
        self.epy_block_0.data_subcarrier = self.data_sc

    def get_ppsc(self):
        return self.ppsc

    def set_ppsc(self, ppsc):
        self.ppsc = ppsc
        self.set_pdsc(numpy.delete((numpy.arange((self.data_sc+self.pilot_sc)//2)+1+(self.null//2)),((numpy.arange((self.data_sc+self.pilot_sc)//2)+1+(self.null//2))[:, None] == self.ppsc).argmax(axis=0))
        )
        self.set_psc(numpy.sort(list(self.ppsc*-1) + list(self.ppsc)))

    def get_pck_len(self):
        return self.pck_len

    def set_pck_len(self, pck_len):
        self.pck_len = pck_len
        self.set_spf((self.pck_len-510)//self.fft_len)
        self.blocks_keep_m_in_n_1.set_n(self.pck_len)
        self.epy_block_1.frame_length = self.pck_len

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len
        self.set_guard(self.fft_len-self.null-self.data_sc-self.pilot_sc)
        self.set_spf((self.pck_len-510)//self.fft_len)
        self.blocks_keep_m_in_n_1.set_m(self.fft_len*self.spf)
        self.blocks_stream_to_tagged_stream_1.set_packet_len(self.fft_len*self.spf)
        self.blocks_stream_to_tagged_stream_1.set_packet_len_pmt(self.fft_len*self.spf)
        self.epy_block_0.fft_size = self.fft_len

    def get_spf(self):
        return self.spf

    def set_spf(self, spf):
        self.spf = spf
        self.set_Data(numpy.array(numpy.random.randint(self.M,size=(self.data_sc//2)*self.spf)))
        self.blocks_keep_m_in_n_1.set_m(self.fft_len*self.spf)
        self.blocks_stream_to_tagged_stream_1.set_packet_len(self.fft_len*self.spf)
        self.blocks_stream_to_tagged_stream_1.set_packet_len_pmt(self.fft_len*self.spf)
        self.epy_block_0.spf = self.spf

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols
        self.set_ps(list(numpy.flip(self.pilot_symbols)) + list(self.pilot_symbols))
        self.epy_block_0.pilot_symbols = self.pilot_symbols

    def get_pdsc(self):
        return self.pdsc

    def set_pdsc(self, pdsc):
        self.pdsc = pdsc
        self.set_dsc(numpy.sort(list(self.pdsc*-1) + list(self.pdsc)))

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Data(numpy.array(numpy.random.randint(self.M,size=(self.data_sc//2)*self.spf)))
        self.epy_block_0.M = self.M
        self.epy_block_2.M = self.M
        self.epy_block_4.M = self.M

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_psc(self):
        return self.psc

    def set_psc(self, psc):
        self.psc = psc

    def get_ps(self):
        return self.ps

    def set_ps(self, ps):
        self.ps = ps

    def get_guard(self):
        return self.guard

    def set_guard(self, guard):
        self.guard = guard
        self.epy_block_0.guard_subcarrier = self.guard

    def get_dsc(self):
        return self.dsc

    def set_dsc(self, dsc):
        self.dsc = dsc

    def get_corr_thresh(self):
        return self.corr_thresh

    def set_corr_thresh(self, corr_thresh):
        self.corr_thresh = corr_thresh
        self.digital_corr_est_cc_0.set_threshold(self.corr_thresh)

    def get_TX_GAIN(self):
        return self.TX_GAIN

    def set_TX_GAIN(self, TX_GAIN):
        self.TX_GAIN = TX_GAIN
        self.blocks_multiply_const_vxx_0.set_k(1/self.TX_GAIN)

    def get_P(self):
        return self.P

    def set_P(self, P):
        self.P = P
        self._P_callback(self.P)
        self.epy_block_3.display_BER = self.P

    def get_Data(self):
        return self.Data

    def set_Data(self, Data):
        self.Data = Data
        self.epy_block_0.data = self.Data





def main(top_block_cls=OFDM_1, options=None):

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
