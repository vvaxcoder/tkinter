from tkinter import *

root = Tk()

# Create a Label widget
myLabel1 = Label(root, text="Label 1")
myLabel2 = Label(root, text="Label2")

# Showing it onto the screen
# myLabel.pack()
# run event loop

#use grid system
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

root.mainloop()