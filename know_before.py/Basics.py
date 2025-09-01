from tkinter import Button,Label,Tk,Entry,Text

window = Tk()
'''Set min WIDTH and HEIGHT for this widget.
 If the window is gridded the values are given in grid units.
 Return the current values if None is given.'''
window.minsize(300,300)
window.title("My First GUI Program")
# window.mainloop() #while Ture: kinda(listening) 
# lable
my_lable = Label(text="I am Label", font=("Times New Roman", 16,"italic"),fg="blue")
#alone this line will not print or will be visible , anywhere in the screen
#unless the .pack() is called. the lable will get printed at the center by default
my_lable.pack()


#TO UPDATE OR CHANGE THE TEXT
# my_lable["text"] = "Updated...!"
#       or
# my_lable.config(text = "New text")

ip = Entry(width=30,background="yellow")
# ip.get()
ip.pack()

#BUTTON
def botton_clicked():
        my_lable.config(text = ip.get())

button = Button(text="Here!!",fg="pink",bg="black",command=botton_clicked)  #No parenthsis to call the function
button.pack()

#CHECKBUTTON


window.mainloop()