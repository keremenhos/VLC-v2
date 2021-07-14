#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: demux2
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
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation

from gnuradio import qtgui

class demux2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "demux2")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("demux2")
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

        self.settings = Qt.QSettings("GNU Radio", "demux2")

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
        self.variable_header_format_default_0 = variable_header_format_default_0 = digital.header_format_default('101010',0, 1)
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_char,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.digital_packet_headergenerator_bb_0 = digital.packet_headergenerator_bb(variable_header_format_default_0, "packet_len")
        self.blocks_vector_source_x_0 = blocks.vector_source_b([0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0], True, 1, [])


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_vector_source_x_0, 0), (self.digital_packet_headergenerator_bb_0, 0))
        self.connect((self.digital_packet_headergenerator_bb_0, 0), (self.qtgui_number_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "demux2")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_header_format_default_0(self):
        return self.variable_header_format_default_0

    def set_variable_header_format_default_0(self, variable_header_format_default_0):
        self.variable_header_format_default_0 = variable_header_format_default_0
        self.digital_packet_headergenerator_bb_0.set_header_formatter(self.variable_header_format_default_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate





def main(top_block_cls=demux2, options=None):

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
