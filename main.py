from tkinter import *
from Buttons import *
import random
import os
import sys

app = Tk()

app.title("Tick-Tac-Toe")

WIDTH = 600
BUTTON_COUNT = 3
HEIGHT = WIDTH + (WIDTH / BUTTON_COUNT/3)

BUTTON_WIDTH = int(round((WIDTH - ((BUTTON_COUNT * 5) + 5)) / BUTTON_COUNT))
BUTTON_HEIGHT = BUTTON_WIDTH
button_coordinates = []


def create_buttons_cordinates():
    i = 0
    while i < BUTTON_COUNT:
        button_coordinates.append((BUTTON_WIDTH * i) + 5 + (i * 5))
        i += 1


def create_buttons(whos_turn):
    button_nr = 0
    for y in button_coordinates:
        for x in button_coordinates:
            MyPlayButton(button_nr, "Click Me", x, y, computer_button_click, BUTTON_HEIGHT, BUTTON_WIDTH, whos_turn, 'white')
            button_nr += 1
    if whos_turn == 'Computer goes first':
        computer_button_click('comp')
        global comp_first
        comp_first = 1


def main():

    canvas = Canvas(app, width=WIDTH, height=HEIGHT)
    canvas.pack()

    wo_goes_first = ['Player goes first', 'Computer goes first']
    whos_turn = random.choice(wo_goes_first)
    lbl1 = Label(app, text=whos_turn, font=("arial", 18))
    lbl1.pack()
    set_all_strike_coordinates(BUTTON_COUNT)
    create_buttons_cordinates()
    create_buttons(whos_turn)

    def test(event):
        x_cor = get_winn(x_coordinates)
        o_cor = get_winn(o_coordinates)
        if x_cor or o_cor:
            if x_cor and comp_first == 1:
                Label(app, text='Computer won', font=("arial", 18)).pack()
                for x in button_list2:
                    if not x in x_cor:
                        x.configure(state='disable')
            elif x_cor and comp_first == 0:
                Label(app, text='Player won', font=("arial", 18)).pack()
                for x in button_list2:
                    if not x in x_cor:
                        x.configure(state='disable')
            elif o_cor and comp_first == 0:
                Label(app, text='Computer won', font=("arial", 18)).pack()
                for x in button_list2:
                    if not x in o_cor:
                        x.configure(state='disable')
            elif o_cor and comp_first == 1:
                Label(app, text='Player won', font=("arial", 18)).pack()
                for x in button_list2:
                    if not x in o_cor:
                        x.configure(state='disable')
            app.unbind('<Button-1>')
    app.bind('<Button-1>', test)
    app.mainloop()


if __name__ == '__main__':
    main()

