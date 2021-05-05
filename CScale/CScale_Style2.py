# Copyright 2021 Melwyn Francis Carlo

import numpy as np
import wavio


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
        y = y + ( amplitude * np.sin(2 * np.pi * \
        notefrequency(notenumberslist[i]) * t) * \
        np.exp( -15 * (( (np.sign(t-i) * (abs(t-i) ** 0.2)) - 0.5) ** 2) ) )
    # Create the *.wav audio file
    wavio.write("CScale_Style2.wav", y, samplerate, sampwidth=3)


generateaudio()


