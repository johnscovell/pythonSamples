import math
import stdio
import sys

# accepts coordinates of two points on earth. cast as floats and converted to radians
x1 = math.radians(float(sys.argv[1]))
y1 = math.radians(float(sys.argv[2]))
x2 = math.radians(float(sys.argv[3]))
y2 = math.radians(float(sys.argv[4]))

# calculates the great circle distance 'd'
d = 6359.83 * math.acos((math.sin(x1)*math.sin(x2)) + (math.cos(x1)*math.cos(x2)*math.cos(y1-y2)))

# outputs d
stdio.writeln(d)
