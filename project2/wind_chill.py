import stdio
import sys

# accepts temperature and wind speed as floats
t = float(sys.argv[1])
v = float(sys.argv[2])

if t > 50:
    # if temperature > 50, error outputs
    stdio.writeln('Value of t must be <= 50 F')
elif v <= 3:
    # if wind speed <= 3, error outputs
    stdio.writeln('Value of v must be > 3 mph')
else:
    # calculates wind speed and outputs result
    w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v**0.16
    stdio.writeln(w)
