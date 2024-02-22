import math
import stdio
import sys

#  accepts angle of incidence 'theta1' and the indices of refraction 'n1' and 'n2'
theta1 = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

#  convert theta1 to radians and calculate sin(theta1)
sinTheta1 = math.sin(math.radians(theta1))

#  calculate sinTheta2 to calculate theta2
sinTheta2 = (n2/n1/sinTheta1)**-1
theta2 = math.degrees(math.asin(sinTheta2))  # converted to degrees

# outputs theta2
stdio.writeln(theta2)
