import stdio
import sys

# accepts month, day, and year from user and casts as int
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# calculations to determine the day of the week
y0 = y-(14 - m)//12
x0 = y0 + (y0//4) - (y0//100) + (y0//400)
m0 = m + (12 * ((14 - m)//12)) - 2
dow = (d + x0 + 31 * m0//12) % 7

# outputs day of week
stdio.writeln(dow)
