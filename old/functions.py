from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

def createprofile():
    name = simpledialog.askstring("Question 1/10", "What is your name?")
    age = simpledialog.askinteger("Question 2/10", "How old are you?")
    print(name, age)
