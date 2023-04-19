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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
##window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLUEBLACK)
tomato_pic = PhotoImage(file=filename)
##label
timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 34, "normal"), bg=BLUEBLACK, highlightthickness=0)
timer.grid(column=1, row=0)

start_timer = Button(text="Start", font=(FONT_NAME, 14, "normal"), fg=GREEN, bg=BLUEBLACK, highlightthickness=0)
start_timer.grid(column=0, row=2)

reset_timer = Button(text="Reset", font=(FONT_NAME, 14, "normal"), fg=GREEN, bg=BLUEBLACK, highlightthickness=0)
reset_timer.grid(column=2, row=2)

pom_checkmark = Label(text="✓", fg=GREEN, bg=BLUEBLACK, highlightthickness=0)
pom_checkmark.grid(column=1, row=3)
##canvas
canvas = Canvas(width=200, height=224, bg=BLUEBLACK, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_pic)
canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()
