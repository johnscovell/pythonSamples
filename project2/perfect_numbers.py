import stdio
import sys

# accepts user input for perfect numbers <= n
n = int(sys.argv[1])

# repeats 2 to n+1
for i in range(2, n+1):
    total = int(0)  # sum of divisors of i
    for j in range(1, i//2 + 1):
        if (i % j) == 0:  # checks possible perfect numbers
            total += j  # adds to total
    # writes i if total is equal to i
    if total == i:
        stdio.writeln(i)
