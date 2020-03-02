from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    lines = f.readlines()
    x = 0
    while x < len(lines):
        lines[x] = lines[x][:-1]
        x += 1
    f.close()
    i = 0
    while i < len(lines):
        if lines[i] == 'line':
            c = lines[i+1].split(' ')
            add_edge(points, int(c[0]), int(c[1]),int(c[2]), int(c[3]), int(c[4]), int(c[5]))
            i += 1
        if lines[i] == 'ident':
            ident(transform)
        if lines[i] == 'scale':
            c = lines[i+1].split(' ')
            matrix_mult(make_scale(int(c[0]), int(c[1]), int(c[2])), transform)
            i += 1
        if lines[i] == 'move':
            c = lines[i+1].split(' ')
            matrix_mult(make_translate(int(c[0]), int(c[1]), int(c[2])), transform)
            i += 1
        if lines[i] == 'rotate':
            c = lines[i+1].split(' ')
            if c[0] == 'x':
                matrix_mult(make_rotX(int(c[1])), transform)
            if c[0] == 'y':
                matrix_mult(make_rotY(int(c[1])), transform)
            if c[0] == 'z':
                matrix_mult(make_rotZ(int(c[1])), transform)
            i += 1
        if lines[i] == 'apply':
            matrix_mult(transform, points)
            r = 0
            while r < len(points):
                c = 0
                while c < len(points[r]):
                    points[r][c] = int(points[r][c])
                    c += 1
                r += 1
            #print_matrix(transform)
        if lines[i] == 'display':
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        if lines[i] == 'save':
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, lines[i+1])
        if lines[i] == 'quit':
            break
        i += 1
