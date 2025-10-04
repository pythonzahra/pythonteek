import time
from tkinter import *

tk = Tk()
tk.title("Moving Shape")
canvas = Canvas(tk, width=400, height=200, bg="white")
canvas.pack()

triangle = canvas.create_polygon(200, 50, 200, 100, 250, 75, fill="blue")

def move_right():
    for i in range(30):
        canvas.move(triangle, 5, 0)
        tk.update()
        time.sleep(0.05)

def move_left():
    for i in range(30):
        canvas.move(triangle, -5, 0) 
        tk.update()
        time.sleep(0.05)

btn1 = Button(tk, text="Move Right", command=move_right, bg="green", fg="white")
btn1.pack(side=RIGHT, )

btn2 = Button(tk, text="Move Left", command=move_left, bg="red", fg="white")
btn2.pack(side=LEFT)

tk.mainloop()
