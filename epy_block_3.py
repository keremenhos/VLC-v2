import numpy as np
import math
import cmath
from gnuradio import gr

import time
import random
from gnuradio import gr_unittest
from gnuradio import digital
from gnuradio import blocks
from gnuradio import grc
import pmt
import inspect

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block

    def __init__(self, data=[], M=4, ttt=1):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='CAP Equalizer',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        self.aa = 0
        self.off=0
        self.ttt = ttt
        self.data = data
        self.M = M
        self.phOff = 0
        self.bin_d2 = []
        self.c = 0
        self.zz = []
        self.zy = 0
        self.a = []
        self.phOffT = 0
        self.phOffM = 0
        self.cc = 0
        self.ccc = 0
        self.flg = 0
        self.xr = []
        self.xi = []
        self.bin_d2=np.zeros(len(self.data), dtype=complex)
        
    def modulat(self, MO):
        if MO == 2:
            cons = (np.array([1+0*1j,-1+0*1j]))
        else:
            n = np.arange(0,MO)
            a = np.asarray([x^(x>>1) for x in n])
            D = np.sqrt(MO).astype(int)
            a = np.reshape(a,(D,D))
            a[1::2, :] = a[1::2, ::-1]
            nGray=np.reshape(a,(MO))
            x1 = nGray//D
            y = nGray%D
            Ay=2*y+1-D
            Ax=2*x1+1-D
            cons = Ax+1j*Ay
            cons = cons/np.max(np.absolute((np.real(cons))))
        return cons
        
    def work(self, input_items, output_items):

        in0 = input_items[0]
        ws = 1000
        
        if self.cc >= ws:
#            self.xr[self.ccc] = np.sqrt(np.nanmean(np.real(in0)**2))
#            self.xi[self.ccc] = np.sqrt(np.nanmean(np.imag(in0)**2))
            self.xr[self.ccc] = np.amax(np.absolute(np.real(in0)))
            self.xi[self.ccc] = np.amax(np.absolute(np.imag(in0)))
            self.ccc += 1
            if self.ccc == ws:
                self.ccc = 0
        else:
#            self.xr.append(np.sqrt(np.nanmean(np.real(in0)**2)))
#            self.xi.append(np.sqrt(np.nanmean(np.imag(in0)**2)))
            self.xr.append(np.amax(np.absolute(np.real(in0))))
            self.xi.append(np.amax(np.absolute(np.imag(in0))))
            self.cc += 1

        self.rmsR = np.nanmean(self.xr)
        self.rmsI = np.nanmean(self.xi)
        
        if self.rmsR != 0 and self.rmsI != 0:
            eq = np.array((self.ttt/np.sqrt(1))*np.real(in0)/self.rmsR)+np.array((self.ttt/np.sqrt(1))*np.imag(in0)/self.rmsI)*1j
        else:
            print('ANAN')
            eq = in0

        if self.flg == 0:
            self.flg = 1
            self.cons = self.modulat(self.M)
        
        for yy in range(len(self.data)):
            self.bin_d2[yy] = self.cons[self.data[yy]]
            
        tags = self.get_tags_in_window(0, 0, len(in0))
        for tag in tags:
            key = pmt.to_python(tag.key) # convert from PMT to python string
            if key == 'pck':
                self.off = tag.offset
                if (self.off-self.aa) + len(self.bin_d2)+1 >= len(in0):
                    a = (in0[(self.off-self.aa)+1:])
                    if len(a) > 0:
                        self.phOff = (np.nanmean(np.angle(self.bin_d2[:(len(in0)-(self.off-self.aa)-1)]*np.conj(a))))
                else:
                    a = (in0[(self.off-self.aa)+1:(self.off-self.aa) + len(self.bin_d2)+1])
                    self.phOff = (np.nanmean(np.angle(self.bin_d2*np.conj(a))))
                    
        output_items[0][:] = cmath.exp(np.real(self.phOff)*1j)*eq
        
        self.aa = self.aa + len(input_items[0])

        return len(output_items[0])

