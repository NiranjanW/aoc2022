from pathlib import Path
import sys

input_file = sys.argv[1] if len(sys.argv) > 1  else (Path (str(Path.cwd()) +"/day9/"+"input9.txt"))
input_data= open(input_file).read().strip()

lines = [line for line in input_data.split("\n")]
print(lines) 
hx ,hy , tx,ty =0,0,0,0

def touching (x1,x2,y1,y2):
    return abs(x1 -x2) <=1 and abs( y1-y2) <=1


def move(dx,dy):

    global hx , hy ,tx,ty
    hx += dx
    hy += dy

    if not touching(hx ,tx,hy,ty):
        sign_x =0 if hx == tx else (hx -tx) /abs(hx-tx)
        sign_y =0 if hy == ty else (hy -ty) /abs(hy-ty)

        tx += sign_x
        ty += sign_y

dd = {
    "R" : [1,0],
    "U" : [0,1],
    "L" : [-1,0],
    "D" : [0,-1]
}

tail_visited =set()
tail_visited.add((tx,ty))

for line in lines:
    op , amt = line.split()
    amt = int(amt)
    dx ,dy = dd[op]

    for _ in range(amt):
        move(dx , dy)
        tail_visited.add((tx,ty))

print(len(tail_visited))

    # knots=[][]
    # knots[0][0] +=dx
    # knots[0][1] +=dy

