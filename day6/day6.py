from pathlib import Path

file_name="input6.txt"
abs_path= Path(str(Path.cwd())+"/day6/"+file_name)

data = open(abs_path).read().strip()


for i in range(4, len(data)):
    s = set(data[(i-4):i])
    if len(s) == 4:
        print(s,i)
        break

for i in range(14, len(data)):
    s = set(data[(i-14):i])
    if len(s) == 14:
        print(s,i)
        break


    