from curses import BUTTON1_PRESSED
import tkinter as w

class test():

    def which_button(button_press):
        print (button_press)

window = w.Tk()
label = w.Label(
    text="Hello!",
    foreground="white",
    background="black",
    width=10,
    height=10
)
label.pack()

button = w.Button(
    text="This is the N buttton",
    foreground="white",
    background="orange",
)
button.pack()

if button == True:
    print("Button has been pressed")
w.mainloop()