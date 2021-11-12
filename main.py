import curses
from curses import wrapper
import time
import random

TEXTOS = ["o rato roeu a roupa do rei de roma", "3 pratos de trigo para 3 tigres tristes","sushi com salsicha", "meu amigo da escola é um macaco"]


def menu(stdscr):
    stdscr.clear()
    stdscr.addstr(10,10,"Teste de Digitação")
    stdscr.addstr(15,15,"Aperte qualquer tecla")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm = 0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"WPM: {wpm}")
    for i,c in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if c != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0,i,c,color)


def wpm(stdscr):
    target_text = random.choice(TEXTOS)
    current_text = []
    wpm = 0 
    start_time = time.time()
    stdscr.nodelay(True)
    
    while True:
        time_elapsed = max(time.time() - start_time,1)
        wpm = round((len(current_text)/(time_elapsed/60)/5))
        stdscr.clear()
        display_text(stdscr,target_text,current_text,wpm)
        stdscr.refresh()
        
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key_pressed =  stdscr.getkey()
        except:
            continue

        #se esc for clicado para sair
        if ord(key_pressed) == 27:
            break
        if key_pressed in ("KEY_BACKSPACE",'\b',"\x7f"):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)< len(target_text):
            current_text.append(key_pressed)

        

def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_BLACK,curses.COLOR_WHITE)

    menu(stdscr)
    while True:
        wpm(stdscr)
        stdscr.addstr(2,0,"Completo! Aperte qualquer tecla para continuar")
        key =stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)
