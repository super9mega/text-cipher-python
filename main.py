import base64
import random
import string

# this code takes an input then encodes the code with the Vigenère cipher, which takes a password to encode or decode
# the note, the colin defines the start, if there is a space directly after the colin, its part of the code
# this value if 0 will encrypt, if 1 will decrypt

print('encode(0) or decode(1) message? ')
while True:
    try:
        endecpt = int(input())
        if endecpt > 1 or endecpt < 0:
            print('1 or a 0')
            continue
        break
    except ValueError:
        print('enter a number, either 0 or 1')
print('enter key (blank for random): ')
key = input()
print('enter text to change: ')
user = input()

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

def passwordgen(legnth):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    chars = letters + digits + symbols

    password = ''
    for i in range(legnth):
        password += random.choice(chars)
    return(password)


if key == '':
    key = passwordgen(16)
if endecpt == 0:
    print('encrypted string:' + str(encode(key, user)))
    print('key: ' + str(key))
if endecpt == 1:
    print('message: ' + str(decode(key, user)))
