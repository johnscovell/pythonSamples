import stdio
import sys

# the nth number of fibonacci sequence
n = int(sys.argv[1])

a = 1  # first fibonacci number
b = 1  # second fibonacci number
i = 3  # starting iterative

# while i less than or equal to nth number
while i <= n:
    temp = a + b  # stores a + b
    a = b  # write previous b to a
    b = temp  # write temp to b
    i += 1

# outputs b
stdio.writeln(b)
