
from major_chords import *
from minor_chords import *

def ask(maj_chords,min_chords):
    chord = raw_input('#######################\ninput a chord.\n')

    if chord == 'exit':
        return 0    

    if chord in maj_chords:
        print eval(chord)

    if chord in min_chords:
        print eval(chord)

    if (chord not in maj_chords) and (chord not in min_chords):
        print '"'+chord+'" not in database'

    ask(maj_chords,min_chords)

ask(maj_chords,min_chords)