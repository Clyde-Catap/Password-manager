from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_letters = []
    password_numbers = []
    password_symbols = []
    for x in range(5):
        gg = random.choice(letters)
        password_letters.append(gg)

    for y in range(4):
        gg = random.choice(numbers)
        password_numbers.append(gg)

    for z in range(3):
        gg = random.choice(symbols)
        password_symbols.append(gg)
    new = password_letters + password_numbers + password_symbols
    new_pass = ''.join(new)
    random.shuffle(new)
    password_entry.delete(0, END)
    password_entry.insert(0, new_pass)
    pyperclip.copy(new_pass)







# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    new_data = {
        website_entry.get().lower(): {
            "email": email_entry.get(),
            "password": password_entry.get()

        }

    }
    if len(password_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showwarning(message="Pleas dont leave any fields empty!")

    else:
        try:
            with open("new_passwords.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)
            with open("new_passwords.json", mode="w") as file:
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            with open("new_passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        finally:

            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    try:
        with open("new_passwords.json", mode="r") as file:
            data = json.load(file)
            email = data[f"{website_entry.get().lower()}"]["email"]
            password = data[f"{website_entry.get().lower()}"]["password"]
            website = website_entry.get().capitalize()
            messagebox.showinfo(title="Website Account", message=f"Website: {website} \n"
                                        f"Email: {email} \n"
                                        f"Password: {password} \n")
    except KeyError:
        messagebox.showwarning(message="No details for the website exists", title="Wrong Input")
    except FileNotFoundError:
        messagebox.showwarning(message="No Data File Found", title="No data saved")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)



canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=2, row=1)



webite_label = Label()
webite_label.config(text="Website:")
webite_label.grid(column=1, row=2)



email_label = Label()
email_label.config(text="Email/Username:")
email_label.grid(column=1, row=3)



password_label = Label()
password_label.config(text="Text:")
password_label.grid(column=1, row=4)



website_entry = Entry(width=52)
# website_entry.config(width=35, highlightthickness=0)
website_entry.grid(column=2, row=2, columnspan=2)
website_entry.focus()


email_entry = Entry(width=52)
email_entry.insert(0, "clydebryoncatap@gmail.com")
# email_entry.config(width=35, highlightthickness=0)
email_entry.grid(column=2, row=3, columnspan=2)



password_entry = Entry(width=52)
# password_entry.config(width=21, highlightthickness=0)
password_entry.grid(column=2, row=4, columnspan=2)



generate_button = Button(text="Generate Password", width=14, command=generate_password)
# generate_button.config(width=14, highlightthickness=0)
generate_button.grid(column=3, row=4)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=3, row=2)



add_button = Button(text="Add", width=44, command=add_password)
# add_button.config(width=35, highlightthickness=0)
add_button.grid(column=2, row=5, columnspan=2)









window.mainloop()