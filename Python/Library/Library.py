#MATH LIBRARY
import operator as oper
#GRAPHIC INTERFACE
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

#principal
def principal():
    op = simpledialog.askinteger('Basic Calculator','''
    1. Sum
    2. Subtraction
    3. Multiplication
    4. Integer division
    5. Residue
    6. Power
    7. Division
    8. Base change
    9. End
    Enter an option: ''')
    while oper.lt(op,1) or oper.gt(op,9):
        messagebox.showwarning(message='Please enter a valid option',title='')
        op = simpledialog.askinteger('Basic Calculator','''
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Integer division
        5. Residue
        6. Power
        7. Division
        8. Base change
        9. End
        Enter an option: ''')
    while oper.ne(op,9):
        n1= simpledialog.askinteger('', 'Type n1: ')
        n2= simpledialog.askinteger('', 'Type n2: ')
        if oper.eq(op,1):
            a = add(n1,n2)
            answer = str(n1)+' + '+str(n2)+' = '+str(a)

        elif oper.eq(op,2):
            a = substract(n1,n2)
            answer = str(n1)+' - '+str(n2)+' = '+str(a)

        elif oper.eq(op,3):
            a = multiply(n1,n2)
            answer = str(n1)+' * '+str(n2)+' = '+str(a)

        elif oper.eq(op,4):
            a = intDivision(n1,n2)
            answer = str(n1)+' // '+str(n2)+' = '+str(a)

        elif oper.eq(op,5):
            while n1 < 0:
                messagebox.showwarning(message='You must enter a positive number',title='')
                n1= simpledialog.askinteger('', 'Type n1: ')
            while n2<0:
                messagebox.showwarning(message='You must enter a positive number',title='')
                n2= simpledialog.askinteger('', 'Type n2: ')
            a = residue(n1,n2)
            answer = str(n1)+' % '+str(n2)+' = '+str(a)

        elif oper.eq(op,6):
            a = power(n1,n2)
            answer = str(n1)+' ** '+str(n2)+' = '+str(a)

        elif oper.eq(op,7):
            a= division(n1,n2)
            answer = str(n1)+' / '+str(n2)+' = '+str(a)

        else:
            a = baseChange(n1,n2)
            answer = str(n1)+' in base '+str(n2)+' is: '+str(a)

        reportT.config(state="normal")
        reportT.insert(INSERT, answer+'\n')
        reportT.config(state="disable")

        op = simpledialog.askinteger('Basic Calculator','''
        1. Addition
        2. Substraction
        3. Multiplication
        4. Whole division
        5. Residue
        6. Power
        7. Division
        8. Base change
        9. End
        Enter an option: ''')
        while op<1 or op>9:
            messagebox.showwarning(message='Please enter a valid option',title='')
            op = simpledialog.askinteger('','Type n: ')
    
#Addition
def add(n1,n2):
    return oper.add(n1,n2)

#Substraction
def substract(n1,n2):
    return oper.sub(n1,n2)

#Multiply
def multiply(mo,mr):
    return oper.mul(mo,mr)

#intDivision
def intDivision(div,dis):
    if dis != 0:
        a = oper.floordiv(div,dis)
    else:
        a ='You cannot divide a number by 0'
        
    return a

#Residue
def residue(div,dis):
    if dis != 0:
        ans = oper.mod(div,dis)
    else:
        ans = 'You cannot divide a number by 0'
    return ans
 
#power
def power(base,exp):
    return oper.pow(base,exp)

#division
def division(n1,n2):
    if n2 != 0:
        a = oper.truediv(n1,n2)
    else:
        a ='You cannot divide a number by 0'
        
    return a

def baseChange(num,bas):
    answer =''
    while num >= bas:
        answer = str(num%bas) + answer
        num = num // bas
    answer = str(num) + answer
    return answer


#Close interface
def end():
    raiz.destroy()

def delete():
    reportT.config(state="normal")
    reportT.delete("1.0","end")
    reportT.config(state="disable")

    
#GUI
raiz = Tk()
raiz.geometry("450x260")
raiz.title("Basic Calculator")

marco1 = Frame(raiz)
marco1.config(bd=3, relief="sunken")
marco1.pack(pady=10)
iniciarB = Button(marco1, text="Start", command=principal)
iniciarB.grid(row=0,column=0,padx=3, pady=3)
salirB = Button(marco1, text="End", command=end)
salirB.grid(row=0,column=1,padx=3, pady=3)
borrarB = Button(marco1, text="Delete", command=delete)
borrarB.grid(row=0,column=2,padx=3, pady=3)


marco2 = LabelFrame(raiz, text="Results")
marco2.config(bd=3, relief="sunken")
marco2.pack()
reportT = Text(marco2)
reportT.config(state="disable", width=50, height=10)
reportT.grid(row=0, column=0)


raiz.mainloop()

