from tkinter import *
from PIL import Image, ImageTk

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

        # exit command in file menu
        file.add_command(label = 'Exit', command = self.client_exit)

        # add 'file' to menu
        menu.add_cascade(label= 'File', menu = file)

        # create edit object
        edit = Menu(menu)

        # show image and text commands in edit menu
        edit.add_command(label = 'Show Pretty Image', command = self.showImg)
        edit.add_command(label = 'Show Text', command = self.showText)

        # add 'edit' to menu
        menu.add_cascade(label = 'Edit', menu = edit)

        # creating a button
        quitButton = Button(self, text='Quit', command = self.client_exit)

        # placing button
        quitButton.place(x = 0, y = 0)
    
    # exit function
    def client_exit(self):
        exit()

    # show image and text functions
    def showImg(self):
        load = Image.open('owo.png')
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image = render)
        img.imnage = render
        img.place(x = 0, y = 0)

    def showText(self):
        text = Label(self, text='OwO')
        text.pack()

# create root window - can add windows within windows
root = Tk()

# size of the window
root.geometry("400x300")

# create instance
app = Window(root)

# mainloop
root.mainloop()

