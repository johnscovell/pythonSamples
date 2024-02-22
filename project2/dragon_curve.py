import stdio
import sys

# user inputs curve order n
n = int(sys.argv[1])

# writes dragon and nogard
dragon = str('F')
nogard = str('F')

# writes dragon from 1 to n+1
for i in range(1, n+1):
    temp = dragon + 'R' + nogard
    dragon = dragon + 'L' + nogard
    nogard = temp

# outputs dragon
stdio.writeln(dragon)
