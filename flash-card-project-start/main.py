from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------- Load Data ----------
data = pandas.read_csv("flash-card-project-start\\data\\hindi.csv")
dict_data = data.to_dict(orient="records")
current_card = {}
flip_timer = None

# ---------- Flip Card Functions ----------
def flip_next():

    global current_card,flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    current_card = random.choice(dict_data)
    canvas1.itemconfig(card_background, image=front_image)
    canvas1.itemconfig(language, text="Hindi", fill="black")
    canvas1.itemconfig(word, text=current_card["Hindi"], fill="black")
    window.after(10000, show_translation)  # Flip after 3 seconds

def show_translation():
    canvas1.itemconfig(card_background, image=back_image)
    canvas1.itemconfig(language, text="English", fill="white")
    canvas1.itemconfig(word, text=current_card["English"], fill="white")

try:
    data = pandas.read_csv("flash-card-project-start/data/Words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("flash-card-project-start/data/hindi.csv")
    dict_data = original_data.to_dict(orient="records")

else:
    dict_data = data.to_dict(orient="records")
def is_known():
    dict_data.remove(current_card)  
    data = pandas.DataFrame(dict_data)
    data.to_csv("flash-card-project-start/data/Words_to_learn.csv",index=False)
    flip_next()



# ---------- UI Setup ----------
window = Tk()
window.title("Learn Hindi!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas1 = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="flash-card-project-start\\images\\card_front.png")
back_image = PhotoImage(file="flash-card-project-start\\images\\card_back.png")

card_background = canvas1.create_image(400, 263, image=front_image)
language = canvas1.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas1.create_text(400, 263, text="", font=("Ariel", 55, "bold"))
canvas1.grid(column=1, row=1, columnspan=2)

# ---------- Buttons ----------
right_image = PhotoImage(file="flash-card-project-start\\images\\right.png")
buttonr = Button(image=right_image, highlightthickness=0, command=is_known)
buttonr.grid(column=1, row=2)

wrong_image = PhotoImage(file="flash-card-project-start\\images\\wrong.png")
buttonw = Button(image=wrong_image, highlightthickness=0, command=show_translation)
buttonw.grid(column=2, row=2)

skip_button = Button(text="SKIP=>",width=10, command=flip_next,background="black",fg="white",font=("Roboto",20,"bold"))
skip_button.grid(column=1, row=3, columnspan=2)


# ---------- Start ----------
flip_next()
window.mainloop()
