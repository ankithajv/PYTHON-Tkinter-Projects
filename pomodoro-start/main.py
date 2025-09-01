from tkinter import *
import math
from tkinter import messagebox
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Roboto"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
time_s=None

mark =""

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():
    window.after_cancel(time_s)
    #timer_text 00:00

    canvas.itemconfig(timer_text,text="00:00")

    #title_lable = "Timer"
    timer.config(text="Timer",fg="black")

    #reset check_marks
    check.config(text = "")

    #reps should be 0
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    reps+=1
    work = WORK_MIN*60
    s_break = SHORT_BREAK_MIN*60
    l_break = LONG_BREAK_MIN*60

    if reps%2==0:
        timer.config(text="SHORT BREAK",fg=PINK)
        countdown(s_break)

    elif reps%8==0:
        countdown(l_break)
        timer.config(text="LONG BREAK",fg=RED)
    
    else:
        countdown(work)
        timer.config(text="WORKING TIME",fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):

        count_min = math.floor(count / 60)
        count_sec = count % 60

        if count_sec<10:
            count_sec = f"0{count_sec}"

        canvas.itemconfig(timer_text,text=(f"{count_min}:{count_sec}"))


        if count>0:
            global time_s
            time_s = window.after(1000,countdown,count-1)  #to stop or start timer
        
        else:
            start_count()
            global mark
            work_sessions = math.floor(reps/2)
            for _ in range(work_sessions):
                mark+="✔"
                check.config(text=mark)
                 


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Tomato Reminds!")
window.config(padx=90,pady=50,bg=YELLOW)

timer = Label(text="Timer",font=(FONT_NAME,30),bg=YELLOW)
timer.grid(column=2,row=1)


canvas = Canvas(height=200,width=224,background=YELLOW,highlightthickness=0)
p = PhotoImage(file="C:\\Users\\ANKITHA JV\\Downloads\\tkinter\\pomodoro-start\\tomato.png")
canvas.create_image(100,87,image = p)

timer_text = canvas.create_text(105,105,text ="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)

start = Button(width=10,text="Start",command=start_count)
start.grid(row=3,column=1)

reset = Button(width=10,text="Reset",command=timer_reset)
reset.grid(column=3,row=3)

check = Label(fg=GREEN,bg=YELLOW,background=YELLOW,font=(30))
check.grid(row=4,column=2)


window.mainloop()