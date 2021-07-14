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


def mod(dat, M):
    n = np.arange(0,M)
    a = np.asarray([x^(x>>1) for x in n])
    D = np.sqrt(M).astype(int)
    a = np.reshape(a,(D,D))
    a[1::2, :] = a[1::2, ::-1]
    nGray=np.reshape(a,(M))
    x = nGray//D
    y = nGray%D
    Ay=2*y+1-D
    Ax=2*x+1-D
    cons = Ax+1j*Ay
    cons = cons/np.max(np.absolute((np.real(cons))))
    for yy in range(len(xx)):
        xx[yy] = cons[dat[yy]]
    return xx
