import rsa
import stdio
import sys


# Entry point.
def main():
    # accepts low and high interval
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # generates key and prints to terminal
    key = rsa.keygen(lo, hi)
    stdio.writeln(str(key[0]) + ' ' + str(key[1]) + ' ' + str(key[2]))


if __name__ == '__main__':
    main()
