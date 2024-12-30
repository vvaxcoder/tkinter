import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def handle_convert():
    miles_input = entry_val.get()
    km_output = miles_input * 1.61
    output_string.set(km_output)


# window
# window = tk.Tk()
# window = ttk.Window(themename='journal')
window = ttk.Window(themename='darkly')
window.title('Demo')
window.geometry('400x200')

# title
title_label = ttk.Label(master=window,
                        text='Miles to kilometers',
                        font='Calibri 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_val = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_val)
button = ttk.Button(master=input_frame, text='Convert', command=handle_convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window,
                         text='Output',
                         font='Calibri 20',
                         textvariable=output_string)
output_label.pack(pady=5)

# run
window.mainloop()
