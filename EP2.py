from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI =Tk()
GUI.title('โปรแกรมบันทึกข้อมูลรายรับ-รายจ่ายส่วนตัวนักเรียน')
GUI.geometry('500x400')

L1 = Label (GUI,text='โปรแกรมบันทึกข้อมูลรายรับ-รายจ่ายส่วนตัวนักเรียน',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

def Button1():
    text = 'ใช้บันทึกรายรับในแต่ละวัน'
    messagebox.showinfo('รายรับ',text)

FB1 = LabelFrame(GUI)
FB1.place(x=10,y=70)
B1 = ttk.Button(FB1,text='รายรับ',command=Button1)
B1.pack(ipadx=20,ipady=20)


def Button2():
    text = 'ใช้บันทึกรายจ่ายในแต่ละวัน'
    messagebox.showinfo('รายจ่าย',text)

FB2 = LabelFrame(GUI)
FB2.place(x=10,y=70)
B2 = ttk.Button(FB1,text='รายจ่าย',command=Button2)
B2.pack(ipadx=20,ipady=20)



def Button3():
    text = 'เงินคงเหลือ'
    messagebox.showinfo('เงินคงเหลือ',text)

FB3 = LabelFrame(GUI)
FB3.place(x=10,y=70)
B3 = ttk.Button(FB1,text='เงินคงเหลือ',command=Button3)
B3.pack(ipadx=20,ipady=20)

def Button4():
    text = 'นำเงินฝากธนาคารโรงเรียน'
    messagebox.showinfo('จำนวนเงินนำฝาก',text)

FB4 = LabelFrame(GUI)
FB4.place(x=10,y=70)
B4 = ttk.Button(FB1,text='นำฝาก',command=Button4)
B4.pack(ipadx=20,ipady=20)


def exit_program():
    FB1.destroy()
    messagebox.showinfo('จบการทำงาน')

FB5 = LabelFrame(GUI)
FB5.place(x=10,y=70)
B5 = ttk.Button(FB1,text='จบการทำงาน',command=exit_program)
B5.pack(ipadx=20,ipady=20)



GUI.mainloop()
