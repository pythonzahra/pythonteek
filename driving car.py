
import time
import random
from tkinter import *
from tkinter.colorchooser import askcolor

tk = Tk()
tk.title("driving car")


canvas = Canvas(tk, width=600, height=300, bg="skyblue")
canvas.pack()

car_body = None
wheel1 = None
wheel2 = None
car_parts = []
text_id=None

def choose_car_color():
    global car_body, wheel1, wheel2, car_parts
    c = askcolor(title="Choose Car Color")
    color=c[1]
    car_body = canvas.create_rectangle(50,
    150, 150, 200, fill=color)
    wheel1 = canvas.create_oval(60, 200, 90,
    230, fill="black")
    wheel2 = canvas.create_oval(110, 200, 140,
    230, fill="black")
    car_parts = [car_body, wheel1, wheel2]


def show_random_text():
    global text_id
    if text_id is not None:
        canvas.delete(text_id)
    side = random.choice(["left", "right"])
    text_id=canvas.create_text(200, 50, text=side, fill="black", font=("Arial", 16), anchor="center")



def move_right():
    for part in car_parts:
        canvas.move(part, 100, 0)
        time.sleep(0.05)
    tk.update()

def move_left():
    for part in car_parts:
        canvas.move(part, -100, 0)
        time.sleep(0.05)
    tk.update()


btn_color = Button(tk, text="Choose your Car", command=choose_car_color, bg="lightgray")
btn_color.pack(side=TOP)

btn_text = Button(tk, text="Show Text", command=show_random_text, bg="lightblue")
btn_text.pack(side=TOP)

btn_right = Button(tk, text="Move Right", command=move_right, bg="green", fg="white")
btn_right.pack(side=TOP)

btn_left = Button(tk, text="Move Left", command=move_left, bg="red", fg="white")
btn_left.pack(side=TOP)


tk.mainloop()