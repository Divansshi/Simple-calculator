from tkinter import *

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=35,borderwidth=3,bg='pink')
e.grid(row=0,column=0,columnspan=3,padx=10,pady=20)


def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
    
    
def button_clear():
    e.delete(0,END)

    
def button_add():
    first_num = e.get()
    global fnum
    global math
    math='addition'
    fnum = int(first_num)
    e.delete(0,END)
    
    
def button_equal():
    second_num = e.get()
    e.delete(0,END)
    
    if math == 'addition':
        e.insert(0,fnum+int(second_num))
    if math == 'subtraction':
        e.insert(0,fnum-int(second_num))
    
    if math=='multiply':
        e.insert(0,fnum*int(second_num))
        
    if math=='division':
        e.insert(0,fnum/int(second_num))

def button_sub():
    first_num = e.get()
    global fnum
    global math
    math='subtraction'
    fnum = int(first_num)
    e.delete(0,END)

def button_multiply():
    first_num = e.get()
    global fnum
    global math
    math='multiply'
    fnum = int(first_num)
    e.delete(0,END)

def button_div():
    first_num = e.get()
    global fnum
    global math
    math='division'
    fnum = int(first_num)
    e.delete(0,END)


#defining the buttons
button1 = Button(root, text='1',padx=42,pady=20,command= lambda: button_click(1))
button2 = Button(root, text='2',padx=40,pady=20,command= lambda: button_click(2))
button3 = Button(root, text='3',padx=40,pady=20,command= lambda: button_click(3))
button4 = Button(root, text='4',padx=40,pady=20,command= lambda: button_click(4))
button5 = Button(root, text='5',padx=40,pady=20,command= lambda: button_click(5))
button6 = Button(root, text='6',padx=40,pady=20,command= lambda: button_click(6))
button7 = Button(root, text='7',padx=40,pady=20,command= lambda: button_click(7))
button8 = Button(root, text='8',padx=40,pady=20,command= lambda: button_click(8))
button9 = Button(root, text='9',padx=40,pady=20,command= lambda: button_click(9))
button0 = Button(root, text='0',padx=40,pady=20,command= lambda: button_click(0))
buttonadd = Button(root, text='+',padx=40,pady=20,command= button_add)
buttonequal = Button(root, text='=',padx=162,pady=20,command= button_equal)
buttonclear = Button(root, text='AC',padx=35,pady=20,command=button_clear)

buttonsub = Button(root, text='-',padx=41,pady=20,command= button_sub)
buttonmultiply = Button(root, text='*',padx=41,pady=20,command= button_multiply)
buttondiv = Button(root, text='/',padx=41,pady=20,command= button_div)


#adding buttons to screen

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=1)

buttonadd.grid(row=4, column=2)
buttonclear.grid(row=4, column=0)

buttonsub.grid(row=5,column=0)
buttonmultiply.grid(row=5,column=1)
buttondiv.grid(row=5,column=2)

buttonequal.grid(row=6,column=0,columnspan=3)

root.mainloop()