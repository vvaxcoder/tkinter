from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="The button has been clicked!")
    myLabel.pack()

# myButton = Button(root, text="Click me!", state=DISABLED)
myButton = Button(root, text="Click me!", padx=50, command=myClick)
myButton.pack()

# run event loop
root.mainloop()