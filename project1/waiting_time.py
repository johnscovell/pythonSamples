import math
import stdio
import sys

# accepts lambda (avg number of events per unit of time) and t (time) as floats
lamb = float(sys.argv[1])
t = float(sys.argv[2])

# calculates probability that one has to wait longer than time t until next event
p = math.exp(-lamb*t)

# outputs p
stdio.writeln(p)
