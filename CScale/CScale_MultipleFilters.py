# Copyright 2021 Melwyn Francis Carlo

import numpy as np
import wavio


samplerate = 22050
sampleduration = 10

amplitude = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 5.0, 7.0]
notenameslist   = ["c4", "d", "e", "f", "g", "a", "b", "c5"]
notenumberslist = [40, 42, 44, 45, 47, 49, 51, 52]


def notefrequency(notenumber):
    return (np.power(2, (notenumber-49)/12) * 440)


def generateaudio():
    y = 0
    # Set the horizonal axis, t (or x)
    t = np.linspace(0, sampleduration, sampleduration * samplerate, \
    endpoint=False)
    # Set the 'C' constants for K=e^C
    cconstant = [ \
        np.exp( -1.0 * np.sign(2.1 * np.float_power(t, 2.1)) * \
            np.float_power(abs(2.1 * np.float_power(t, 2.1)), 2.2) ), \
        0.75 / ((t-1+0.75) + np.power(4 * (t-1-0.25), 100)), \
        0.5 / ((t-1.5+0.5) + np.power(2 * (t-1.5-0.5), 100)), \
        0.75 / ((t-2.5+0.75) + np.power(4 * (t-2.5-0.25), 100)), \
        0.5 / ((t-3+0.5) + np.power(2 * (t-3-0.5), 100)), \
        0.75 / ((t-4+0.75) + np.power(4 * (t-4-0.25), 100)), \
        0.75 / ((t-4.5+0.75) + np.power(4 * (t-4.5-0.25), 100)), \
        1.1 / (t-6+2 + np.power(t-6, 100)) \
        # ( (5.5 * 2) / (((2*t)-5.5) + np.power(t-5.5-1, 100)) ) - 1 \
    ]
    for i in range(len(notenumberslist)):
        # Set the sine wave audio function y=f(x)
        y = y + ( amplitude[i] * np.sin(2 * np.pi * \
        notefrequency(notenumberslist[i]) * t) * cconstant[i] )
    # Create the *.wav audio file
    wavio.write("CScale_MultipleFilters.wav", y, samplerate, sampwidth=3)


generateaudio()


