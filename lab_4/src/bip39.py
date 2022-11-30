import os
import hashlib
import random

message = 'test'

def generateKeys():
    entropy = hashlib.sha256(os.urandom(16) + b"test").digest()[:12]
    print("Entropy: ", list(entropy))

    words = []
    with open("english.txt", "r", encoding="utf-8") as f:
        for word in f.readlines():
            words.append(word)

    # print(words)

    def mapToPhrase(index):
        return words[index]

    phrase = ' '.join(map(mapToPhrase, list(entropy))).replace('\n', ' ').replace('\r', '').strip()
    print(phrase)

    passphrase = "password".encode("utf-8")

    seed = hashlib.pbkdf2_hmac("sha512", phrase.encode("utf-8"), passphrase, 2048)

    print(seed)

    random.seed(seed)

    return (random.randrange(10), phrase)


def encrypt(msg, key):
    encodedMsg = ''
    for char in msg:
        encodedMsg += chr(ord(char) + key)

    return encodedMsg


key, mnemonic = generateKeys()

encryptedMessage = encrypt(message, key)
print(encryptedMessage)

print("Encrypted message: ", encryptedMessage)
print("Phrase: ", mnemonic)
