from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from tkinter import *
import time


def search_result():
    bot=webdriver.Firefox()
    bot.get('https://www.duckduckgo.com')
    time.sleep(2)
    window.quit()
    result=bot.find_element_by_name('q')
    result.clear()
    result.send_keys(entry1.get())
    result.send_keys(Keys.RETURN)




window=Tk()
window.geometry("450x200")
search=Label(window,text="What will you search for?",font='Montserrat 15')
search.place(x=10,y=10)
entry1=Entry(window)
entry1.place(x=250,y=10)

b1=Button(window,text="Search", command=search_result,width=12,bg='white', fg='black')
b1.place(x=150,y=50)

window.mainloop()