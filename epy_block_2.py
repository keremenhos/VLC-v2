"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import time
import random
import numpy as np

from gnuradio import gr
from gnuradio import gr_unittest
from gnuradio import digital
from gnuradio import blocks
from gnuradio import grc
from scipy import interpolate
import pmt
import inspect


class blk(gr.basic_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, M=4, data_subcarrier=1, pilot_subcarrier=1, null_subcarrier=1, guard_subcarrier = 1, fft_size = 64, pilot_symbols=[], symbols_per_frame=1):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.basic_block.__init__(
            self,
            name='OFDM Receiver',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.M = M
        self.data_sc = data_subcarrier
        self.pilot_sc = pilot_subcarrier
        self.null_sc = null_subcarrier
        self.guard_sc = guard_subcarrier
        self.ffts = fft_size
        self.pilot_sym = pilot_symbols
        self.aa = 0
        self.out_buf = []
        self.data_out_buf = []
        self.sym_n = 0
        self.spf = symbols_per_frame
        self.flg = 0
        self.flg2 = 0
#        self.n_sc = (self.data_sc+self.pilot_sc)/2
        self.n_grd = self.guard_sc//2

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = 4096
            
    def pilot_generator(self, psc, pd):
        pp = np.zeros(psc, dtype=complex)
        for i in range(psc):
            if pd[i] == 1:
                pp[i] = 1+0*1j
            else:
                pp[i] = -1+0*1j
        return pp

    def general_work(self, input_items, output_items):

        in0 = input_items[0][:]
        out = output_items[0][:]
        
        if self.flg2 == 0:
            self.ppos = np.arange(-1*((self.data_sc+self.pilot_sc)//(self.pilot_sc*2)),((self.data_sc+self.pilot_sc)/2),((self.data_sc+self.pilot_sc)/self.pilot_sc))
            self.ppos = self.ppos[self.ppos>0].astype(int)
            self.pilots = self.pilot_generator(self.pilot_sc//2, self.pilot_sym)
            self.tx_pilot = np.concatenate((np.flip(self.pilots),self.pilots),axis=None)
            
            self.alli = np.array(range(self.ffts))
            self.sc_ind = np.arange((self.n_grd+1),(self.ffts-self.n_grd))
            self.sc_ind = np.delete(self.sc_ind,(self.sc_ind[:, None] == (np.arange(-self.null_sc//2,self.null_sc//2)+(self.ffts/2)+1)).argmax(axis=0))
            self.sc_ind[:(np.where(self.sc_ind==((self.ffts/2)-(self.null_sc//2)-1))[0][0])+1]=np.flipud(self.sc_ind[:(np.where(self.sc_ind==((self.ffts/2)-(self.null_sc//2)-1))[0][0])+1])
            self.alli[:(np.where(self.alli==((self.ffts/2)-1))[0][0])+1]=np.flipud(self.alli[:(np.where(self.alli==((self.ffts/2)-1))[0][0])+1])
            self.p_ind = np.sort(np.concatenate((self.alli[self.ppos+(self.null_sc//2)],self.alli[((self.ffts//2)+(self.null_sc//2)+1+self.ppos)]),axis=None))
            self.s_sc_ind = np.sort(self.sc_ind)
            self.dsc_ind = np.delete(self.s_sc_ind,(self.s_sc_ind[:, None] == self.p_ind).argmax(axis=0))
            self.flg2 = 1
            ppp=np.where(self.sc_ind>=self.ffts//2)[0]
            self.dsc_iii = np.delete(ppp,(ppp[:,None]==(self.ppos+((self.data_sc+self.pilot_sc)//2))).argmax(axis=0))
        
        tags = self.get_tags_in_window(0, 0, len(in0))
        for tag in tags:
            offset = tag.offset
            key = pmt.to_python(tag.key) # convert from PMT to python string
            if key == 'sym':
                self.offset = offset
                self.xx = self.p_ind + self.offset - self.aa
                self.ch_est = np.true_divide(in0[self.xx.astype(int)],self.tx_pilot)
                
                self.ch_est_r = np.real(self.ch_est)
                self.ch_est_i = np.imag(self.ch_est)
                
                f_r = interpolate.splrep(self.p_ind,self.ch_est_r,s=0)
                f_i = interpolate.splrep(self.p_ind,self.ch_est_i,s=0)
                H_r = interpolate.splev((self.s_sc_ind),f_r,der=0)
                H_i = interpolate.splev((self.s_sc_ind),f_i,der=0)
                H = H_r + H_i*1j

                if sum(H_r) != 0:
                    self.indind = self.s_sc_ind + (self.offset-self.aa)
                    self.sym_out = np.multiply(np.multiply((np.multiply(np.conj(H),H)**(-1)),np.conj(H)),in0[self.indind])
                    self.data_out_buf.extend(self.sym_out[self.dsc_iii])
                    self.sym_n += 1
                    if self.flg == 0:
                        self.flg = 1
                        self.index1 = self.offset
                        self.cind = 0
                    self.add_item_tag(0, (self.index1 + self.cind*(self.data_sc//2)), pmt.intern("Sym#"), pmt.intern(str(self.sym_n)))
                    if self.sym_n == 1:
                        self.add_item_tag(0, (self.index1 + self.cind*(self.data_sc//2)), pmt.intern("pck_st"), pmt.intern(str(self.sym_n)))
                    self.cind += 1
                    if self.sym_n == self.spf:
                        self.sym_n = 0
                
        if len(self.data_out_buf)>=len(out):
            output_items[0][:] = self.data_out_buf[:len(out)]
            self.data_out_buf = self.data_out_buf[len(out):]
            self.aa = self.aa + len(in0)
            self.consume(0, len(in0))
            return len(out)

        self.aa = self.aa + len(in0)
        self.consume(0, len(in0))
        return 0
