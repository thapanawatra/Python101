# unclevocab.py
from tkinter import *
from tkinter import ttk #theme of tk

GUI = Tk()
GUI.geometry('500x300+600+200')
GUI.title('โปรแกรมท่องจำคำศัพท์อัจฉริยะ - Uncle Vocab')

FONT1 = ('Angsana New',25)
FONT2 = ('Angsana New',30)
L1 = ttk.Label(GUI,text='คำศัพท์',font=FONT1)
L1.pack()

v_vocab = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_vocab,font=FONT1,width=30)
E1.pack()


#######VOCAB########
L2 = ttk.Label(GUI,text='คำแปล',font=FONT1)
L2.pack()

v_meaning = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_meaning,font=FONT1,width=30)
E2.pack()

#######BUTTON########
def SaveVocab(event=None):
    vocab = v_vocab.get()
    meaning = v_meaning.get()
    print('v: {} M: {}'.format(vocab,meaning))
    v_vocab.set('')
    v_meaning.set('')
    E1.focus()
    print('------')

B1 = ttk.Button(GUI,text='Save Vacab',command=SaveVocab)
B1.pack(ipadx=40,ipady=20,pady=20)

E2.bind('<Return>',SaveVocab)


GUI.mainloop()
