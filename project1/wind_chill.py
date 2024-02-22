import stdio
import sys

# accepts temperature 't' (Fahrenheit) and wind speed 'v' (miles per hour) as floats
t = float(sys.argv[1])
v = float(sys.argv[2])

# calculates wind chill and assigns to 'w'
w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v**0.16

# outputs wind chill
stdio.writeln(w)
