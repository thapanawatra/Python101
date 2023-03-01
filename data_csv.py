from tkinter import *
from tkinter import ttk #theme of tk
import csv

GUI = Tk()
GUI.geometry('500x400+600+200')
GUI.title('โปรแกรมกรอกข้อมูลรายชื่อ เบอร์โทรติดต่อ')

FONT1 = ('Angsana New',25)
FONT2 = ('Angsana New',30)
L1 = ttk.Label(GUI,text='ชื่อ - นามสกุล',font=FONT1)
L1.pack()

name_entry = StringVar()
E1 = ttk.Entry(GUI,textvariable=name_entry,font=FONT1,width=30)
E1.pack()


L2 = ttk.Label(GUI,text='เบอร์โทรศัพท์',font=FONT1)
L2.pack()

phone_entry = StringVar()
E2 = ttk.Entry(GUI,textvariable=phone_entry,font=FONT1,width=30)
E2.pack()

L3 = ttk.Label(GUI,text='ไอดีไลน์',font=FONT1)
L3.pack()

ID_line_entry = StringVar()
E3 = ttk.Entry(GUI,textvariable=ID_line_entry,font=FONT1,width=30)
E3.pack()


# สร้างฟังก์ชันสำหรับบันทึกข้อมูล
def save_data():
    name = name_entry.get()
    phone = phone_entry.get()
    ID_line = ID_line_entry.get()

    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, ID_line])
    
    name_entry.set('')
    phone_entry.set('')
    ID_line_entry.set('')
    

B1 = ttk.Button(GUI,text='บันทึก',command=save_data)
B1.pack(ipadx=40,ipady=20,pady=20)

E3.bind('<Return>',save_data)


GUI.mainloop()
