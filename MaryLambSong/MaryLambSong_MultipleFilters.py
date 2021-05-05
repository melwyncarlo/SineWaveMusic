# Copyright 2021 Melwyn Francis Carlo

import matplotlib.pyplot as plt
import numpy as np
import wavio


samplerate = 22050
sampleduration = 17

notenameslist   = ["c4", "d", "e", "f", "g", "a", "b", "c5"]
notenumberslist = [40, 42, 44, 45, 47, 49, 51, 52]


def notefrequency(notenumber):
    return (np.power(2, (notenumber-49)/12) * 440)


def generateaudio():
    # Set the horizonal axis, t (or x)
    t = np.linspace(0, sampleduration, sampleduration * samplerate, endpoint=False)
    y = \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("e")]) * t) * \
        np.exp( -1.0 * np.sign(2.1 * np.float_power(t, 2.1)) * \
        np.float_power(abs(2.1 * np.float_power(t, 2.1)), 2.2) ) ) + \
    ( 2 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("d")]) * t) * \
        (0.75 / ((t-1+0.75) + np.power(4 * (t-1-0.25), 100))) ) + \
    ( 2 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("c4")]) * t) * \
        (0.75 / ((t-1.5+0.75) + np.power(4 * (t-1.5-0.25), 100))) ) + \
    ( 2 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("d")]) * t) * \
        (0.75 / ((t-2+0.75) + np.power(4 * (t-2-0.25), 100))) ) + \
    ( 2 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("e")]) * t) * \
        np.exp( -15 * (( (np.sign(2*(t-2.5)) * (abs(2*(t-2.5)) ** 0.2)) - 0.5) ** 2) ) ) + \
    ( 2 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("e")]) * t) * \
        np.exp( -15 * (( (np.sign(2*(t-3)) * (abs(2*(t-3)) ** 0.2)) - 0.5) ** 2) ) ) + \
    ( 2 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("e")]) * t) * \
        (1 / (1 + (100 * np.power(2 * (t-3.5-0.5), 20)))) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("d")]) * t) * \
        np.exp( -15 * (( (np.sign(2*(t-4.5)) * (abs(2*(t-4.5)) ** 0.2)) - 0.5) ** 2) ) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("d")]) * t) * \
        np.exp( -15 * (( (np.sign(2*(t-5)) * (abs(2*(t-5)) ** 0.2)) - 0.5) ** 2) ) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("d")]) * t) * \
        (1 / (1 + (100 * np.power(2 * (t-5.5-0.5), 20)))) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("e")]) * t) * \
        np.exp( -15 * (( (np.sign(2*(t-6.5)) * (abs(2*(t-6.5)) ** 0.2)) - 0.5) ** 2) ) ) + \
    ( 6 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("g")]) * t) * \
        np.exp( -15 * (( (np.sign(2*(t-7)) * (abs(2*(t-7)) ** 0.2)) - 0.5) ** 2) ) ) + \
    ( 6 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("g")]) * t) * \
        (1 / (1 + (100 * np.power(2 * (t-7.5-0.5), 20)))) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("e")]) * t) * \
        (0.75 / ((t-8.5+0.75) + np.power(4 * (t-8.5-0.25), 100))) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("d")]) * t) * \
        (0.75 / ((t-9+0.75) + np.power(4 * (t-9-0.25), 100))) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("c4")]) * t) * \
        (0.75 / ((t-9.5+0.75) + np.power(4 * (t-9.5-0.25), 100))) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("d")]) * t) * \
        (0.75 / ((t-10+0.75) + np.power(4 * (t-10-0.25), 100))) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("e")]) * t) * \
        np.exp( -15 * (( (np.sign(2*(t-10.5)) * (abs(2*(t-10.5)) ** 0.2)) - 0.5) ** 2) ) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("e")]) * t) * \
        np.exp( -15 * (( (np.sign(2*(t-11)) * (abs(2*(t-11)) ** 0.2)) - 0.5) ** 2) ) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("e")]) * t) * \
        np.exp( -15 * (( (np.sign(2*(t-11.5)) * (abs(2*(t-11.5)) ** 0.2)) - 0.5) ** 2) ) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("c4")]) * t) * \
        (0.75 / ((t-12+0.75) + np.power(4 * (t-12-0.25), 100))) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("d")]) * t) * \
        np.exp( -15 * (( (np.sign(2*(t-12.5)) * (abs(2*(t-12.5)) ** 0.2)) - 0.5) ** 2) ) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("d")]) * t) * \
        np.exp( -15 * (( (np.sign(2*(t-13)) * (abs(2*(t-13)) ** 0.2)) - 0.5) ** 2) ) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("e")]) * t) * \
        (0.75 / ((t-13.5+0.75) + np.power(4 * (t-13.5-0.25), 100))) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("d")]) * t) * \
        (0.75 / ((t-14+0.75) + np.power(4 * (t-14-0.25), 100))) ) + \
    ( 3 * np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("c4")]) * t) * \
        (1 / (1 + (100 * np.power(2 * (t-14.5-0.5), 20)))) ) + \
    ( 3 * ( np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("e")]) * t) + \
            np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("g")]) * t) + \
            np.sin(2 * np.pi * notefrequency(notenumberslist[notenameslist.index("c5")]) * t)) * \
        np.exp( -15 * (( (np.sign(2*(t-15.5)) * (abs(2*(t-15.5)) ** 0.2)) - 0.5) ** 2) ) )
    plt.title("The 'Mary had a little lamb' song")
    plt.xlabel("Time, t")
    plt.ylabel("Amplitude, A")
    plt.plot(t, y, 'k')
    plt.grid()
    plt.show()
    # Create the *.wav audio file
    wavio.write("MaryLambSong_MultipleFilters.wav", y, samplerate, sampwidth=3)


generateaudio()


