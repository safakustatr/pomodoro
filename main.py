from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_string = ""
reps = 0
timer = None
WORK_REPS = [1, 3, 5, 7]
BREAK_REPS = [2, 4, 6]

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer, check_string, reps
    window.after_cancel(timer)
    reps = 0
    check_string = ""
    check_mark_label.config(text=check_string)
    heading_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps in WORK_REPS:
        count_down(work_sec)
        heading_label.config(text="Work", fg=GREEN)
    elif reps in BREAK_REPS:
        count_down(short_break_sec)
        heading_label.config(text="Break", fg=PINK)
    else:
        count_down(long_break_sec)
        heading_label.config(text="Break", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global check_string
    count_min = math.floor(count / 60)
    count_sec = int(count % 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps < 8:
            if reps in WORK_REPS:
                check_string += "✔️"
                check_mark_label.config(text=check_string)
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

heading_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
heading_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill = "white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

check_mark_label = Label(text=check_string, fg=GREEN, bg=YELLOW)
check_mark_label.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()