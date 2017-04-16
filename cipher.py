import string
import random

def passwordgen(legnth):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    chars = letters + digits + symbols

    password = ''
    for i in range(legnth):
        password += random.choice(chars)
    return(password)


def encode(a, b):
    x = len(b)
    y = len(a) - 1
    z = -1
    realkey = []
    for i in range(x):
        z += 1
        realkey.append(a[z])
        if z >= y:
            z = -1
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    chars = list(letters + digits + symbols)
    chars.append(' ')
    ans = []
    for i in range(x):
        cypher = chars.index(realkey[i])
        let = chars.index(b[i])
        a = let + cypher
        if a > len(chars):
            a -= len(chars)
        ans.append(chars[a])
    return ''.join(ans)


def decode(a, b):
    x = len(b)
    y = len(a) - 1
    z = -1
    realkey = []
    encry = []
    for i in range(x):
        z += 1
        realkey.append(a[z])
        if z >= y:
            z = -1
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    chars = list(letters + digits + symbols)
    chars.append(' ')
    ans = []
    for i in range(x):
        cypher = chars.index(realkey[i])
        let = chars.index(b[i])
        a = let - cypher
        if a < 0:
            a += len(chars)
        ans.append(chars[a])
    return ''.join(ans)
