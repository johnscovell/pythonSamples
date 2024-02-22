import stdio
import sys

# accepts three ints
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# determines minimum, maximum, and middle value
alpha = min(x, y, z)
omega = max(x, y, z)
middle = (x + y + z) - (alpha + omega)

# outputs in ascending order
stdio.writeln(str(alpha) + " " + str(middle) + " " + str(omega))
