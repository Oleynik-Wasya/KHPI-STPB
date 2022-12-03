from math import gcd
import random
from random import randint
import sys


def multiplicativeInverse(e, phi):
    return extendedEuclid(e, phi)[1] % phi


def extendedEuclid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d2, x2, y2 = extendedEuclid(b, a % b)
        d, x, y = d2, y2, x2 - (a // b) * y2
        return d, x, y


def convertMessageToNumber(msg):
    encodedMsg = 0
    for char in msg:
        encodedMsg = encodedMsg ^ ord(char)
        encodedMsg = encodedMsg << 6
    return encodedMsg


def getRandomPrime(primeSize):
    x = randint(1 << (primeSize - 1), (1 << primeSize) - 1)
    while not (isPrime(x)):
        x = randint(1 << (primeSize - 1), (1 << primeSize) - 1)
    return x


def isPrime(n):
    if n % 2 == 0:
        return False

    for i in range(1, 40):
        a = random.randint(1, n - 1)
        if isComposite(a, n):
            return False
    return True


def isComposite(a, n):
    t, d = decompose(n - 1)
    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        return False

    for i in range(1, t):
        x0 = x
        x = pow(x0, 2, n)
        if x == 1 and x0 != 1 and x0 != n - 1:
            return True
    if x != 1:
        return True

    return False


def decompose(n):
    i = 0
    while n & (1 << i) == 0:
        i += 1
    return i, n >> i


def getKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    for i in range(2, phi):
        if gcd(phi, i) == 1:
            e = i
            break

    d = multiplicativeInverse(e, phi)

    return n, e, d


try:
    modulusSize = int(input("Enter module size: "))

except:
    modulusSize = 1024

msg = input("Enter message: ")

primeSize = modulusSize // 2
p = getRandomPrime(primeSize)
q = getRandomPrime(primeSize)
while p == q:
    q = getRandomPrime(primeSize)

n, e, d = getKeys(p, q)

encodedMsg = convertMessageToNumber(msg)
encryptedMsg = pow(encodedMsg, e, n)
decryptedMsg = pow(encryptedMsg, d, n)

print("Public key (e, n):")
print("\te = ", e)
print("\tn = ", n)
print("-----------------------")
print("\nPrivate key (d, n):")
print("\td = ", d)
print("\tn = ", n)
print("-----------------------")
print("\nOriginal message string:\n\t", msg)
print("\nConverted to integer message:\n\t", encodedMsg)
print("\nEncrypted message:\n\t", encryptedMsg)
print("\nDecrypted message:\n\t", decryptedMsg)
if encodedMsg == decryptedMsg:
    print("\nThe decrypted message and the original encoded message match.")
