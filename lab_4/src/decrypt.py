import hashlib
import random

def decrypt(msg, key):
    decodedMsg = ''
    for char in msg:
        decodedMsg += chr(ord(char) - key)

    return decodedMsg


def getKey(mnemonic):
    passphrase = "password".encode("utf-8")

    seed = hashlib.pbkdf2_hmac("sha512", mnemonic.strip().encode("utf-8"), passphrase, 2048)

    print(seed)

    random.seed(seed)

    return random.randrange(10)


decodedMessage = decrypt(input("Encrypted message: "), getKey(input("Phrase: ")))

print(decodedMessage)
