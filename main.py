from tkinter import *
import math

#SetUp
calc = Tk()
calc.title("CASIO")
calc.geometry("440x450+0+0")
calc.configure(bg="aquamarine3")


#Entry Widget
en = Entry(calc, width=35, borderwidth=5, bg ="white", fg = "black")
en.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

#functions
def button_click(number): 
    current = en.get()
    en.delete(0, END)
    en.insert(0, str(current) + str(number))

def b_del():
    en.delete(0, END)

def b_add():
    first_number = en.get()
    global f_num 
    global math
    math = "Addation"
    f_num = int(first_number)
    en.delete(0, END) 

def b_minus():
    first_number = en.get()
    global f_num 
    global math
    math = "Subtraction"
    f_num = int(first_number)
    en.delete(0, END) 

def b_multiply():
    first_number = en.get()
    global f_num 
    global math
    math = "Multiplication"
    f_num = int(first_number)
    en.delete(0, END) 

def b_divide():
    first_number = en.get()
    global f_num 
    global math
    math = "Division"
    f_num = int(first_number)
    en.delete(0, END) 

def b_Square():
    first_number = en.get()
    k = int(first_number) 
    en.delete(0, END) 
    en.insert(0, k*k)

def b_Squareroot():
    first_number = en.get()
    k = int(first_number)
    en.delete(0, END) 
    en.insert(0, math.sqrt(int(k)))
   
def b_power():
    first_number = en.get()
    global f_num 
    global math
    math = "Power"
    f_num = int(first_number)
    en.delete(0, END) 

def b_equal():
    second_number = en.get()
    global s_nur
    s_nur = second_number
    en.delete(0, END)
    if math == "Addation":
        en.insert(0, f_num + int(second_number))
    if math == "Subtracton":
        en.insert(0, f_num - int(second_number))
    if math == "Division":
        en.insert(0, f_num / int(second_number))
    if math == "Multiplication":
        en.insert(0, f_num * int(second_number))
    if math == "Power":
        pow = str(f_num) * int(second_number)
        for i in pow:
            int(i)
            j = i + i
        en.insert(0, j)

def b_Sin():
    return

b7= Button(calc, text="7", padx=40, pady=20, bg='aquamarine1', fg='black', command=lambda: button_click(7))
b8= Button(calc, text="8",padx=40, pady=20, command=lambda: button_click(8))
b9= Button(calc, text="9",padx=40, pady=20, command=lambda: button_click(9))

b6= Button(calc, text="6",padx=40, pady=20, command=lambda: button_click(6))
b5= Button(calc, text="5",padx=40, pady=20, command=lambda: button_click(5))
b4= Button(calc, text="4",padx=40, pady=20, command=lambda: button_click(4))

b3= Button(calc, text="3",padx=40, pady=20, command=lambda: button_click(3))
b2= Button(calc, text="2",padx=40, pady=20, command=lambda: button_click(2))
b1= Button(calc, text="1",padx=40, pady=20, command=lambda: button_click(1))

b0 = Button(calc, text="0",padx=40, pady=20, command=lambda: button_click(0))
b_plus = Button(calc, text="+",padx=40, pady=20, command=b_add)
b_minus = Button(calc, text="-",padx=40, pady=20, command=b_minus)

b_multi= Button(calc, text="x",padx=40, pady=20, command=b_multiply)
b_div= Button(calc, text="/",padx=40, pady=20, command=b_divide)
b_equals= Button(calc, text="=",padx=40, pady=20, command=b_equal)

b_deci = Button(calc, text=".",padx=40, pady=20)
b_del = Button(calc, text="Del", padx=40, pady=20, command=b_del)

b_SIN= Button(calc, text="SIN",padx=40, pady=20, command=b_Sin)
b_COS= Button(calc, text="COS",padx=40, pady=20)
b_TAN= Button(calc, text="TAN",padx=40, pady=20)

b_SQUARE = Button(calc, text="A*A",padx=40, pady=20, command=b_Square)
b_SQUAREROOT = Button(calc, text="Sqrt", padx=40, pady=20, command=b_Squareroot)

b_Raised = Button(calc, text="A^n",padx=40, pady=20, command=b_power)
b_Exit = Button(calc, text="Exit", padx=40, pady=20)

#Put the buttons on the screen
b7.grid(column=0, row=1)
b8.grid(column=1, row=1)
b9.grid(column=2, row=1)

b6.grid(column=0, row=2)
b5.grid(column=1, row=2)
b4.grid(column=2, row=2)

b3.grid(column=0, row=3)
b2.grid(column=1, row=3)
b1.grid(column=2, row=3)

b0.grid(column=0, row=4)
b_plus.grid(column=1, row=4)
b_minus.grid(column=2, row=4)

b_multi.grid(column=0, row=5)
b_div.grid(column=1, row=5)
b_equals.grid(column=1, row=6)

b_deci.grid(column=0, row=6)
b_del.grid(column=2, row=6)

b_SIN.grid(column=3, row=1)
b_COS.grid(column=3, row=2)
b_TAN.grid(column=3, row=3)

b_SQUARE.grid(column=2, row=5)
b_SQUAREROOT.grid(column=3, row=4)
b_Raised.grid(column=3, row=5)

b_Exit.grid(column=3, row=6)


calc.mainloop()