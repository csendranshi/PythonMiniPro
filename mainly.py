# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:19:42 2020

@author: Ketaki Keluskar
"""

import os
from subprocess import call

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def click_checkinn():
    call(["python", "checkin_gui_and_program.py"])
def click_list():
    call(["python", "listgui.py"])
def click_checkout():
    call(["python", "checkoutgui.py"])
def click_getinfo():
    call(["python","getinfoui.py"])


class HOTEL_MANAGEMENT:
    def __init__(self):
        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font14 = "-family {Times New Roman} -size 18 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Times New Roman} -size 36 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Times New Roman} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("10000x10000")
        root.title("SE GROUP OF RESORTS")
        root.configure(background="#A9A9A9")
        root.configure(highlightbackground="black")
        root.configure(highlightcolor="black")



        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)

        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#e75480")
        self.Frame1.configure(highlightbackground="#8B008B")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        self.Label6 = Label(self.Frame1)
        self.Label6.place(relx=0.08, rely=0.01, relheight=0.15, relwidth=0.86)
        self.Label6.configure(background="light blue")
        self.Label6.configure(font=font16)
        self.Label6.configure(foreground="black")
        self.Label6.configure(highlightbackground="light blue")
        self.Label6.configure(highlightcolor="light blue")
        self.Label6.configure(text='''SE GROUP OF RESORTS''')
        self.Label6.configure(width=791)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.32, rely=0.17, height=103, width=566)
        self.Button2.configure(activebackground="light blue")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="light blue")
        self.Button2.configure(disabledforeground="light blue")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="light blue")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''CHECK IN''')
        self.Button2.configure(width=566)
        self.Button2.configure(command=click_checkinn)

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.32, rely=0.33, height=93, width=566)
        self.Button3.configure(activebackground="light blue")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="light blue")
        self.Button3.configure(disabledforeground="light blue")
        self.Button3.configure(font=font14)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="light blue")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''CHECKED IN GUESTS''')
        self.Button3.configure(width=566)
        self.Button3.configure(command=click_list)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.32, rely=0.47, height=93, width=566)
        self.Button4.configure(activebackground="light blue")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="light blue")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=font14)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="light blue")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''CHECK OUT''')
        self.Button4.configure(width=566)
        self.Button4.configure(command=click_checkout)

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.32, rely=0.61, height=103, width=566)
        self.Button5.configure(activebackground="light blue")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="light blue")
        self.Button5.configure(disabledforeground="light blue")
        self.Button5.configure(font=font14)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="light blue")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''GET INFO OF CHECKED IN CUSTOMER''')
        self.Button5.configure(width=566)
        self.Button5.configure(command=click_getinfo)

        root.mainloop()
        


if __name__ == '__main__':
    GUUEST=HOTEL_MANAGEMENT()


