# Guitar_Chords
ASCII guitar chord tab printer from linux terminal. Written in Python 3 due to a collaboration with dustpancake. Maybe written in Julia soon.

## Example
```py
from map_neck_notes import map_neck
map_neck(scale='A_minor_pen')
```

![](https://github.com/Shellywell123/Guitar_Chords/blob/master/screenshot.png)

## Features
plot all notes:
```py
map_neck()
```

set tuning (requires spaces):
```py
map_neck(tuning=['E ','A ','D ','G ','B ','E '])
```

select num of frets:
```py
map_neck(num_of_frets=12)
```

## Chord Query

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


