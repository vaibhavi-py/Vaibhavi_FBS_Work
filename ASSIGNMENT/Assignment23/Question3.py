from tkinter import *

def calculate():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        op = operator.get()

        if op == "+":
            result = n1 + n2
        elif op == "-":
            result = n1 - n2
        elif op == "*":
            result = n1 * n2
        elif op == "/":
            result = n1 / n2

        label_result.config(text="Result: " + str(result))

    except:
        label_result.config(text="Invalid Input")


root = Tk()
root.title("Basic Calculator")
root.geometry("300x250")

Label(root, text="Enter First Number").pack()
entry1 = Entry(root)
entry1.pack()

Label(root, text="Enter Second Number").pack()
entry2 = Entry(root)
entry2.pack()

Label(root, text="Select Operator").pack()
operator = StringVar(root)
operator.set("+")
OptionMenu(root, operator, "+", "-", "*", "/").pack()

Button(root, text="Calculate", command=calculate).pack(pady=10)

label_result = Label(root, text="")
label_result.pack()

root.mainloop()