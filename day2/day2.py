import pathlib
from pathlib import Path
import sys

def parse(puzzle_input):
    return [line for line in puzzle_input.split('\n')]

def game(plays):
    score =0
    for x in plays:
        op , me = x.split()
        score += {'X' :1 , 'Y':2 , 'Z' :3}[me]
        score += { ('A', 'X') : 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
                   ('B', 'X') : 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
                   ('C', 'X') : 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
                }[op,me]

    return score

def game2(plays):
    score =0
    for x in plays:
        op , me = x.split()
        score += {'X' :0 , 'Y':3 , 'Z' :6}[me]
        score += { ('A', 'X') : 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
                   ('B', 'X') : 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
                   ('C', 'X') : 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
                }[op,me]

    return score

    # strategy = {
    #     'A X' : 3,
    #     'B Y': 2,
    #     'C Z': 1,
    #     'A Y' : 8,
    #     'B X' : 1,
    #     'C Z'  :6
    # }
    # play = plays.split('\n')
    # for  move in plays:
    #     if move in  strategy.keys():
    #         print (strategy.get(move))


# def main():
#     None

if __name__ == '__main__':
    for file in sys.argv[1:]:
        print(f"\n{file}:")
        file = Path(str(Path.cwd())+"/"+file)
        puzzle_input = [ line.strip()  for line in open(file)]
        final_score = (game(puzzle_input))
        print(final_score)


   