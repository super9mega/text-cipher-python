import curses
import cipher

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

if key == '':
    key = cipher.passwordgen(16)
if endecpt == 0:
    print('encrypted string:' + str(cipher.encode(key, user)))
    print('key: ' + str(key))
if endecpt == 1:
    print('message: ' + str(cipher.decode(key, user)))
