# TreasureHunt

## General information
Treasue hunt is a program to explore a table for treasure. The values in the table are clues. The treasure is found in a cells whose value is the same as its coordinates. First the programs read in the treasure map data into a 5 by 5 array.

## TreasureHunt_1

TreasureHunt_1.py is the functional programming approach implementation of the treasure hunt. It is implemented with a recursion.

How to run: python3 TreasureHunt_1.py

## TreasureHunt_2

TreasureHunt_2.py is the object-oriented implementation of the treasure hunt. It is implemented without a recursion.

How to run: python3 TreasureHunt_2.py


## Input/Output

Both implementation. Ask for a input file at the start of the program. Input_1.txt and Input_2.txt are two example inputs.
### Input Format
Input contains five lines each containing five space separated integers. The integers are numbers between 11 and 55, where the ten's digit represents the row number and the unit's digit represents the column number of the cell containing the next clue.

### Output Format
If the treasure is found, the program output the index (row, column) of cells it visits during its search for treasure (separated by a single space). Cells must be separated by a newline “\n”.
If there is no treasure, it prints “NO TREASURE”
