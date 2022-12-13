from pathlib import Path
from collections import defaultdict

file_name="input7.txt"
abs_path= Path(str(Path.cwd())+"/day7/"+file_name)
data1 = open(abs_path).read().strip()
lines = [line for line in data1.split('\n')]
# print(X)
path=[]
DD = defaultdict(int)
for line in lines:
    words = line.strip().split()
    # print(words)
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == 'ls':
        continue
    else:
        # print(path,words[0])   
        try:
            sz = int(words[0])
            # print(path,sz)
            for i in range(len(path)+1):
                # DD['/'.join(path[:i])] += sz
                DD['/'.join(path[:i])] += sz
        except:
            pass
print(DD)
ans = 0


for k ,v in DD.items():
    # print(k,v)
    if v <= 100000:
        ans +=v
print(ans)

max_capacity=70000000-30000000
amount_used= DD['/']
to_free=amount_used-max_capacity 
# print(to_free)
best =1e9
for k, v in DD.items():
    if v >= to_free:
        best=min(best,v)
print(best)


# data = [ line.split("\n") for line in open(abs_path).read().strip()]
# input = [ line.replace(" ","")for line in data]
# print(data)