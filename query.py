
from major_chords import *
from minor_chords import *

def ask(maj_chords,min_chords):
    chord = raw_input('#######################\ninput a chord.\n')
    

    if chord in maj_chords:
        print eval(chord)

    if chord in min_chords:
        print eval(chord)

    ask(maj_chords,min_chords)

ask(maj_chords,min_chords)