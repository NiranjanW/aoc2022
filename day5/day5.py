
from pathlib import Path

if __name__ == "__main__":
    file_name = 'example.txt'
    file = Path(str(Path.cwd())+"/day5/" + file_name)
    with open(file, 'r') as f:
        stack_strings , instructions = (x.splitlines() for x in f.read().strip("\n").split('\n\n'))
    # print(stack_strings, move)

    stack_strings = { int(digit):[] for digit in stack_strings[-1].replace(" " ,"")}
    indexes =[index for index, char in enumerate(stack_strings[-1]) if char != " "]

    def display_stack(stacks):
        print("\n\nStack\n")
        for stack in stacks:
            print(stack,stacks[stack])
        print("\n")
    
    def loadstacks():
        for string in stack_strings[:-1]:
            stack_num =1
            for index in indexes:
                if string[index] == " ":
                    pass
                else:
                    stack[stack_num].insert(0,string[index])
                stack_num +=1
    
def getStackEnds():
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer

    def emptyStacks():
        for stac_num in stacks:
            stacks[stack_num].claer()
    
    for instruction in instructions:
        instruction =instructions.replace("move","").replace("to", "").replace("from", "").strip().split( " ")
        instruction = [int(i) for i in instruction]

        crates = instruction[0]
        from_stack = instruction[1]
        to_Stack = instruction[2]

        from crate in range(crates):
        crate_removed = stacks[from_stack].pop()
        stacks[to_stack].append(crate_removed)


    print(stack , indexes)

