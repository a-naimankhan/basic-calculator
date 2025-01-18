from tkinter import *

root = Tk()
root.geometry("265x400")
root.title("Калькулятор")
root.config(background="black")

expression = ""


result = StringVar()
expression_field = Entry(root, textvariable=result, justify='left', font=('Arial', 16))
expression_field.grid(columnspan=4, ipadx=10, ipady=10, padx=10, pady=10)

def press_num(num):
    global expression 
    expression += str(num)
    result.set(expression)

def equal_press():
    try:
        global expression
        total=str(eval(expression))
        result.set(total)
        expression = ""
    except:
        result.set("error")
        expression = ""

class bits:
    def to_bin():
        global expression
        try:
            
            total = bin(int(expression))[2:]  
            result.set(total)
            expression = ""
        except:
            result.set("error")
            expression = ""
        
    def to_oct():
        global expression
        try:
        
            total = oct(int(expression))[2:]  
            result.set(total)
            expression = ""
        except:
            result.set("error")
            expression = ""

    def to_dec():
        global expression
        try:
            
            total = str(int(expression))
            result.set(total)
            expression = ""
        except:
            result.set("error")
            expression = ""

    def to_hex():
        global expression
        try:
        
            total = hex(int(expression))[2:].upper() 
            result.set(total)
            expression = ""
        except:
            result.set("error")
            expression = ""

    def to_reset():
        global expression
        total = ""
        result.set(total)
        expression = ""


class buttons:

    button1 = Button(root, text="1", height=2, width=5 , command=lambda: (press_num(1)) , background="darkgray")
    button1.grid(row=3, column=0, padx=4, pady=4)

    button2 = Button(root, text="2", height=2, width=5 , command=lambda: (press_num(2)) , background="darkgray")
    button2.grid(row=3, column=1, padx=4, pady=4)

    button3 = Button(root, text="3", height=2, width=5 , command=lambda: (press_num(3)) , background="darkgray")
    button3.grid(row=3, column=2, padx=4, pady=4)

    button4 = Button(root, text="4", height=2, width=5 , command=lambda: (press_num(4)) , background="darkgray")
    button4.grid(row=4, column=0, padx=4, pady=4)

    button5 = Button(root, text="5", height=2, width=5 , command=lambda: (press_num(5)) , background="darkgray")
    button5.grid(row=4, column=1, padx=4, pady=4)

    button6 = Button(root, text="6", height=2, width=5 , command=lambda: (press_num(6)) , background="darkgray") 
    button6.grid(row=4, column=2, padx=4, pady=4)

    button7 = Button(root, text="7", height=2, width=5 , command=lambda: (press_num(7)) , background="darkgray")
    button7.grid(row=5, column=0, padx=4, pady=4)

    button8 = Button(root, text="8", height=2, width=5 , command=lambda: (press_num(8)) , background="darkgray")
    button8.grid(row=5, column=1, padx=4, pady=4)

    button9 = Button(root, text="9", height=2, width=5 , command=lambda: (press_num(9)) , background="darkgray")
    button9.grid(row=5, column=2, padx=4, pady=4)

    plus = Button(root, text="+", height=2, width=5 , command=lambda: (press_num("+")) , background="yellow")
    plus.grid(row=5, column=3, padx=4, pady=4)

    button0 = Button(root, text="0", height=2, width=5 , command=lambda: (press_num(0)) , background="darkgray")
    button0.grid(row=6, column=1, padx=4, pady=4)

    minus = Button(root, text="-", height=2, width=5 , command=lambda: (press_num("-"))  , background="yellow")
    minus.grid(row=4, column=3, padx=4, pady=4)

    equal = Button(root, text="=", height=2, width=5 , command=equal_press , background="yellow")
    equal.grid(row=6, column=3, padx=4, pady=4)

    multiply = Button(root, text="*", height=2, width=5 , command=lambda: (press_num("*")) , background="yellow" )
    multiply.grid(row=3, column=3, padx=4, pady=4)

    divide = Button(root, text="/", height=2, width=5 , command=lambda: (press_num("/"))  , background="yellow")
    divide.grid(row=2, column=3, padx=4, pady=4)

    binary = Button(root, text="BIN", height=2, width=5 , command=bits.to_bin , background= "gray" )
    binary.grid(row=7, column=0, padx=4, pady=4)

    octal = Button(root, text="OCT", height=2, width=5 , command=bits.to_oct , background= "gray")
    octal.grid(row=7, column=1, padx=4, pady=4)

    decimal = Button(root, text="DEC", height=2, width=5 , command=bits.to_dec , background= "gray" )
    decimal.grid(row=7, column=2, padx=4, pady=4) 

    Hexadecimal = Button(root, text="HEX", height=2, width=5 , command=bits.to_hex  , background= "gray" )
    Hexadecimal.grid(row=7, column=3, padx=4, pady=4)

    reset = Button(root, text="C", height=2, width=5 , command= bits.to_reset  , background="lightgrey")
    reset.grid(row=2, column=0, padx=4, pady=4)


root.mainloop()
