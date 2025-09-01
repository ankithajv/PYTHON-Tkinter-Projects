#PACK
'''Little complicated to place the things, 
to place them at an exact position where we need.
the things can be at center,left,right,top bottom.'''

#PLACE
'''will take x,y co-ordinates.'''

#GRID
'''Works on coloumn and row.Prefered'''

##***Grid is not compatible with pack and palce***#


from tkinter import *

#padding>>> BORDER

tik = Tk()
tik.minsize(300,300)

tik.config(padx=20,pady=20)

entry = Entry(width=30)
entry.grid(column=3,row=2)

my_label = Label(text="LABEL")
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)


button = Button(width=20,bg="green")
button.grid(column=1,row = 1)

button2 = Button(bg="red")
button2.grid(column=2,row=0)



tik.mainloop()





