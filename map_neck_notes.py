
notes = ['A ','A#','B ','C ','C#','D ','D#','E ','F ','F#','G ','G#']

a_min_pen = ['A ', 'D ', 'G ', 'C ', 'E ']

open_strings = ['E ','A ','D ','G ','B ','E ']
num_of_frets = 12


def print_fret_notes(fret_notes,scale=None):
    """
    """

    if scale == 'A_minor_pen':
        for string_num in range(0,len(fret_notes)):
            if fret_notes[string_num] not in a_min_pen:
                fret_notes[string_num] = '  '

    string1,string2,string3,string4,string5,string6 = fret_notes

    print('    {} {} {} {} {} {}'.format(string1,string2,string3,string4,string5,string6))


def map_neck(scale=None):
    """
    """
    neck_width = 20
    print(' ','#'*neck_width)
    for fret_num in range(0,num_of_frets+1):

        fret_notes = []
        
        for string in open_strings:
            open_index = notes.index(string)
          #  note_index = open_index+fret_num
            note_index = open_index + (fret_num % len(notes))
            if note_index >= len(notes):
                note_index = note_index - len(notes)

            fret_notes.append(notes[note_index])


        print_fret_notes(fret_notes,scale=scale)
        print(fret_num,'-'*neck_width)

map_neck(scale='A_minor_pen')