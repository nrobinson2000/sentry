#!/usr/bin/env python3

import curses

from time import sleep

from sentry import sentry

cur = curses.initscr() # initialisation

curses.noecho()
curses.cbreak()
cur.keypad(True)


def move(sentrycmd, delay):
    sentrycmd()
    sleep(delay)
    sentry.stop()

try:
     while True:
        char = cur.getch()

        cur.clear()

        if char == 259:
            cur.addstr("UP")
            move(sentry.up, 0.25)
        if char == 258:
            cur.addstr("DOWN")
            move(sentry.down, 0.25)
        if char == 260:
            cur.addstr("LEFT")
            move(sentry.left, 0.25)
        if char == 261:
            cur.addstr("RIGHT")
            move(sentry.right, 0.25)

except KeyboardInterrupt:
    print("interrupted...")

curses.nocbreak()
cur.keypad(False)
curses.echo()
curses.endwin() # cleanup
print("Goodbye :-)")
