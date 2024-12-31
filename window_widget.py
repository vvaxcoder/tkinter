import tkinter as tk
from tkinter import ttk


def button_func(arg):
    if arg == 'test':
        print('hello')
    else:
        print('Button was pressed')


# create a window
window = tk.Tk()
window.title('window and Widgets')
window.geometry('800x700')

# create widgets
tk.Text(master=window).pack()

# ttk widgets
label = ttk.Label(master=window)
label.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

label_test = ttk.Label(master=window, text='Test label')
label_test.pack()

# button_test = ttk.Button(master=window, text='Execute test button', command=button_func('test'))
button_test = ttk.Button(master=window, text='Execute test button', command=lambda: print('hello'))
button_test.pack()

# ttk button
button = ttk.Button(master=window, text='Execute', command=button_func)
button.pack()

# run
window.mainloop()
