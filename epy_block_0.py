"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
import time
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, data=[], M=4, data_subcarrier=1, pilot_subcarrier=1, null_subcarrier=1, guard_subcarrier = 1, fft_size = 64, pilot_symbols=[], spf = 1):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='OFDM Frame Generator',   # will show up in GRC
            in_sig=[],
            out_sig=[np.complex64]
        )
        self.M = M
        self.c = 0
        self.data = data
        self.data_subcarrier = data_subcarrier
        self.pilot_subcarrier = pilot_subcarrier
        self.null_subcarrier = null_subcarrier
        self.guard_subcarrier = guard_subcarrier
        self.fft_size = fft_size
        self.l = (len(self.data)//((self.data_subcarrier)/2))-1
        self.d = ((self.data_subcarrier+self.pilot_subcarrier)//2)
        self.data_buf = np.zeros(len(self.data), dtype=complex)
        self.pilot_symbols = pilot_symbols
        self.out_buf = np.zeros(len(self.data)*2, dtype=complex)
        self.spf = spf
        self.flg = 0
        self.data2 = self.data
        
    def modulat(self, MO):
        if MO == 2:
            cons = np.array([-1+0*1j,1+0*1j])
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
        
        out = output_items[0]
        
        if self.flg == 0:
            self.flg = 1
            self.cons = self.modulat(self.M)
            if len(out)<len(self.data):
                self.flg = 0
                print('22222-0000')
                return 0
            for x in range(len(self.data)):
                self.data_buf[x] = self.cons[self.data[x]]
            for z in range(self.spf*(self.data_subcarrier//2)):
                self.out_buf[z*self.data_subcarrier:(z+1)*self.data_subcarrier] = list(np.conj(np.flip(self.data_buf[z*self.data_subcarrier//2:(z+1)*self.data_subcarrier//2]))) + list(self.data_buf[z*self.data_subcarrier//2:(z+1)*self.data_subcarrier//2])
#            print('1111')
#            print(len(out))
         
        if np.sum(self.data2-self.data) != 0:
            self.data2 = self.data
            if len(out)<len(self.data):
                print('22222')
                return 0
            self.data2 = self.data
            for x in range(len(self.data)):
                self.data_buf[x] = self.cons[self.data[x]]
            for z in range(self.spf*(self.data_subcarrier//2)):
                self.out_buf[z*self.data_subcarrier:(z+1)*self.data_subcarrier] = list(np.conj(np.flip(self.data_buf[z*self.data_subcarrier//2:(z+1)*self.data_subcarrier//2]))) + list(self.data_buf[z*self.data_subcarrier//2:(z+1)*self.data_subcarrier//2])
            print(self.data2-self.data)
                

        out[:(len(out)//len(self.out_buf))*len(self.out_buf)] = list(self.out_buf)*(len(out)//len(self.out_buf))
        return (len(out)//len(self.out_buf))*len(self.out_buf)
