from pathlib import Path
import sys
from collections import defaultdict

DIR = [(-1,0),(0,1),(1,0),(0,-1)]

input_file = sys.argv[1] if len(sys.argv) > 1  else (Path (str(Path.cwd()) +"/day8/"+"example.txt"))
input_data=  open(input_file).read().strip()
lines = [x for x in input_data.split("n")]


Grid =[]
for line in lines:
    row =line
    Grid.append(row)


R = len(Grid)
C = len(Grid[0])
for r in range(R):
    for c in range(C):
        vis = False
        rr = r
        cc =c
        for (dr, dc) in DIR:

            while True:
                rr += dr
                cc += dc 
                if not ( 0<=rr<R and 0<=cc<C):
                    break
                if Grid[rr][cc] >= Grid[r][c]:
                    print('CHECK' ,r,c ,rr,cc ,Grid[rr][cc],Grid[r][c])
        # if r <= rr and r <= cc


for line in lines:
    words = line.split()
    print(words)

# data = [ int(chr) for str in input_data for chr in str  ]
# print(data)

def tree(inp , x,y):
    pass
