import pathlib
import sys

def parse(puzzle_input):
    return [int(line)for line in puzzle_input.split('\n')]

def nonblank_lines(f):
    for l in f:
        line = l.strip()
        if line:
            yield line

def part1(numbers):
    """Solve part 1."""
    result = []
    
    # for elf in ('\n'.join(numbers.strip())).split('\n\n'):
    for elf in (numbers.split('\n\n')):
        q = 0
        for x in elf.split('\n'):
            q += int(x)
        result.append(q)
    # for n in numbers:
    #     if n.strip('\n'):
    #         result.append(int(n))
    result.sort(reverse=True)
    return result


    # for num1 in numbers:
    #     for num2 in numbers:
    #         if num1 < num2 and num1 + num2 == 2020:
    #             return num1 * num2

if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        numbers = part1(puzzle_input)
       
        print(numbers)
        print(sum(numbers[:3])) 
       