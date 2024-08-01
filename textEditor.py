from tkinter import *
from tkinter import colorchooser
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
import os


def change_color():
    color = colorchooser.askcolor()
    # print(color)
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_family.get(), font_size.get()))

def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)
    
def open_file():
    global path
    path = filedialog.askopenfile().name
    # print(type(path))
    file = open(path,'r')
    if not file:
        return
    window.title(os.path.basename(path))
    text_area.insert(1.0, file.read())
    
def save_file():
    file = open(path, 'w')
    file.write(text_area.get(1.0, END))

def saveas_file():
    path = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[("Text",".txt"),
                                               ("HTML", ".html"),
                                               ("All Types",".*")]).name
    file = open(path, 'w')
    file.write(text_area.get(1.0, END))
    window.title(os.path.basename(path))

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    messagebox.showinfo(title="About", message="This is the program writtem by YOU")

def quit():
    window.destroy()
    
window = Tk()

path = ""

font_family = StringVar()
font_family.set("arial")
font_size = StringVar()
font_size.set("25")

window.geometry("500x500")
window.title("Text Editor program")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


# creating a text area
text_area = Text(window,font=(font_family.get(), font_size.get()))
text_area.grid(sticky=NSEW)

# creating a scroll bar for text area
scroll_bar = Scrollbar(text_area)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

# creating a color chooser button
color_button = Button(frame, command=change_color, text="color")
color_button.grid(row=0, column=0, ipadx=10, padx=5)

# creating a option menu for font families
# OptionMenu(master, variable, *different_options)
option_menu = OptionMenu(frame, font_family, *font.families(), command=change_font)
option_menu.grid(row=0, column=1, ipadx=10, padx=5)

#creating a spinbox for changing font size
spin_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
spin_box.grid(row=0, column=2, ipadx=10, padx=5)


# creating a menubar for file, edit, help
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=saveas_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)


window.mainloop()