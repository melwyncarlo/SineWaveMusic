import numpy as np
import wavio
import wave
import time
import os


amplitude = 1
samplerate = 22050
sampleduration = 1

notenameslist   = ["c4", "d", "e", "f", "g", "a", "b", "c5"]
notenumberslist = [40, 42, 44, 45, 47, 49, 51, 52]


def notefrequency(notenumber):
    return (np.power(2, (notenumber-49)/12) * 440)


def generateaudio(f, filename):
    # f is the ordinary frequency
    # Set the angular frequency
    omega = 2 * np.pi * f
    # Set the horizonal axis, t (or x)
    t = np.linspace(0, sampleduration, sampleduration * samplerate, \
    endpoint=False)
    # Set the decay filter
    decayfilter = np.power(np.exp(1), -25 * np.power(t - 0.5, 2))
    # Set the sine wave audio function y=f(x)
    y = amplitude * decayfilter * np.sin(omega * t)
    # Create the *.wav audio file
    wavio.write(filename + ".wav", y, samplerate, sampwidth=3)


def mergeaudiofiles():
    data = []
    for notefile in notenameslist:
        w = wave.open(notefile + ".wav", 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
    scalefile = wave.open("scale.wav", 'wb')
    scalefile.setparams(data[0][0])
    for i in range(len(notenameslist)):
        scalefile.writeframes(data[i][1])
    scalefile.close()


def deleteaudiofiles():
    for notefile in notenameslist:
        os.remove(notefile + ".wav")


def main():
    for i in range(len(notenumberslist)):
        generateaudio( notefrequency(notenumberslist[i]), notenameslist[i] )
    while True:
        if os.path.exists(notenameslist[-1] + ".wav"):
            break
        else:
            time.sleep(0.1)
    mergeaudiofiles()
    deleteaudiofiles()


main()


