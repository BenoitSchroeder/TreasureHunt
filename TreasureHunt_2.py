# Author: Benoit Schroeder
# TreasureHunt Version 2 object-oriented

import re


class TreasureHunt:

    # Initialize Function for the Object TreasureHunt
    def __init__(self, file, first_clue):
        self.file = file    # File containing the input
        self.table = self.read_input()  # Reads array containing the clues
        self.visited = list()   # List of visited clues
        self.clue = first_clue  # First clue for the treasure hunt

    # Function to read and verify the input file
    def read_input(self):
        table = []
        n = 0
        for line in self.file:
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

    # Function that does the treasure search
    def search_treasure(self):
        self.visited.append(self.clue)
        row = self.clue // 10  # Get the ten's digit representing the row
        col = self.clue % 10  # Get the unit's digit representing the column
        self.clue = self.table[row - 1][col - 1]  # Set the new clue
        while self.clue not in self.visited:
            self.visited.append(self.clue)
            row = self.clue // 10
            col = self.clue % 10
            self.clue = self.table[row - 1][col - 1]
        # Check if treasure is found (same value in the cell as its coordinates)
        if self.visited[-1] == self.clue:
            for n in self.visited:
                r, c = str(n)  # Split the visited clues into the coordinates
                print(r + ' ' + c)  # Print coordinates to STDOUT
            return 0
        else:
            print("NO TREASURE")
        return 0


def main():
    path = input('Path to the Input file: ')   # Read input file path from STDIN
    try:
        with open(path, "r") as f:
            hunt = TreasureHunt(f, 11)
            hunt.search_treasure()
            return 0
    except IOError as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
