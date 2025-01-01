import tkinter as tk
from tkinter import ttk


def button_func(arg=None):
    # print(button.configure())
    if arg == 'test':
        print('hello')
    else:
        print('Button was pressed')

    string_var.set('string_var was rewritten')
    window.quit()


# create a window
window = tk.Tk()
window.title('window and Widgets')
window.geometry('800x700')

# create widgets
tk.Text(master=window).pack()

# ttk widgets
label = ttk.Label(master=window)
label.pack()

# tkinter variable
string_var = tk.StringVar(value='This should be default value')

# ttk entry
entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

label_test = ttk.Label(master=window, textvariable=string_var)
label_test.pack()

# button_test = ttk.Button(master=window, text='Execute test button', command=button_func('test'))
button_test = ttk.Button(master=window, text='Execute test button', command=lambda: print('hello'))
button_test.pack()

# ttk button
button = ttk.Button(master=window, text='Execute', command=button_func)
button.pack()

# run
window.mainloop()
