from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

lab1 = Label(text="is equal to")
lab1.grid(column=1,row=2)

entry = Entry(width=15)
entry.grid(row=1,column=2)

lab2 = Label(text="0")
lab2.grid(column=2,row=2)

def but_cl():
    miles = float(entry.get())
    km = round(miles * 1.609, 2)
    lab2.config(text=str(km))

botton = Button(text="Caluclate",command=but_cl)
botton.grid(row=3,column=2)

lab3 = Label(text="Miles")
lab3.grid(column=3,row=1)

lab4 = Label(text="Km")
lab4.grid(column=3,row=2)

window.mainloop()