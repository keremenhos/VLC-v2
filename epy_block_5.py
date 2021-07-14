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


class blk(gr.sync_block):

    def __init__(self, data=[], M=4, display_BER = 0, num_bits = 1000000):
        gr.sync_block.__init__(
            self,
            name='BER',
            in_sig=[np.int16],
            out_sig=[]
        )
        self.bin_data = data
        self.e = 0
        self.p = 0
        self.buf = []
        self.flg = 0
        self.k = np.sqrt(M)
        self.ber = 1
        self.display_BER = display_BER
        self.num_bits = num_bits
        self.aa = 0

    def work(self, input_items, output_items):
        
        if self.flg == 1:
            self.flg = 0
            self.buf.extend(input_items[0][:len(self.bin_data)-len(self.buf)+10])
            self.p += 1
            for j in range(len(self.bin_data)):
                if j<len(self.buf):
                    self.e += sum(np.array(list(bin(int(self.buf[j])^self.bin_data[j])[2:])).astype('int'))

        if self.flg == 0:
            tags = self.get_tags_in_window(0, 0, len(input_items[0]))
            for tag in tags:
                offset = tag.offset
                key = pmt.to_python(tag.key) # convert from PMT to python string
                value = pmt.to_python(tag.value)
                if key == 'pck':
                    self.off = offset
                    if (self.off-self.nitems_read(0)+1) + len(self.bin_data) < len(input_items[0]):
                        self.p += 1
                        for i in range(len(self.bin_data)):
                            self.e += sum(np.array(list(bin(int(input_items[0][(self.off-self.nitems_read(0)+1)+i])^self.bin_data[i])[2:])).astype('int'))
                    else:
                        self.buf=[]
                        self.buf.extend(input_items[0][(self.off-self.nitems_read(0)+1):])
                        self.flg = 1
                        
        if self.p*(self.k*len(self.bin_data)) > self.num_bits:
            self.ber = self.e/(self.p*(self.k*len(self.bin_data)))
            self.e = 0
            self.p = 0
            if self.display_BER == 1:
                print(self.ber)

#        output_items[0][:] = self.ber*np.ones(len(output_items[0]))
        return len(input_items[0])
