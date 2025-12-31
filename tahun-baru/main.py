import curses
import random
import time
import math

TEXT = "HAPPY NEW YEAR 2026"
WARNA = [1, 2, 3, 4, 5, 6, 7]

# Tulisan di tengah layar
def textTampil(stdscr, y, text):
    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text) // 2
    stdscr.addstr(y, x, text)

def kembangApi(stdscr):
    h, w = stdscr.getmaxyx()
    x = random.randint(10, w - 10)
    y = h - 2
    peak = random.randint(h // 4, h // 2)

    color = random.choice(WARNA)

    # Kembang api yg naik
    while y > peak:
        stdscr.clear()
        stdscr.attron(curses.color_pair(color))
        stdscr.addstr(y, x, "|")
        stdscr.attroff(curses.color_pair(color))
        stdscr.refresh()
        y -= 1
        time.sleep(0.02)

    for r in range(1, 8):
        stdscr.clear()
        for angle in range(0, 360, 20):
            rad = math.radians(angle)
            ex = int(x + r * math.cos(rad))
            ey = int(y + r * math.sin(rad))
            if 0 < ey < h and 0 < ex < w:
                stdscr.attron(curses.color_pair(random.choice(WARNA)))
                stdscr.addstr(ey, ex, "*")
                stdscr.attroff(curses.color_pair(random.choice(WARNA)))
        textTampil(stdscr, h // 2, TEXT)
        stdscr.refresh()
        time.sleep(0.05)

# Interfacenya
def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    for i in range(1, 8):
        curses.init_pair(i, i, -1)

    while True:
        kembangApi(stdscr)

curses.wrapper(main)