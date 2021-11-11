import math
import stdarray
import stdaudio
import stdio
import numpy as np

SPS = 44100
CONCERT_A = 440.0
while not stdio.isEmpty():
 pitch = stdio.readInt()
 duration = stdio.readFloat()
 hz = CONCERT_A * (2 ** (pitch / 12.0))
 n = int(SPS * duration)
 samples = 440
    samples = math.sin(2.0 * math.pi * i * hz / SPS)
    samples *= 8388607 / np.max(np.abs(samples))
    samples = samples.astype(np.int32)

 stdaudio.playSamples(samples)
stdaudio.wait()