# Author: Benoit Schroeder
# TreasureHunt Version 1 functional programming with recursion

import re


# Function to read and verify the input file
def read_input(file):
    table = []
    n = 0
    for line in file:
        n += 1
        if n <= 5:
            if re.match('^([0-9][0-9] ){4}[0-9][0-9]$', line):
                tmp = []
                for num in line.split(' '):
                    if 11 <= int(num) <= 55:
                        tmp.append(int(num))
                    else:
                        raise Exception('Not all numbers in the input are in the range (11,55).')
                table.append(tmp)
            else:
                raise Exception('Not all the lines contain 5 space separated integers.')
        else:
            raise Exception('The input has more than 5 lines.')
    if n != 5:
        raise Exception('The input does not have 5 lines.')
    # table = [[int(num) for num in line.split(' ')] for line in file]
    return table


# Function for the recursive treasure hunt
def recursive_treasure_hunt(current_clue, table, visited):
    row = current_clue // 10    # Get the ten's digit representing the row
    col = current_clue % 10     # Get the unit's digit representing the column
    new_clue = table[row-1][col-1]  # Set the new clue
    visited.append(current_clue)   # Add current clue to the visited list

    # Check if treasure is found (same value in the cell as its coordinates)
    if new_clue == current_clue:
        for n in visited:
            r, c = str(n)   # Split the visited clues into the coordinates
            print(r+' '+c)  # Print coordinates to STDOUT
        return 0
    # If new clue was already visited we can stop search because we run in circles
    elif str(new_clue) in visited:
        print("NO TREASURE")
        return 0
    # Run the recursive treasure hunt with the new clue
    else:
        recursive_treasure_hunt(new_clue, table, visited)
    return 0


def main():
    path = input('Path to the Input file: ')   # Read input file path from STDIN
    try:
        with open(path, "r") as f:
            table = read_input(f)  # Array containing the clues
            visited = list()  # List of visited clues
            clue = 11  # First clue for the treasure hunt
            recursive_treasure_hunt(clue, table, visited)  # Run the recursive treasure hunt
            return 0
    except IOError as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
