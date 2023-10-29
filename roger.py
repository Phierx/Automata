from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import os, sys
from selenium.webdriver.common.by import By
import time
# GUI
from tkinter import *
from tkinter import messagebox




root =Tk()
root.title("Roger Automation")
#root.iconbitmap(resource_path('images/icon.ico'))

root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

def searchMode():
    username = user.get()
    password = code.get()
    thesearch = searchl.get()
    option = Options()

    option.add_experimental_option ("detach",True)

    web = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    web.maximize_window()

    web.get ("https://moal.sisk12.net/MOAL360x3/login")

    time.sleep(4)
    unam=web.find_element("xpath",'//*[@id="txtUserName"]')
    # ############ username ##############
    unam.send_keys(username)

    passn=web.find_element("xpath",'//*[@id="txtPassword"]')
    # ############ password ##############
    passn.send_keys(password)

    login = web.find_element("xpath",'//*[@id="classicLoginButton"]')
    login.click()

    time.sleep(2)

    nav = web.find_element("xpath", '//*[@id="594"]')
    nav.click()
    nav = web.find_element("xpath", '//*[@id="843"]')
    nav.click()
    nav = web.find_element("xpath", '//*[@id="928"]')
    nav.click()

    time.sleep(1)
    nav = web.switch_to.frame(web.find_element("xpath", '//*[@id="contentFrame"]'))
    nav = web.find_element("xpath", '//*[@name="ctl00$ctl02$txtFirstName"]')
    # ############ Search ##############
    nav.send_keys(thesearch)
    j = web.find_element("xpath", '//*[@id="ctl00_ctl02_btnSearch"]')
    j.click()

#img= PhotoImage(file='images/pageinfo.png')
#Label(root,image=img,bg='white').place(x=40,y=40)

frame =Frame (root,width=450,height=450,bg="white")
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
        searchl.insert(0,'Search By firstname')


searchl = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsft YaHei UI Light',11))
searchl.place (x=30,y=160)
searchl.insert(0,'Search By firstname')
searchl.bind('<FocusIn>', on_enter)
searchl.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=187)
###############################---------------------------

Button(frame,width=29,pady=7,text='Search',bg='#57a1f8',fg='white',border=0,command=searchMode).place(x=30,y=224)



root.mainloop()