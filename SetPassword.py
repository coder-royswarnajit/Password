from tkinter import * #type:ignore
import re
from tkinter import messagebox

root=Tk()
root.title("SET PASSWORD")
root.geometry("200x150")


def check_password_strength():
    password = password_entry.get()
    #if len(password) <= 16 and len(password)>=8:
       # messagebox.showwarning("Result", "Weak password. Please Choose a Password with at least 16 Characters.")
    if not re.search(r"[A-Z]", password):
        messagebox.showwarning("Result", "Weak password. Please Choose a Password with at least One Capital Letters.")
    if not re.search(r"[a-z]", password) :
        messagebox.showwarning("Result", "Weak password. Please Choose a Password with at least One Small Letters.")
    if not re.search(r"\d", password):
        messagebox.showwarning("Result", "Weak password. Please Choose a Password which contain Numbers.")
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\/\-]", password):
        messagebox.showwarning("Result", "Weak password. Please choose a password with at least contain a Special Character")
    else:
        messagebox.showinfo("Result", "Strong password! Good job.")


# Create a label and an entry widget for password input
password_label = Label(root, text="Set A Password")
password_label.pack()
password_entry = Entry(root)  # Use show="*" to hide the password
password_entry.pack()

# Create a button to check the password strength
check_button = Button(root, text="Check Strength", command=check_password_strength)
check_button.pack()





mainloop()