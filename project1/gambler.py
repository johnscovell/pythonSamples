import stdio
import sys

# accepts number of pennies for each player ('n1', 'n2')
# and probability player 1 wins each toss ('p')
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])

# probability player 2 wins each toss
q = 1 - p

# calculate probability of winning for each player
p1 = (1-(p/q)**n2)/(1-(p/q)**(n1+n2))
p2 = (1-(q/p)**n1)/(1-(q/p)**(n1+n2))

# outputs probabilities
stdio.writeln(str(p1) + " " + str(p2))
