from pathlib import Path
import sys

def part1(input):
    ans1 = 0
    ans2 =0
    for inp in input:
        x, y = inp.split(',')
        s1,e1 = x.split('-')
        s2,e2 =y.split('-')
       
        s1,e1,s2,e2 = [ int(x) for x in [s1,e1,s2,e2]]
        # print(s1,s2,e1,e2)
        if s1<=s2 and e2<=e1 or s2<=s1 and e1<=e2: 
            ans1 += 1
        if not (e1 < s2 or  s1 > e2):
            ans2 +=1
     
        # x = [i for i in range(int(x.split('-')[0]), int(x.split('-')[1])+1 )]
        # for i in range(int(x.split('-')[0]), int(x.split('-')[1])+1):
    print(ans2)   #     print(i)
    
     


if __name__ == '__main__':
    file_name = 'input4.txt'
    input_data = Path(str(Path.cwd())+"/day4/"+file_name)
    data =open(input_data).read().strip()
    X = [ line.strip() for line in data.split('\n')]

    part1(X)
