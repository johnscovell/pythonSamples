import stdio
import sys

# stores user input as ints
n = int(sys.argv[1])
k = int(sys.argv[2])
total = 0

# adds each i^k to the total
for i in range(1, n+1):
    total += i ** k

# writes sum of powers
stdio.writeln(total)
