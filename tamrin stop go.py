import tkinter as tk
import time

# ساخت پنجره
root = tk.Tk()
root.title("Moving Car Example")

canvas = tk.Canvas(root, width=600, height=300, bg="lightblue")
canvas.pack()

# کشیدن ماشین (یک مستطیل + دو تا چرخ)
car_body = canvas.create_rectangle(50, 150, 150, 200, fill="blue")
wheel1 = canvas.create_oval(60, 200, 90, 230, fill="black")
wheel2 = canvas.create_oval(110, 200, 140, 230, fill="black")

car_parts = [car_body, wheel1, wheel2]

# متغیر کنترل حرکت
running = False

# تابع شروع حرکت
def start_moving():
    global running
    running = True
    for _ in range(100):  # ماشین حداکثر 100 بار حرکت می‌کند
        if not running:   # اگر stop زده شود
            break
        for part in car_parts:
            canvas.move(part, 10, 0)  # حرکت به راست
        canvas.update()
        time.sleep(0.1)  # سرعت حرکت

# تابع توقف حرکت
def stop_moving():
    global running
    running = False

# دکمه‌ها
btn_start = tk.Button(root, text="Start Car", command=start_moving, bg="green", fg="white")
btn_start.pack(side=tk.LEFT, padx=10, pady=10)

btn_stop = tk.Button(root, text="Stop Car", command=stop_moving, bg="red", fg="white")
btn_stop.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
