import numpy as np
import wavio


amplitude = 1
samplerate = 22050

notenameslist   = ["c4", "d", "e", "f", "g", "a", "b", "c5"]
notenumberslist = [40, 42, 44, 45, 47, 49, 51, 52]


def notefrequency(notenumber):
    return (np.power(2, (notenumber-49)/12) * 440)


def generateaudio(notesarray):
    y = 0
    sampleduration = len(notesarray)
    # Set the horizonal axis, t (or x)
    t = np.linspace(0, sampleduration, sampleduration * samplerate, \
    endpoint=False)
    for i, notearrayelem in enumerate(notesarray):
        if notearrayelem != []:
            for noteelem in notearrayelem:
                # Set the sine wave audio function y=f(x)
                y = y + amplitude * np.sin(2 * np.pi * \
                notefrequency(notenumberslist[notenameslist.index(noteelem)]) \
                * t) * np.exp(-25 * np.power(t - i - 0.5, 2))
    # Create the *.wav audio file
    wavio.write("Chords.wav", y, samplerate, sampwidth=3)


chords_notes =  [
                    ["c4", "e", "g" ], 
                    ["d",  "f", "a" ], 
                    ["e",  "g", "b" ], 
                    ["f",  "a", "c5"], 
                    ["c4", "e", "g" ]
                ]
generateaudio(chords_notes)


