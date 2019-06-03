from tkinter import *
from PIL import Image, ImageTk
import sys
import os
import funct

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # creation of init_window
    def init_window(self):

        # changing title of master widget
        self.master.title('ACITventure')

        # fill space of root window
        self.pack(fill=BOTH, expand=1)

        # creating menu instance
        menu = Menu(self.master)
        self.master.config(menu = menu)

        # create file object
        file = Menu(menu)

        # background image 
        #FIXME: file.add_command(label = 'Load background', command = self.backgroundImg)

        # exit command in file menu
        file.add_command(label = 'Exit', command = self.client_exit)

        # add 'file' to menu
        menu.add_cascade(label= 'File', menu = file)

        # create edit object
        edit = Menu(menu)

        # show image and text commands in edit menu
        # edit.add_command(label = 'Show Image', command = self.showImg)
        # edit.add_command(label = 'Show Text', command = self.showText)

        # add 'edit' to menu
        menu.add_cascade(label = 'Edit', menu = edit)

        # creating a button
        quitButton = Button(self, text='Quit', command = self.client_exit)

        # placing button
        quitButton.place(x = 0, y = 0)
    
    # exit function
    def client_exit(self):
        exit()

    """
    # show image and text functions
    def showImg(self):
        load = Image.open('owo.png')
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image = render)
        img.image = render
        img.place(x = 0, y = 0)

    # background image
    def backgroundImg(self):
        load = Image.open('main.png')
        render = ImageTk.PhotoImage(load)
        background_label = Label(root, image = render)
        background_label.render = render
        background_label.place(x = 0, y = 0, height = 720, width = 720)


    def showText(self):
        text = Label(self, text='OwO')
        text.pack()
    """

# create root window - can add windows within windows
root = Tk()

# background image for root window
loadbackground = Image.open('main.png')
maincanvas = Canvas(root, width = 720, height = 720)
maincanvas.pack()
tk_img = ImageTk.PhotoImage(loadbackground)
maincanvas.create_image(125, 125, image = tk_img)
quit_button = Button(root, text = 'Quit', command = root.quit, width = 10, activebackground = '#33B5E5')
quit_button_window = maincanvas.create_window(10, 690, anchor = 'nw', window = quit_button)

quit_button = Button(root, text = 'Help', command = root.quit, width = 10, activebackground = '#33B5E5')
quit_button_window = maincanvas.create_window(100, 690, anchor = 'nw', window = quit_button)

quit_button = Button(root, text = 'Start', command = root.quit, width = 10, activebackground = '#33B5E5')
quit_button_window = maincanvas.create_window(190, 690, anchor = 'nw', window = quit_button)


# size of the window
root.geometry("720x720")

# create instance
app = Window(root)

def UwUcallback():
    os.system('main.py')
b = Button(root, text = 'hello', command = UwUcallback)
b.pack()

# mainloop
root.mainloop()

