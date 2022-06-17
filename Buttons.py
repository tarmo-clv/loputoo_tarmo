from tkinter import *
from PIL import Image, ImageTk
import random

press_order = []
button_list = []
button_list2 = []
comp_first = 0
x_coordinates = []
o_coordinates = []
BUTTON_COUNT = 0
strike_coordinates = []
winn_coordinates = None
winnning_player =None


class MyPlayButton(Button):
    def __init__(self, buttonnr, text, x, y, command, height, width, turn, color=None):
        button_list.append(self)
        button_list2.append(self)
        self.buttonnr = buttonnr
        self.text = text
        self.x = x
        self.y = y
        self.command = command = lambda: computer_button_click(self)
        self.color = color
        self.height = height
        self.width = width
        self.turn = turn
        super().__init__()
        self['bg'] = self.color
        self['text'] = self.text
        self['command'] = self.command = lambda: computer_button_click(self)
        self['height'] = self.height
        self['width'] = self.width
        self.place(x=self.x, y=self.y, height=self.height, width=self.width)
        self.toggleState = 1
        X_image = Image.open('X.png')
        resize_X_image = X_image.resize((int(width), int(height)))
        O_image = Image.open('O.png')
        resize_O_image = O_image.resize((int(width), int(height)))
        self.firstImage = ImageTk.PhotoImage(resize_X_image)
        self.secondImage = ImageTk.PhotoImage(resize_O_image)
        self.bind('<Button-1>', self.clickFunction)
        self.update()

    def clickFunction(self, event=None):
        if self.cget('state') != 'disabled':
            if len(press_order) == 0 or len(press_order) % 2 == 0:
                self.config(image=self.firstImage)
                global x_coordinates
                x_coordinates.append((self, (int(self.buttonnr / BUTTON_COUNT), self.buttonnr % BUTTON_COUNT)))
            else:
                self.config(image=self.secondImage)
                global o_coordinates
                o_coordinates.append((self, (int(self.buttonnr / BUTTON_COUNT), self.buttonnr % BUTTON_COUNT)))
        self.unbind('<Button-1>')


def get_winn(symbol_coordinates):
    global strike_coordinates, winn_coordinates
    for x in strike_coordinates:
        i = 0
        winn_buttons = []
        for y in symbol_coordinates:
            if y[1] in x:
                i += 1
                winn_buttons.append(y[0])
        if i == 3:
            return winn_buttons
    return None


def computer_button_click(self):
    global press_order, comp_first
    if self in press_order or (get_winn(x_coordinates) or get_winn(o_coordinates)):
        pass
    else:
        if not self == 'comp':
            press_order.append(self)
            button_list.remove(self)
        else:
            comp_first = 1

        if (len(press_order) + 1 + comp_first) % 2 == 0:
            if not len(button_list) == 0:
                next_click = random.choice(button_list)
                next_click.event_generate('<Button-1>')
                button_list.remove(next_click)
                press_order.append(next_click)
            else:
                pass


def set_all_strike_coordinates(btn):
    global BUTTON_COUNT, strike_coordinates
    BUTTON_COUNT = btn
    all_coordinates = []

    for x in range(0, (BUTTON_COUNT * 2) + 2):
        strike_coordinates.append([])

    for x in range(0, (BUTTON_COUNT * BUTTON_COUNT)):
        all_coordinates.append((int(x / BUTTON_COUNT), int(x % BUTTON_COUNT)))

    for x in range(0, BUTTON_COUNT):
        f = 0
        for y in all_coordinates:
            if y[0] == x:
                strike_coordinates[x].insert(x+f, y)
                f += 1
        for z in all_coordinates:
            if z[1] == x:
                strike_coordinates[x + BUTTON_COUNT].insert(x + BUTTON_COUNT, z)
        for i in all_coordinates:
            if i[0] == x and i[1] == (BUTTON_COUNT - (x + 1)) and (i[0] + i[1]) == (BUTTON_COUNT - 1):
                strike_coordinates[-2].insert(-2, i)
        for j in all_coordinates:
            if j[0] == x and j[1] == ((x + BUTTON_COUNT) - BUTTON_COUNT):
                strike_coordinates[-1].insert(-1, j)
