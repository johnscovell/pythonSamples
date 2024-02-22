import stdio
import sys

# user inputs n
n = int(sys.argv[1])

for a in range(1, int(n**(1/3)) + 1):
    for b in range(a + 1, int((n-a**3)**(1/3)) + 1):
        for c in range(a + 1, int(n**(1/3)) + 1):
            for d in range(c + 1, int((n-c**3)**(1/3)) + 1):
                # checks if a^3+b^3 = c^3+d^3
                if a**3+b**3 == c**3+d**3:
                    # outputs result
                    stdio.writeln(str(a**3+b**3) + " = " + str(a) + "^3 + " + str(b) + "^3 = "
                                  + str(c) + "^3 + " + str(d) + "^3")
