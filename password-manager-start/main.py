from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!','@','#','$','%','^','&','*','_','~','-','+']
file_address = "password-manager-start\\data_stored.json"

def password_generator():

    letters_list = [random.choice(letters) for _ in range(4)]
    number_list = [str(random.choice(numbers)) for _ in range(3)]
    symbols_list = [random.choice(symbols) for _ in range(2)]

    passw = letters_list + number_list + symbols_list

    passwo = "".join(passw)
    pass_e.delete(0,END)
    pass_e.insert(0,passw)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = web_entry.get()
    email = email_e.get()
    passw = pass_e.get()

    new_data = {
        website:{
            "email": email,
            "password" : passw
        }
    }

    if passw=="" or website==''or email=='':
        messagebox.showinfo(title="TRY AGAIN!❌🚫",message="Please make sure that you have entered all the required information‼️")
    else:   
        is_ok = messagebox.askokcancel(title="CONFORMATION",message=f"These are the details you have entered:\nEmail : {email}\nUsername/E-mail: {email}\nPassword : {passw}\nIS THIS OKAY TO SAVE!")

        if is_ok:
            try:
            #In read mode
                with open(file_address,"r") as saving:

                        #Reading the old data
                    data = json.load(saving)

            except FileNotFoundError:
                    with open(file_address,"w") as saving:
                        json.dump(new_data,saving,indent=4)   #data.update <<<<SEE CAREFULLY>>>>
            
            else:
                with open(file_address,"w") as saving:
                    #Updating the data
                    data.update(new_data)
                    #saving the data
                    json.dump(data,saving,indent=4)   #json.dump <<<<SEE CAREFULLY>>>
                 
            finally:   
                #DELETING THINGS AFTER SAVING THE PASSWORD
                web_entry.delete(0,END)
                pass_e.delete(0,END)
        
        else:
            web_entry.delete(0,END)
            pass_e.delete(0,END)

# ---------------------------- SEARCHING ------------------------------- #


def search_command():
    with open(file_address,"r") as saving:

        content = json.load(saving)
        c = content[web_entry.get()]
        # print(content[web_entry.get()])
        if c:
            messagebox.showinfo(title=web_entry.get(),message=f"Username/Email: {c["email"]} \n\nPassword:{c['password']}")
        else:
            messagebox.showerror(title="Oops", message="No details for this website found.")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PASSWORD GENERATOR")
window.config(padx=50,pady=50,background="#007fff")


canvas = Canvas(height=200,width=200,highlightthickness=0)
pic = PhotoImage(file="password-manager-start/logo.png")
canvas.create_image(97,90,image=pic)
canvas.grid(column=2,row=1)

#WEBSITE NAME
web_name = Label(text="Website:",font=("Roboto",10,"bold"),highlightthickness=0)
web_name.grid(column=1,row=2)

search = Button(width=7,text="Search",command=search_command)
search.grid(column=3,row=2)

web_entry = Entry(width=31)
web_entry.grid(column=2,row=2,columnspan=1)
web_entry.focus()

# EMAIL OR USERNAME
email_or_user = Label(text="Email/Username:",font=("Roboto",10,"bold"),highlightthickness=0)
email_or_user.grid(row=3,column=1)

email_e = Entry(width=43)
email_e.grid(column=2,row=3,columnspan=2)
email_e.insert(END,"ankitha@gmail.com")

#PASSWORD
password = Label(text="Password:",font=("Roboto",10,"bold"),highlightthickness=0)
password.grid(column=1,row=4)

pass_e = Entry(width=33)
pass_e.grid(column=2,row=4,columnspan=1)

generator = Button(width=7,text="Generate",bg="blue",fg="white",command=password_generator)
generator.grid(column=3,row=4)

#ADD
add = Button(width=37,text="Add",bg="green",fg="white",command=save)
add.grid(column=2,row=5,columnspan=2)


window.mainloop()