
notes = ['A ','A#','B ','C ','C#','D ','D#','E ','F ','F#','G ','G#']

a_min_pen = ['A ', 'D ', 'G ', 'C ', 'E ']
b_min_pen = ['B ', 'E ', 'A ', 'D ', 'F#']
c_min_pen = ['C ', 'F ', 'A#', 'D#', 'G ']
d_min_pen = ['D ', 'G ', 'C ', 'F ', 'A ']
e_min_pen = ['E ', 'A ', 'D ', 'G ', 'B ']
f_min_pen = ['F ', 'A#', 'D#', 'G#', 'C ']
g_min_pen = ['G ', 'C ', 'F ', 'A#', 'D ']

c_phrygi = ['C ', 'C#', 'E ', 'F ', 'G ', 'G#', 'A#', 'C ']
g_min_blues = ['G ', 'C ', 'F ', 'A#', 'D ', 'C#']

open_strings = ['E ','A ','D ','G ','B ','E ']
num_of_frets = 12

def print_fret_notes(fret_notes,scale=None):
    """
    """

    if scale == 'A_minor_pen':
        for string_num in range(0,len(fret_notes)):
            if fret_notes[string_num] not in a_min_pen:
                fret_notes[string_num] = '  '

    if scale == 'B_minor_pen':
        for string_num in range(0,len(fret_notes)):
            if fret_notes[string_num] not in b_min_pen:
                fret_notes[string_num] = '  '

    if scale == 'C_minor_pen':
        for string_num in range(0,len(fret_notes)):
            if fret_notes[string_num] not in c_min_pen:
                fret_notes[string_num] = '  '

    if scale == 'D_minor_pen':
        for string_num in range(0,len(fret_notes)):
            if fret_notes[string_num] not in d_min_pen:
                fret_notes[string_num] = '  '

    if scale == 'E_minor_pen':
        for string_num in range(0,len(fret_notes)):
            if fret_notes[string_num] not in e_min_pen:
                fret_notes[string_num] = '  '

    if scale == 'F_minor_pen':
        for string_num in range(0,len(fret_notes)):
            if fret_notes[string_num] not in f_min_pen:
                fret_notes[string_num] = '  '

    if scale == 'G_minor_pen':
        for string_num in range(0,len(fret_notes)):
            if fret_notes[string_num] not in g_min_pen:
                fret_notes[string_num] = '  '

    if scale == 'G_minor_blues':
        for string_num in range(0,len(fret_notes)):
            if fret_notes[string_num] not in g_min_blues:
                fret_notes[string_num] = '  '

    if scale == 'C_Phrygian':
        for string_num in range(0,len(fret_notes)):
            if fret_notes[string_num] not in c_phrygi:
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

map_neck(scale='G_minor_blues')