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
reps = 0 
reset = "None"
mark = ""
## change Godgive computer to the name of your administrator or user name, or if using pycharm, simply use the filename without the directory
filename = "images/tomato.png"
# ---------------------------- TIMER RESET ------------------------------- # 

def resettimer():
    global reps
    window.after_cancel(reset)
    reps = 0
    timer.config(text="Timer")
    canvas.itemconfig(timer_text, text= "00:00")
    pom_checkmark.config(text=" ")
    
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def Starttimer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    shortbreaksec = SHORT_BREAK_MIN * 60
    longbreaksec = LONG_BREAK_MIN * 60
    
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        timer.config(text="Coding", fg=RED)
    elif reps % 2 == 0:
        count_down(shortbreaksec)
        timer.config(text="Break", fg=GREEN)
    elif reps % 8 == 0:
        count_down(longbreaksec)
        timer.config(text="Long Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00" 
        
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        global reset
        reset = window.after(1000, count_down, count - 1)
    else:
        Starttimer()
        global mark
        for _ in range(math.floor(reps / 2)):
            mark += "✓"
        pom_checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
##window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLUEBLACK)
icon = "images/icon.png"
appicon = PhotoImage(file=icon)
window.iconphoto(False, appicon)

    
##label
tomato_pic = PhotoImage(file=filename)
timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 34, "normal"), bg=BLUEBLACK, highlightthickness=0)
timer.grid(column=1, row=0)

start_timer = Button(text="Start", font=(FONT_NAME, 14, "normal"), fg=GREEN, bg=BLUEBLACK, highlightthickness=0, command=Starttimer)
start_timer.grid(column=0, row=2)

reset_timer = Button(text="Reset", font=(FONT_NAME, 14, "normal"), fg=GREEN, bg=BLUEBLACK, highlightthickness=0, command=resettimer)
reset_timer.grid(column=2, row=2)

pom_checkmark = Label(fg=GREEN, bg=BLUEBLACK, highlightthickness=0)
pom_checkmark.grid(column=1, row=3)
##canvas
canvas = Canvas(width=200, height=224, bg=BLUEBLACK, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_pic)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)




window.mainloop()   
