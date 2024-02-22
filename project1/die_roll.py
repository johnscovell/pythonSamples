import stdio
import sys
import stdrandom

# accepts input for number of sides on dice
n = int(sys.argv[1])

# adds two random dice rolls
diceSum = (stdrandom.uniformInt(1, n+1)) + (stdrandom.uniformInt(1, n+1))

# outputs sum
stdio.writeln(diceSum)
