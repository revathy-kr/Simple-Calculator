from tkinter import *

expression = ""
# Function to update expressiom in the text entry box
def press(num):
    global expression
    # concatenation of string
    expression = expression + str(num)
    # update the expression by using set method
    equation.set(expression)
def equalpress():
    try:
        global expression
        # eval function evaluate the expression and str function convert the result into string
        total = str(eval(expression))
        equation.set(total)
        # initialze the expression variable by empty string
        expression = ""
    except:
        equation.set(" error ")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")

window = Tk()
window.title("CALCULATOR")
equation = StringVar()
expression_field = Entry(window, textvariable=equation)
expression_field.grid(columnspan=10, ipadx=150, ipady=25)
equation.set('0')

Button(window, text="0",fg='black', bg='grey',height=1, width=7,command=lambda: press(0)).grid(column=6, row=4,ipadx=5,ipady=10)
Button(window, text="1",fg='black', bg='grey',height=1, width=7,command=lambda: press(1)).grid(column=0, row=2,ipadx=5,ipady=10)
Button(window, text="2",fg='black', bg='grey',height=1, width=7,command=lambda: press(2)).grid(column=1, row=2,ipadx=5,ipady=10)
Button(window, text="3",fg='black', bg='grey',height=1, width=7,command=lambda: press(3)).grid(column=2, row=2,ipadx=5,ipady=10)
Button(window, text="4",fg='black', bg='grey',height=1, width=7,command=lambda: press(4)).grid(column=0, row=3,ipadx=5,ipady=10)
Button(window, text="5",fg='black', bg='grey',height=1, width=7,command=lambda: press(5)).grid(column=1, row=3,ipadx=5,ipady=10)
Button(window, text="6",fg='black', bg='grey',height=1, width=7,command=lambda: press(6)).grid(column=2, row=3,ipadx=5,ipady=10)
Button(window, text="7",fg='black', bg='grey',height=1, width=7,command=lambda: press(7)).grid(column=0, row=4,ipadx=5,ipady=10)
Button(window, text="8",fg='black', bg='grey',height=1, width=7,command=lambda: press(8)).grid(column=1, row=4,ipadx=5,ipady=10)
Button(window, text="9",fg='black', bg='grey',height=1, width=7,command=lambda: press(9)).grid(column=2, row=4,ipadx=5,ipady=10)
Button(window, text="CLEAR",fg='black', bg='grey',height=1, width=7,command=clear).grid(column=7, row=4,ipadx=40,ipady=10,columnspan=2)
Button(window, text="+",fg='black', bg='grey',height=1, width=7,command=lambda: press('+')).grid(column=6, row=2,ipadx=5,ipady=10)
Button(window, text="-",fg='black', bg='grey',height=1, width=7,command=lambda: press('-')).grid(column=7, row=2,ipadx=5,ipady=10)
Button(window, text="*",fg='black', bg='grey',height=1, width=7,command=lambda: press('*')).grid(column=8, row=2,ipadx=5,ipady=10)
Button(window, text="/",fg='black', bg='grey',height=1, width=7,command=lambda: press('/')).grid(column=6, row=3,ipadx=5,ipady=10)
Button(window, text=".",fg='black', bg='grey',height=1, width=7,command=lambda: press('.')).grid(column=7, row=3,ipadx=5,ipady=10)
Button(window, text="=",fg='black', bg='grey',height=1, width=7,command=lambda: equalpress()).grid(column=8, row=3,ipadx=5,ipady=10)

window.mainloop()