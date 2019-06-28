import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

y = np.random.randn(100)
y2 = np.copy(y)

yft = fft(y)
y = ifft(yft)
y = np.real(y)
print np.sum(y-y2)





