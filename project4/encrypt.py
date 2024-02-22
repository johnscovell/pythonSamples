import rsa
import stdio
import sys


# Entry point.
def main():
    # accepts command line inputs
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # gets number of bits per character of n
    width = rsa.bitLength(n)

    # accepts message from input
    message = ''
    ghost = 0
    while not stdio.isEmpty():
        if ghost != 0:
            message = message + stdio.readLine() + '\n'
        else:
            message = stdio.readLine() + '\n'
        ghost += 1

    # iterates through each character of message
    for i in range(0, len(message)):
        c = str(message[i:i+1])  # slices each character
        x = ord(c)
        # converts to binary
        stdio.write(rsa.dec2bin(rsa.encrypt(x, n, e), width))

    stdio.writeln()


if __name__ == '__main__':
    main()
