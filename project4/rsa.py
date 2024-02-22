import stdio
import stdrandom
import sys
import stdarray


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    primelist = _primes(lo, hi)  # generates list of primes

    # finds two randomly chosen primes from list
    p = _choice(primelist)
    q = _choice(primelist)
    while p == q:
        # ensures no duplicates
        q = _choice(primelist)

    # calculates n and m
    n = p*q
    m = (p-1)*(q-1)

    # creates new list from 2 to m of primes
    mlist = _primes(2, m)
    e = _choice(mlist)  # random choice from mlist
    while e % m == 0:
        # ensures e does not divide m
        e = _choice(mlist)

    # chooses d so that ed%1=1
    for i in range(1, m):
        check = e*i % m
        if check == 1:
            d = i

    # returns variables
    return n, e, d


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    return x**e % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    return y**d % n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % width)


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    num = 0  # keeps track of prime numbers
    a = stdarray.create1D(hi - lo)  # create array

    # iterates from low to high
    for i in range(lo, hi):
        prime = True
        for j in range(2, i):
            # iterates from 2 to i to check for primes
            if i % j == 0:
                # remainder of 0 means not prime
                prime = False
                break
        if prime is True and i != 1 and i != 0:
            # adds the prime number to array 'a'
            a[num] = i
            num += 1  # increments num

    # creates an array of correct size
    b = stdarray.create1D(num)
    for i in range(0, num):
        b[i] = a[i]

    return b


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    b = a  # creates copy of list 'a'
    shuff = stdarray.create1D(k)  # creates array of size k

    # iterates through b and assigns to shuff
    for i in range(0, k):
        shuff[i] = b[i]

    # alt to shuffle function found in stdrandom module
    for i in range(len(shuff)):
        j = i + stdrandom.uniformInt(0, len(shuff) - i)
        temp = shuff[i]
        shuff[i] = shuff[j]
        shuff[j] = temp

    # returns randomly shuffled array
    return shuff


# Returns a random item from the list a.
def _choice(a):
    r = stdrandom.uniformInt(0, len(a))
    return a[r]


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
