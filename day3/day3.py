from pathlib import Path
import sys

# for file in sys.argv[1:]:

def part1(input_data):

    ans = 0
    for line in open(input_data):
    
        f_p , s_p = line[:len(line)//2] , line[len(line)//2:]
        for c in f_p:
            if(c in s_p):
                if  ('a' <=c<= 'z'):
                    ans += ord(c) - ord('a') +1
                else :
                    ans += ord(c) -ord('A') +1+26
                break
    print(ans)


def score(c):
     if  ('a' <=c<= 'z'):
        return ord(c) - ord('a') +1
     else :
        return ord(c) -ord('A') +1+26

def part2(input_data):
    i =0
    
    ans = 0
    line = [x for x in open(input_data)]
    while i < (len(line)):
        for c in line[i]:
            if c in line[i+1] and  c in line[i+2]:
                 ans += score(c)               
                 break
        i += 3
    print(ans)

if __name__ == '__main__':
      
    file1 = 'input3.txt'
    input_data = Path(str(Path.cwd())+"/day3/"+file1)
    part2(input_data)
# lines = [l for l in input_data.split('\n')]
# middle_idx = len(lines[0])/2
# first_pack , second_pack =  lines[:middle_idx] ,lines[middle_idx:],
# print(first_pack, second_pack)
# letters={}

# for c in first_pack:
#     if c in letters.key():
#         continue
#     letters[c] =1