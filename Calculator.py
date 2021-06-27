# Establish needed modules
from tkinter import *
from tkinter import font as tkFont

# Establish root and title
root = Tk()
root.title("Simple Calculator")

# Font options
helv36 = tkFont.Font(family='Helvetica', size=12, weight='bold')

# Establish entry widget
e = Entry(root, width=35, borderwidth=2, font=helv36)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Click function
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# Clear function
def button_clear():
    e.delete(0, END)


# Equal function
def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == 'addition':
        e.insert(0, f_num + float(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - float(second_number))
    if math == 'multiply':
        e.insert(0, f_num * float(second_number))
    if math == 'division':
        e.insert(0, f_num / float(second_number))


# Addition function
def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = float(first_number)
    e.delete(0, END)


# Subtract function
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = float(first_number)
    e.delete(0, END)


# Multiply function
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiply'
    f_num = float(first_number)
    e.delete(0, END)


# Divide function
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first_number)
    e.delete(0, END)


# 1/x function
def button_over():
    number = e.get()
    e.delete(0, END)
    e.insert(0, 1 / float(number))


# Squared function
def button_squared():
    number = e.get()
    e.delete(0, END)
    e.insert(0, float(number)**2)


# Establish buttons
button_1 = Button(root, text='1', padx=40, pady=20, font=helv36, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, font=helv36, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, font=helv36, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, font=helv36, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, font=helv36, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, font=helv36, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, font=helv36, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, font=helv36, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, font=helv36, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, font=helv36, command=lambda: button_click(0))
button_dec = Button(root, text='.', padx=42, pady=20, font=helv36, command=lambda: button_click('.'))

button_over = Button(root, text='1/x', padx=34, pady=20, font=helv36, command=button_over)
button_squared = Button(root, text='x^2', padx=32, pady=20, font=helv36, command=button_squared)
button_add = Button(root, text='+', padx=40, pady=20, font=helv36, command=button_add)
button_equal = Button(root, text='=', padx=97, pady=20, font=helv36, command=button_equal)
button_subtract = Button(root, text='—', padx=36, pady=20, font=helv36, command=button_subtract)
button_multiply = Button(root, text='x', padx=40, pady=20, font=helv36, command=button_multiply)
button_divide = Button(root, text='÷', padx=40, pady=20, font=helv36, command=button_divide)
button_clear = Button(root, text='CLEAR', padx=74, pady=20, font=helv36, command=button_clear)

# Put buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

button_over.grid(row=4, column=1)
button_squared.grid(row=4, column=2)
button_0.grid(row=4, column=0)


button_subtract.grid(row=6, column=0)
button_clear.grid(row=6, column=1, columnspan=2)

button_dec.grid(row=7, column=0)
button_equal.grid(row=7, column=1, columnspan=2)

# End root loop
root.mainloop()
