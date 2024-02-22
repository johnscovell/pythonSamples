import stdio
import sys

# accepts two ints from command line
p = int(sys.argv[1])
q = int(sys.argv[2])

# determines greatest common devisor
while (p % q) != 0:
    temp = p % q
    p = q
    q = temp
    if p % q == 0:  # catches final p % q before while break
        p = temp

# outputs p
stdio.writeln(p)
