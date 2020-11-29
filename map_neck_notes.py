
notes = ['A ','A#','B ','C ','C#','D ','D#','E ','F ','F#','G ','G#']

# scales

a_min_pen = ['A ', 'D ', 'G ', 'C ', 'E ']
b_min_pen = ['B ', 'E ', 'A ', 'D ', 'F#']
c_min_pen = ['C ', 'F ', 'A#', 'D#', 'G ']
d_min_pen = ['D ', 'G ', 'C ', 'F ', 'A ']
e_min_pen = ['E ', 'A ', 'D ', 'G ', 'B ']
f_min_pen = ['F ', 'A#', 'D#', 'G#', 'C ']
g_min_pen = ['G ', 'C ', 'F ', 'A#', 'D ']

a_phrygi = []
b_phrygi = []
c_phrygi = ['C ', 'C#', 'E ', 'F ', 'G ', 'G#', 'A#']
d_phrygi = []
e_phrygi = []
f_phrygi = []
g_phrygi = []

a_min_blues = ['A ', 'D ', 'G ', 'C ', 'E ', 'D#']
b_min_blues = ['B ', 'E ', 'A ', 'D ', 'F#', 'F ']
c_min_blues = ['C ', 'F ', 'A#', 'D#', 'G ', 'F#']
d_min_blues = ['D ', 'G ', 'C ', 'F ', 'A ', 'G#']
e_min_blues = ['E ', 'A ', 'D ', 'G ', 'B ', 'A#']
f_min_blues = ['F ', 'A#', 'D#', 'G#', 'C ', 'B ']
g_min_blues = ['G ', 'C ', 'F ', 'A#', 'D ', 'C#']

#guitar setup

open_strings = ['E ','A ','D ','G ','B ','E ']
num_of_frets = 12

def print_fret_notes(fret_notes,scale=None):
    """
    """

    if scale != None:
        if scale == 'A_minor_pen':
            scale_notes = a_min_pen
        if scale == 'B_minor_pen':
            scale_notes = b_min_pen
        if scale == 'C_minor_pen':
            scale_notes = c_min_pen
        if scale == 'D_minor_pen':
            scale_notes = d_min_pen
        if scale == 'E_minor_pen':
            scale_notes = e_min_pen
        if scale == 'F_minor_pen':
            scale_notes = f_min_pen
        if scale == 'G_minor_pen':
            scale_notes = g_min_pen

        if scale == 'A_minor_blues':
            scale_notes = a_min_blues
        if scale == 'B_minor_blues':
            scale_notes = b_min_blues
        if scale == 'C_minor_blues':
            scale_notes = c_min_blues
        if scale == 'D_minor_blues':
            scale_notes = d_min_blues
        if scale == 'E_minor_blues':
            scale_notes = e_min_blues
        if scale == 'F_minor_blues':
            scale_notes = f_min_blues
        if scale == 'G_minor_blues':
            scale_notes = g_min_blues

        if scale == 'C_Phrygian':
            scale_notes = c_phrygi

        for string_num in range(0,len(fret_notes)):
            if fret_notes[string_num] not in scale_notes:
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

map_neck(scale='C_Phrygian')