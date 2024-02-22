import stdio
import sys

# accepts masses of two objects (kg) and distance between them 'r' (meter)
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])

# gravitational constant (m^3 kg^-1 s^-2)
G = 6.674e-11

# calculation of gravitational force between the two objects
f = (G * m1 * m2)/(r**2)

# outputs force
stdio.writeln(f)
