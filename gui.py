from tkinter import *

root = Tk()

# create entry widget
entry = Entry(root, width=50, borderwidth=4)
entry.pack()
entry.get()

def myClick():
    myLabel = Label(root, text="The button has been clicked!")
    myLabel.pack()

# myButton = Button(root, text="Click me!", state=DISABLED)
myButton = Button(root, text="Enter any string", padx=50, command=myClick, fg="blue", bg="cyan")
myButton.pack()

# run event loop
root.mainloop()