import math
import stdio
import sys

# accepts latitude and longitude and casts as floats. longitude = x so only one variable is used
lat = float(sys.argv[1])
x = float(sys.argv[2])

# convert latitude to radians
lat = math.radians(lat)

# determines x and y coordinates in terms of latitude and longitude
y = math.log((1+math.sin(lat))/(1-math.sin(lat)))/2

# outputs x and y
stdio.writeln(str(x) + " " + str(y))
