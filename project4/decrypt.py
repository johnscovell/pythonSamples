import rsa
import stdio
import sys


# Entry point.
def main():
    # accepts n and d as inputs
    n = int(sys.argv[1])
    d = int(sys.argv[2])

    # gets width of n
    width = rsa.bitLength(n)
    # reads message
    while not stdio.isEmpty():
        message = stdio.readString()

    # increments through message in steps of width
    for i in range(0, len(message), width):
        s = message[i:i+width]
        y = rsa.bin2dec(s)  # converts s to decimal
        decrypt = rsa.decrypt(y, n, d)  # decryption
        stdio.write(chr(decrypt))


if __name__ == '__main__':
    main()
