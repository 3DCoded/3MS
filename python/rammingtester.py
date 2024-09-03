iname = '~/Downloads/ramming.gcode'
oname = '~/Downloads/ramming2.gcode'

with open(iname) as ifile:
    for line in ifile.readlines():
        w