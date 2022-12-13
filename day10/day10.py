
with open("./day10/input10.txt" ,"r") as f:
    data = f.read().strip().split("\n")
    lines = [ l for l in data]

X =1
op =0
ans =0
needed = [20 ,60,100,140,180,220]
for l in lines:
    parts = l.split(" ")
    print(parts)

    if parts[0] == "noop":
         op +=1

         if op in needed:
             ans += op *X
    elif parts[0]== "addx":
        V =int(parts[1])
        X += V

        op += 1

        if op in needed:
            ans += op * (X-V)

        op += 1

        if op in needed:
            ans += op * (X -V)

        # op += 1

print(ans)






    # print(reg ,val)