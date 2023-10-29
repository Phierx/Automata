from tkinter import *
from tkinter import messagebox

def login():
    username=user.get()
    password=code.get()


root =Tk()
root.title("login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username = user.get()
    password = code.get()
    if username=='admin' and password=='1234':
        print('You are the shit')

img= PhotoImage(file='pageinfo.png')
Label(root,image=img,bg='white').place(x=40,y=40)

frame =Frame (root,width=250,height=250,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign In',fg='#57a1f8',bg= 'white', font=('Microsft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)


###############################---USER------------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name == '':
        user.insert(0,'Username')


user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsft YaHei UI Light',11))
user.place (x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

###############################------PASSWORD---------------------
def on_enter(e):
    code.delete(0,'end')
    
def on_leave(e):
    name=code.get()
    if name == '':
        code.insert(0,'Password')


code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsft YaHei UI Light',11))
code.place (x=30,y=120)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=147)
###############################--------Search-------------------
def on_enter(e):
    searchl.delete(0,'end')
    
def on_leave(e):
    name=searchl.get()
    if name == '':
        searchl.insert(0,'Search By lastname')


searchl = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsft YaHei UI Light',11))
searchl.place (x=30,y=160)
searchl.insert(0,'Search By lastname')
searchl.bind('<FocusIn>', on_enter)
searchl.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=187)
###############################---------------------------

Button(frame,width=29,pady=7,text='Search',bg='#57a1f8',fg='white',border=0,command=signin).place(x=30,y=224)



root.mainloop()