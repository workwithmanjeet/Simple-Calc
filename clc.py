#SIMPLE CALC
from tkinter import *
root = Tk()
root.title("Calculator")
root.iconbitmap('C:/Users/Manjeet Saini/Documents/py_project/tkinter/clcicon.ico') 

root.geometry("335x330")
root.minsize(335,330)
root.maxsize(335,330)

e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def b_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def b_sign():
    num=-(float(e.get()))
    e.delete(0,END)
    e.insert(0,str(num))
    
def b_deci():
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str("."))
    bdeci["state"] = DISABLED

    
def b_clear():
    e.delete(0,END)
    bdeci["state"] = NORMAL
    
def b_add():
    first=e.get()
    global f_num
    global ops
    ops="+"
    f_num=float(first)
    e.delete(0,END)
    bdeci["state"] = NORMAL
    
def b_sub():
    first=e.get()
    global f_num
    global ops
    ops="-"
    f_num=float(first)
    e.delete(0,END)
    bdeci["state"] = NORMAL
        
def b_multi():
    first=e.get()
    global f_num
    global ops
    ops="*"
    f_num=float(first)
    e.delete(0,END)
    bdeci["state"] = NORMAL
        
def b_div():
    first=e.get()
    global f_num
    global ops
    ops="/"
    f_num=float(first)
    e.delete(0,END)
    bdeci["state"] = NORMAL
        

    
def b_equal():
    second=e.get()
    if ops=="+":
        result=float(second)+f_num
    elif ops=="-":
        result=f_num-float(second)
    elif ops=="*":
        result=float(second)*f_num
    else:
        result=f_num/float(second)
        
    e.delete(0,END)
    e.insert(0,result)
        
    


# butttons    
b1=Button(root,text="1",padx=30,pady=15,command=lambda: b_click(1))
b2=Button(root,text="2",padx=30,pady=15,command=lambda: b_click(2))
b3=Button(root,text="3",padx=30,pady=15,command=lambda: b_click(3))
b4=Button(root,text="4",padx=30,pady=15,command=lambda: b_click(4))
b5=Button(root,text="5",padx=30,pady=15,command=lambda: b_click(5))
b6=Button(root,text="6",padx=30,pady=15,command=lambda: b_click(6))
b7=Button(root,text="7",padx=30,pady=15,command=lambda: b_click(7))
b8=Button(root,text="8",padx=30,pady=15,command=lambda: b_click(8))
b9=Button(root,text="9",padx=30,pady=15,command=lambda: b_click(9))
b0=Button(root,text="0",padx=30,pady=15,command=lambda: b_click(0))

bdeci=Button(root,text=".",padx=31,pady=15,command=b_deci)
bsign=Button(root,text="+/-",padx=25,pady=15,command=b_sign)

badd=Button(root,text="+",padx=30,pady=15,command=b_add)
bsub=Button(root,text="-",padx=31,pady=15,command=b_sub)
bmulti=Button(root,text="*",padx=31,pady=15,command=b_multi)
bdiv=Button(root,text="/",padx=31,pady=15,command=b_div)
bequal=Button(root,text="=",padx=70,pady=15,command=b_equal)
bclear=Button(root,text="Clear",padx=62,pady=15,command=b_clear)
# button positons
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
b0.grid(row=4,column=1)

badd.grid(row=1,column=3)
bsub.grid(row=2,column=3)
bmulti.grid(row=3,column=3)
bdiv.grid(row=4,column=3)
bdeci.grid(row=4,column=2)
bsign.grid(row=4,column=0)
bclear.grid(row=5,column=0,columnspan=2)
bequal.grid(row=5,column=2,columnspan=2)


root.mainloop()
