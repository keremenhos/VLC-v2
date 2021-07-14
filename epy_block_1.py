import time
import random
import numpy as np

from gnuradio import gr
from gnuradio import gr_unittest
from gnuradio import digital
from gnuradio import blocks
from gnuradio import grc
import pmt
import inspect

class blk(gr.basic_block):
    def __init__(self, frame_length=1):
        
        gr.basic_block.__init__(
            self,
            name="Preamble Demux",
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.a = 0
        self.aa = 0
        self.buf = []
        self.off = 0
        self.det = 0
        self.flg2 = 0
        self.b = 0
        self.frame_length = frame_length
        
    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = 4096
            
    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        
        if self.det == 0:
            tags = self.get_tags_in_window(0, 0, len(in0))
            for tag in tags:
                offset = tag.offset
                key = pmt.to_python(tag.key) # convert from PMT to python string
                if key == 'corr_est':
                    self.off = offset
                    self.det = 1
                    self.flg2 = 0
                    self.buf.extend(in0[(self.off-self.aa)+2:])
                    break
            if self.det == 0:
                self.b = 0
                    
        if len(self.buf)<self.frame_length and self.det == 1 and self.flg2 == 1:
            self.buf.extend(in0)
        
        if len(self.buf)>=self.frame_length and self.det == 1 and len(out)>=self.frame_length:
            out[:self.frame_length] = self.buf[:self.frame_length]
            if len(self.buf) == self.frame_length:
                self.buf = []
                self.det = 0
                self.b = 1
            else:
                tags = self.get_tags_in_window(0, 0, len(in0))
                for tag in tags:
                    self.offset2 = tag.offset
                    key = pmt.to_python(tag.key) # convert from PMT to python string
                    if key == 'corr_est':
                        if self.offset2 == self.off:
                            self.buf = []
                            self.det = 0
                            self.b = 1
                            break
                        else:
                            self.off = self.offset2
                            self.det = 1
                            self.flg2 = 0
                            self.buf=[]
                            self.buf.extend(in0[(self.off-self.aa)+2:])
                            self.b = 1
                            break

        self.flg2 = 1
        self.aa = self.aa + len(in0)
        
        self.consume(0, len(in0)) #consume port 0 input
        
        if self.b == 0:
            return 0
        else:
            return self.frame_length
