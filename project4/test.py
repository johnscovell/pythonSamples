import stdarray
import stdio
import stdrandom
import sys
import math

## PRIMES
hi = 1000
lo = 0
num = 0
a = stdarray.create1D(hi-lo)

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
        num += 1

# creates an array of correct size
b = stdarray.create1D(num)
for i in range(0, num):
    b[i] = a[i]


## SAMPLE

k = 4
c = [1, 2, 3, 4, 5]
check = stdarray.create1D(k)

for i in range(0, k):
    check[i] = c[i]

for i in range(len(check)):
    j = i + stdrandom.uniformInt(0, len(check) - i)
    temp = check[i]
    check[i] = check[j]
    check[j] = temp

stdio.writeln(check)
