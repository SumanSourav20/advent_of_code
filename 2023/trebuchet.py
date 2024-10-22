import sys
from typing import List

def find_first_number(line: str, numbers: List[str]) -> str:
    n = len(line)

    for i in range(n):
        if line[i].isdigit():
            return line[i]

        for num_idx, number in enumerate(numbers):
            if line.startswith(number, i):
                return str(num_idx + 1)

def main():
    trebuchet_strs = open('trebuchet.txt', 'r')
    # print(sys.getsizeof(trebuchet_strs))
    # print(sys.getsizeof(list(trebuchet_strs)))
    total = 0
    first_digit = ''
    last_digit = ''

    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    reversed_numbers = [number[::-1] for number in numbers]

    for line in trebuchet_strs:
        first_digit = find_first_number(line, numbers)
        
        last_digit = find_first_number(line[::-1], reversed_numbers)

        total += int(first_digit+last_digit)

    print(total)

        
if __name__ == "__main__":
    main()