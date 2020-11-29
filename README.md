# Guitar_Chords
ASCII guitar chord tab printer from linux terminal. Written in Python 3 due to a collaboration with dustpancake. Maybe written in Julia soon.

## usage

```bash
python3 query.py
#######################
input a chord.
C

-------------
-------------
 | | | | | |
 | | | | x |
-------------
 | | | | | |
 | | x | | | 
-------------
 | | | | | | 
 | x | | | | 
-------------

```


## map all notes
```py
map_neck()
```

```
  ####################
    E  A  D  G  B  E
0 --------------------
    F  A# D# G# C  F
1 --------------------
    F# B  E  A  C# F#
2 --------------------
    G  C  F  A# D  G
3 --------------------
    G# C# F# B  D# G#
4 --------------------
    A  D  G  C  E  A
5 --------------------
    A# D# G# C# F  A#
6 --------------------
    B  E  A  D  F# B
7 --------------------
    C  F  A# D# G  C
8 --------------------
    C# F# B  E  G# C#
9 --------------------
    D  G  C  F  A  D
10 --------------------
    D# G# C# F# A# D#
11 --------------------
    E  A  D  G  B  E
12 --------------------
```
## Minor Pentatonic Scales
```py
map_neck(scale='A_minor_pen')
```
[](https://github.com/Shellywell123/Guitar_Chords/blob/main/screenshot.png)
## Minor Blues Scales
```py
map_neck(scale='G_minor_blues')
```

```bash
  ####################
          D  G
0 --------------------
    F  A#       C  F
1 --------------------
                C#
2 --------------------
    G  C  F  A# D  G
3 --------------------
       C#
4 --------------------
       D  G  C
5 --------------------
    A#       C# F  A#
6 --------------------
             D
7 --------------------
    C  F  A#    G  C
8 --------------------
    C#             C#
9 --------------------
    D  G  C  F     D
10 --------------------
          C#    A#
11 --------------------
          D  G
12 --------------------
```

## Phrygian Scales
```py
map_neck(scale='C_Phrygian')
```

```bash
  ####################
    E        G     E
0 --------------------
    F  A#    G# C  F
1 --------------------
          E     C#
2 --------------------
    G  C  F  A#    G
3 --------------------
    G# C#          G#
4 --------------------
          G  C  E
5 --------------------
    A#    G# C# F  A#
6 --------------------
       E
7 --------------------
    C  F  A#    G  C
8 --------------------
    C#       E  G# C#
9 --------------------
       G  C  F
10 --------------------
       G# C#    A#
11 --------------------
    E        G     E
12 --------------------
```