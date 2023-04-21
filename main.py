from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUEBLACK = "#070A52"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
filename = "/Users/Godgive Computer/PycharmProjects/day 28 projects/tomato.png"
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def Starttimer():
    count_down(WORK_MIN * 60)


def resetTimer():
    pass

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
##window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLUEBLACK)

    
##label
tomato_pic = PhotoImage(file=filename)
timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 34, "normal"), bg=BLUEBLACK, highlightthickness=0)
timer.grid(column=1, row=0)

start_timer = Button(text="Start", font=(FONT_NAME, 14, "normal"), fg=GREEN, bg=BLUEBLACK, highlightthickness=0, command=Starttimer)
start_timer.grid(column=0, row=2)

reset_timer = Button(text="Reset", font=(FONT_NAME, 14, "normal"), fg=GREEN, bg=BLUEBLACK, highlightthickness=0)
reset_timer.grid(column=2, row=2)

pom_checkmark = Label(text="✓", fg=GREEN, bg=BLUEBLACK, highlightthickness=0)
pom_checkmark.grid(column=1, row=3)
##canvas
canvas = Canvas(width=200, height=224, bg=BLUEBLACK, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)




window.mainloop()   
