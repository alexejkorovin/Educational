import stdarray
import math
import stdaudio
import numpy as np
from scipy.io.wavfile import write

def tone(hz, duration, sps=44100):
 n = int(sps * duration)
 a = stdarray.create1D(n+1, 0.0)
 for i in range(n+1):
   a[i] = math.sin(2.0 * math.pi * i * hz / sps)
 return a

n = int(440 * 3)
a = stdarray.create1D(n+1, 0.0)
a = tone(440, 3)
write(123, 44100, a)
