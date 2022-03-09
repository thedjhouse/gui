
from tkinter import *
 

app = Tk()
 

def which_button(button_press):
    print(button_press)
 
 
# 
b1 = Button(app, text="Apple",
            command=lambda m="It is an apple": which_button(m),
            foreground="red",
            background="black",
            borderwidth=0)
 
b1.grid(padx=10, pady=10)

t1 = Text(app, text="Dit is mijn prachtige knop", foreground="#474444")

app.mainloop()