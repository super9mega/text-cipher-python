import curses
import cipher

# this code takes an input then encodes the code with the Vigenère cipher, which takes a password to encode or decode
# the note, the colin defines the start, if there is a space directly after the colin, its part of the code
# this value if 0 will encrypt, if 1 will decrypt

def endecode(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    height,width = stdscr.getmaxyx()
    s1 = ('encode','decode')
    x = len(s1) // 2
    for i in s1:
     stdscr.addstr((height // 2) - x,(width // 2) - (len(i) // 2),i)
     x = x - 1
    y = x + 1
    x = len(s1) // 2
    z = x
    index = 0
    stdscr.addstr((height // 2) - x,(width // 2) - (len(s1[0]) // 2),s1[0], curses.A_STANDOUT)
    stdscr.addstr(((height // 2) - (x + 2)) , (width // 2) - (len('encode or decode?')) // 2,'encode or decode?')
    stdscr.addstr(((height // 2) - (x - len(s1) - 2)) , (width // 2) - (len('(up/down arrow, right arrow to select)')) // 2,'(up/down arrow, right arrow to select)')
    stdscr.refresh()

    while True:
     a = stdscr.getch()
     if a == curses.KEY_UP:
      if x == z:
       continue
      stdscr.addstr((height // 2) - x,(width // 2) - (len(s1[index]) // 2),s1[index])
      index -= 1
      x += 1
      stdscr.addstr((height // 2) - x,(width // 2) - (len(s1[index]) // 2),s1[index], curses.A_STANDOUT)
      stdscr.refresh()
      continue
     if a == curses.KEY_DOWN:
      if x == y:
       continue
      stdscr.addstr((height // 2) - x,(width // 2) - (len(s1[index]) // 2),s1[index])
      index += 1
      x -= 1
      stdscr.addstr((height // 2) - x,(width // 2) - (len(s1[index]) // 2),s1[index], curses.A_STANDOUT)
      stdscr.refresh()
      continue
     if a == curses.KEY_RIGHT:
      return s1[index]

def userinput(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    height,width = stdscr.getmaxyx()
    stdscr.addstr((height // 2) - 1,  (width // 2) - (len('enter key:')) // 2 , 'enter key:')
    curses.echo()
    stdscr.move((height // 2), 2)
    stdscr.refresh()
    key = stdscr.getstr((height // 2),1, width)

    stdscr.clear()
    curses.curs_set(0)
    height,width = stdscr.getmaxyx()
    stdscr.addstr((height // 2) - 1,  (width // 2) - (len('enter text to change:')) // 2 , 'enter text to change:')
    curses.echo()
    stdscr.move((height // 2), 2)
    stdscr.refresh()
    user = stdscr.getstr((height // 2),1, width)

    return (user, key)

endecpt = curses.wrapper(endecode)
user,key = curses.wrapper(userinput)
user = str(user)
user = user[2:-1]
key = str(key)
key = key[2:-1]
if key == None:
    key = cipher.passwordgen(16)
if endecpt == 'encode':
    print('encrypted string:' + str(cipher.encode(key, user)))
    print('key:' + str(key))
if endecpt == 'decode':
    print('message:' + str(cipher.decode(key, user)))
