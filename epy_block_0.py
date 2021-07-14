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

    def __init__(self, M=4):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='QAM Modulator',   # will show up in GRC
            in_sig=[np.int32],
            out_sig=[np.complex64]
        )
        self.M = M
        self.tM = self.M
        self.c = 0
        
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
        
        self.cons = self.modulat(self.M)
                
        for xx in range(len(input_items[0])):
            output_items[0][xx] = self.cons[input_items[0][xx]]

        return len(output_items[0])
