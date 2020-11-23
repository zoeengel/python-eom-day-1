# ZOE ENGEL, CLASS 1

from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Age Verification")
window.geometry("300x100")

# AGE LABEL AND ENTRY
age_lbl = Label(window, text="Enter your age:" , font=20)
age_entry = Entry(window, width=5)
age_lbl.pack(side=TOP)
age_entry.pack(side=TOP)

# AGE CHECKING FUNCTION
def ageCheck():
    age = int(age_entry.get())
    try:
         if age < 18:
             raise ValueError(messagebox.showinfo("ERROR","You need to be 18 years or older to play the lottery!"))
    except ValueError as e:
        print(e)
        age_entry.delete(0, END)
    else:
              messagebox.showinfo('Message',"Get ready to play the Lotto!")
              age_entry.delete(0, END)

# SUBMIT BUTTON
HEIGHT = 1
WIDTH = 12
submit_btn = Button(window, text="Submit", width=WIDTH, height=HEIGHT, command=ageCheck)
submit_btn.config(bg="orange")
submit_btn.pack(side=TOP)

window.mainloop()
