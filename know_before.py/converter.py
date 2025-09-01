from tkinter import Button,Label,Tk,Entry

window = Tk()

window.minsize(width=400,height=300)

def convert(temp_c):
    temp_f =temp_c*(9//5)-32
    return temp_f

label = Label(fg="red",font=("Arial"),text="Enter the temperature in celcius:")
label.pack()

c=Entry(width=10,background="light green")
c.pack()

def button_clicked():
    label.config(text=convert(int(c.get())))

button = Button(text="Tap to convert",width=20,bg="orange",command=button_clicked)
button.pack()

window.mainloop()