import base64
import random 
import string

# this code takes an input then encodes the code in AES with a password or decrypts the password
# note, the colin defines the start, if there is a space directly after the colin, its part of the code
#this value if 0 will encrypt, if 1 will decrypt
print('encode(0) or decode(1) message? ')
while True:
    try:
        endecpt = int(input())
        break
    except ValueError:
        print('enter a number, either 0 or 1')
print('enter key: ')
key = input()
print('enter text to change: ')
user = input()

def encode(key, user):
    x = len(user)
    y = len(key) - 1
    z = -1
    realkey = []
    encry = []
    for i in range(x):
        z += 1
        realkey.append(key[z])
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
        let = chars.index(user[i])
        key = let + cypher
        if key > len(chars):
            key -= len(chars)
        ans.append(chars[key])
    return ''.join(ans)
    
    
def decode(key, user):
    x = len(user)
    y = len(key) - 1
    z = -1
    realkey = []
    encry = []
    for i in range(x):
        z += 1
        realkey.append(key[z])
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
        let = chars.index(user[i])
        key = let - cypher
        if key < 0:
            key += len(chars)
        ans.append(chars[key])
    return ''.join(ans)    

def passwordgen():
# this program generates passwords based on the legnth defined below
    legnth = 16
# and based on the chars below (but works without any confg)
    letters = string.ascii_letters 
    digits = string.digits 
    symbols = string.punctuation
    chars = letters + digits + symbols
# based of the ideas shown in 'https://code.sololearn.com/cYhUD6B6Gry6/#py'

    password = ''
    for i in range(legnth):
        password += random.choice(chars)
    return(password)


if key == None:
    key = passwordgen()
if endecpt == 0:
    print('encrypted string:' + str(encode(key, user)))
    print('key: ' + str(key))
if endecpt == 1:
    print('message: ' + str(decode(key, user))) 
