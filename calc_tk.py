from tkinter import *
import tkinter as tk






window_2 = Tk()
window_2.title("Calculator")
window_2.configure(bg='light blue')
window_2.geometry('300x500')


field = Entry(window_2, width=30, font=("Comic Sans MS", 10, "bold"))
field.place(x=40,y=70)
field_txt = ""

def press(value):
    global field_txt
    field_txt =  field_txt + str(value)
    field.delete("0","end")
    field.insert("0",field_txt)
def equal():
    global field_txt
    res = str(eval(field_txt))
    field.delete("0","end")
    field_txt = ""
    field.insert("0",res)
def clear():
    global field_txt
    field_txt = ""
    field.delete("0", "end")
#############################################################
#entering numbers
bpress_0 = Button(window_2, text="0", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='royal blue',
            bd='5',command=lambda :press(0)).place(x=100, y=385)
press_7 = Button(window_2, text="7", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='royal blue',
            bd='5',command=lambda :press(7)).place(x=60, y=310)
press_8 = Button(window_2, text="8", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='royal blue',
            bd='5',command=lambda :press(8)).place(x=100, y=310)
press_9 = Button(window_2, text="9", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='royal blue',
            bd='5',command=lambda :press(9)).place(x=140, y=310)
press_4 = Button(window_2, text="4", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='royal blue',
            bd='5',command=lambda :press(4)).place(x=60, y=235)
press_5 = Button(window_2, text="5", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='royal blue',
            bd='5',command=lambda :press(5)).place(x=100, y=235)
press_6 = Button(window_2, text="6", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='royal blue',
            bd='5',command=lambda :press(6)).place(x=140, y=235)
press_1 = Button(window_2, text="1", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='royal blue',
            bd='5',command=lambda :press(1)).place(x=60, y=170)
press_2 = Button(window_2, text="2", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='royal blue',
            bd='5',command=lambda :press(2)).place(x=100, y=170)
press_3 = Button(window_2, text="3", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='royal blue',
            bd='5',command=lambda :press(3)).place(x=140, y=170)
###################################################################
#enter operators
press_plus =  Button(window_2, text="+", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='saddlebrown',
            bd='6',command=lambda :press('+')).place(x=180, y=170)
press_minus =  Button(window_2, text="-", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='saddlebrown',
            bd='6',command=lambda :press('-')).place(x=180, y=240)
press_multiply =  Button(window_2, text="*", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='saddlebrown',
            bd='6',command=lambda :press('*')).place(x=180, y=310)
press_divid =  Button(window_2, text="/", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='saddlebrown',
            bd='6',command=lambda :press('/')).place(x=180, y=385)
press_dot =  Button(window_2, text=".", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='saddlebrown',
            bd='6',command=lambda :press('.')).place(x=140, y=385)	

press_equal =  Button(window_2, text="=", width=5, height=14, font=("Comic Sans MS", 10, "bold"), background='saddlebrown',
            bd='9',command=lambda :equal()).place(x=220, y=169)	
press_clear =  Button(window_2, text="CLR", width=3, height=3, font=("Comic Sans MS", 10, "bold"), background='saddlebrown',
            bd='6',command=lambda :clear()).place(x=60, y=385)


entry1=Entry()
window_2.mainloop()