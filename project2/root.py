import stdio
import sys

# accepts inputs to find kth root of c up to epsilon decimal points
k = int(sys.argv[1])
c = float(sys.argv[2])
epsilon = float(sys.argv[3])

# calculates each required decimal point of kth root of c
t = c
while abs(1 - (c/(t**k))) > epsilon:
    t = t - (t**k - c)/(k*(t**(k-1)))

# outputs t (the kth root of c)
stdio.writeln(t)
