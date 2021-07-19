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


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block

    def __init__(self, M=4):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='QAM Demodulator',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.int16]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.flg = 0
        self.M=M

        
    def modulat(self, MO):
        if MO == 2:
            cons = (np.array([-1+0*1j,1+0*1j]))
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
        if self.flg == 0:
            self.dp = self.modulat(self.M)
            self.flg = 1
        
        tdat = np.transpose(np.tile(input_items[0],(len(self.dp),1)))
        tcons = np.tile(self.dp,(len(input_items[0]),1))

        ll = np.subtract(tdat,tcons)
        min_ind = np.argmin(np.sqrt(np.real(ll)**2 + np.imag(ll)**2),axis=1)
        output_items[0][:] = min_ind.astype('int')
        

        return len(output_items[0])
