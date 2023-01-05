from tkinter import *
import math as m
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    short_break_sec = SHORT_BREAK_MIN*60
    working_sec = WORK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
    else:
        count_down(working_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = m.floor(count/60)
    count_sec = m.floor(count % 60)
    if 0 <= count_sec <= 9:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)
        print(count)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)


label = Label(text="Timer", font=(FONT_NAME, 25, "bold"), bg=YELLOW, fg=GREEN)
label.grid(column=2, row=0)

canvas = Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=2, row=1)


button1 = Button(text="Start", font=(FONT_NAME, 10), command=start_timer)
button1.grid(column=1, row=2)

button2 = Button(text="Reset", font=(FONT_NAME, 10))
button2.grid(column=3, row=2)

check_marks = Label(text="✔", fg=GREEN, font=(FONT_NAME, 20), bg=YELLOW)
check_marks.grid(column=2, row=4)


window.mainloop()







