import numpy as np
import wavio
import math


amplitude = 1
samplerate = 22050
sampleduration = 8

notenameslist   = ["c4", "d", "e", "f", "g", "a", "b", "c5"]
notenumberslist = [40, 42, 44, 45, 47, 49, 51, 52]


def notefrequency(notenumber):
    return (np.power(2, (notenumber-49)/12) * 440)


def generateaudio():
    y = 0
    # Set the horizonal axis, t (or x)
    t = np.linspace(0, sampleduration, sampleduration * samplerate, \
    endpoint=False)
    for i in range(len(notenumberslist)):
        # Set the sine wave audio function y=f(x)
        y = y + (amplitude * \
        (np.sin(1 * 2 * np.pi * notefrequency(notenumberslist[i]) * t) + \
        math.log10(9)*np.sin(2 * 2 * np.pi * notefrequency(notenumberslist[i]) * t) + \
        math.log10(8)*np.sin(3 * 2 * np.pi * notefrequency(notenumberslist[i]) * t) + \
        math.log10(7)*np.sin(4 * 2 * np.pi * notefrequency(notenumberslist[i]) * t) + \
        math.log10(6)*np.sin(5 * 2 * np.pi * notefrequency(notenumberslist[i]) * t) + \
        math.log10(5)*np.sin(6 * 2 * np.pi * notefrequency(notenumberslist[i]) * t) + \
        math.log10(4)*np.sin(7 * 2 * np.pi * notefrequency(notenumberslist[i]) * t) + \
        math.log10(3)*np.sin(8 * 2 * np.pi * notefrequency(notenumberslist[i]) * t) + \
        math.log10(2)*np.sin(9 * 2 * np.pi * notefrequency(notenumberslist[i]) * t) + \
        math.log10(1)*np.sin(10 * 2 * np.pi * notefrequency(notenumberslist[i]) * t)) * \
        np.exp(-25 * np.power(t - i - 0.5, 2)))
    # Create the *.wav audio file
    wavio.write("CScale_Harmonics.wav", y, samplerate, sampwidth=3)


generateaudio()


