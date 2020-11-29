from colours import *

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

    #string colouring
    for string_num in range(0,len(fret_notes)):

        if string_num == 0:
            fret_notes[string_num] = red_back_k+fret_notes[string_num]+white
        if string_num == 1:
            fret_notes[string_num] = yellow_back_k+fret_notes[string_num]+white        
        if string_num == 2:
            fret_notes[string_num] = green_back_k+fret_notes[string_num]+white        
        if string_num == 3:
            fret_notes[string_num] = blue_back_k+fret_notes[string_num]+white        
        if string_num == 4:
            fret_notes[string_num] = purp_back_k+fret_notes[string_num]+white
        if string_num == 5:
            fret_notes[string_num] = turq_back_k+fret_notes[string_num]+white

    string1,string2,string3,string4,string5,string6 = fret_notes

    print('    |{} {} {} {} {} {}|'.format(string1,string2,string3,string4,string5,string6))

def print_guitar_head():
    """
    """

    a = red_back_k+'  '+white
    b = yellow_back_k+'  '+white        
    c = green_back_k+'  '+white        
    d = blue_back_k+'  '+white        
    e = purp_back_k+'  '+white
    f = turq_back_k+'  '+white

    ao = red_back+'O '+white
    bo = yellow_back+'O '+white        
    co = green_back+'O '+white        
    do = blue_back+'O '+white        
    eo = purp_back+'O '+white
    fo = turq_back+'O '+white

    ao2 = red_back+' O'+white
    bo2 = yellow_back+' O'+white        
    co2 = green_back+' O'+white        
    do2 = blue_back+' O'+white        
    eo2 = purp_back+' O'+white
    fo2 = turq_back+' O'+white

    t = white_back_k+' '+white

    tag = red+'Shellywell123'+white

    head= """
      _______________    
     /               \\ 
    /  /~~~~~~~~~~~\\  \\
   /  ({})  \\
  |    \\~~~~~~~~~~~/    |
{}=|=={}             {}==|={}
  |  {}             {}  |
  |   {}           {}   |
{}=|=={} {}       {} {}==|={}
  |  {}   {}   {}   {}  |
  |    {}  {} {}  {}    |
{}=|=={} {} {} {} {} {}==|={}
  |  {} {} {} {} {} {}  |
   \\ {}_{}_{}_{}_{}_{} / """.format(tag,t,co,do2,t,c,d,c,d,t,bo,c,d,eo2,t,b,c,d,e,b,c,d,e,t,ao,b,c,d,e,fo2,t,a,b,c,d,e,f,a,b,c,d,e,f,a,b,c,d,e,f)
    print(head)

def print_guitar_body():
    """
    """

    body="""
-------------------------------------------------------
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|                                                     |
|_____________________________________________________|
"""
    print(body)

def map_neck(scale=None,num_of_frets=12,tuning=['E ','A ','D ','G ','B ','E ']):
    """
    """
    print('Configuration:\n- tuning       = {}\n- num_of_frets = {}\n- scale        = {}'.format(tuning,num_of_frets,scale))
    print_guitar_head()
    neck_width = 17
    #print('   ',white_back_k,'#'*neck_width,white)
    for fret_num in range(0,num_of_frets+1):

        fret_notes = []
        
        for string in tuning:
            open_index = notes.index(string)
          #  note_index = open_index+fret_num
            note_index = open_index + (fret_num % len(notes))
            if note_index >= len(notes):
                note_index = note_index - len(notes)

            fret_notes.append(notes[note_index])

        print_fret_notes(fret_notes,scale=scale)
        #print(fret_num,'-'*neck_width)

        colored_fret = ' -{}--{}-{}--{}-{}--{}-{}--{}-{}--{}-{}--{}-'.format(red_back,white,yellow_back,white,green_back,white,blue_back,white,purp_back,white,turq_back,white)
      
        if fret_num==0:
            colored_fret=' |'+white_back_k+'#'*neck_width+white+'|'
        if fret_num<=9:
            fret_num = ' '+str(fret_num)
        print(fret_num,colored_fret)
 #   print_guitar_body()

map_neck(scale='A_minor_pen')