
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import gui_support
from PIL import Image, ImageTk
from tkinter import messagebox,filedialog
import PIL.ImageDraw as ImageDraw,PIL.Image as Image, PIL.ImageShow as ImageShow 


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    gui_support.set_Tk_var()
    top = KPIT_Annotation_tool (root)
    gui_support.init(root, top)
    root.mainloop()


def create_KPIT_Annotation_tool(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    gui_support.set_Tk_var()
    top = KPIT_Annotation_tool (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_KPIT_Annotation_tool():
    w.destroy()


class KPIT_Annotation_tool:

    msg1=[]
    msg2=[]
    op=0
    def openimg(self):
        print("open")
        inpath = filedialog.askopenfilename()
        print (inpath)
        im = Image.open(inpath)
        self.Canvas1.image = ImageTk.PhotoImage(im)
# Add the image to the canvas, and set the anchor to the top left / north west corner
        self.Canvas1.create_image(0,0,image=self.Canvas1.image, anchor='nw')

    def closeimg(self):
        print("close")
        res=messagebox.askyesno("Quit","Are you sure to quit?")
        if res==1:
            root.destroy()
    def viewShortcuts(self):
        print("view")
        messagebox.showinfo("KPIT Annotation tool", "Open ctrl+o  \nClose Ctrl+q  \nwidth increase ctrl+i  \nwidth decrease ctrl+d  \nSwitch ctrl+r ")
        
    def rectangle(self):
        self.Canvas1.delete("all")
        rect=self.Canvas1.create_rectangle(200, 200, 300, 300, width=gui_support.spinbox.get(), fill='white')
    
    def polygon(self):
         self.Canvas1.delete("all")   
         poly=self.Canvas1.create_polygon([150,75,225,0,300,75,225,150],     outline='black', fill='white', width=gui_support.spinbox.get())
    
    def event(self):
        print("in event")
        if self.op==1:
            self.closeimg() 
        elif self.op==2:
            temp=gui_support.spinbox.get()
            if temp<5:
                temp=temp+1
            gui_support.spinbox.set(temp)
        elif self.op==3:
            temp=gui_support.spinbox.get()
            if temp>0:
                temp=temp-1
            gui_support.spinbox.set(temp)
        elif self.op==4:
            temp=gui_support.v.get()
            if temp==1:
                temp=2
                self.polygon()
            elif temp==2:
                temp=1
                self.rectangle()
            gui_support.v.set(temp)
        elif self.op==5:
            self.openimg()
            
    
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("600x430+416+123")
        top.title("KPIT Annotation tool")
        top.configure(background="#d9d9d9")



        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_separator(
                background="#d9d9d9")
        self.file = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.file,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="File")
        self.file.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.openimg,# TODO,
                font="TkMenuFont",
                foreground="#000000",
                label="Open      ctrl +O")
        self.file.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.closeimg,# TODO,
                font="TkMenuFont",
                foreground="#000000",
                label="Close      Ctrl+D")
        self.menubar.add_separator(
                background="#d9d9d9")
        self.shortcuts = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.shortcuts,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Shortcuts")
        self.shortcuts.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                command=self.viewShortcuts,# TODO,
                font="TkMenuFont",
                foreground="#000000",
                label="view shortcuts")


        self.Canvas1 = Canvas(top)
        self.Canvas1.place(relx=0.1, rely=0.23, relheight=0.98, relwidth=1.28)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief=RIDGE)
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(width=766)


        self.Spinbox1 = Spinbox(top, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.3, rely=0.05, relheight=0.04, relwidth=0.09)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(from_="1.0")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(textvariable=gui_support.spinbox)
        self.Spinbox1.configure(to="100.0")
        self.Spinbox1.configure(width=55)
        #print(gui_support.spinbox)

        self.txtWidth = Label(top)
        self.txtWidth.place(relx=0.17, rely=0.05, height=21, width=63)
        self.txtWidth.configure(background="#d9d9d9")
        self.txtWidth.configure(disabledforeground="#a3a3a3")
        self.txtWidth.configure(foreground="#000000")
        self.txtWidth.configure(text='''Tool width''')
        

        self.Radiobutton1 = Radiobutton(top)
        self.Radiobutton1.place(relx=0.52, rely=0.05, relheight=0.06
                , relwidth=0.13)
        self.Radiobutton1.configure(activebackground="#d9d9d9")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify=LEFT)
        self.Radiobutton1.configure(text='''Rectangle''')
        self.Radiobutton1.configure(variable=gui_support.v)
        self.Radiobutton1.configure(value=1)
        self.Radiobutton1.configure(command=self.rectangle)
        widget1=self.Radiobutton1
        widget1.bind('<Alt-r>',self.rectangle)
       

        self.Radiobutton2 = Radiobutton(top)
        self.Radiobutton2.place(relx=0.7, rely=0.05, relheight=0.06
                , relwidth=0.12)
        self.Radiobutton2.configure(activebackground="#d9d9d9")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify=LEFT)
        self.Radiobutton2.configure(text='''Polygon''')
        self.Radiobutton2.configure(variable=gui_support.v)
        self.Radiobutton2.configure(value=2)
        self.Radiobutton2.configure(command=self.polygon)
        
        def key(event):
            
            if event.char == event.keysym:
                self.msg2 = '%r' % event.char
                #print("m2 %r" %self.msg2)
            elif len(event.char) == 1:
                msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
            else:
                self.msg1 = '%r' % event.keysym
                #print("m1 %r" %self.msg1)
            if(self.msg1=="'Control_L'"  and self.msg2=="'q'"):
                #print(self.msg1)
                self.op=1
                self.event()
            elif(self.msg1=="'Control_L'"  and self.msg2=="'i'"):
                #print(self.msg1)
                self.op=2
                self.event()
            elif(self.msg1=="'Control_L'"  and self.msg2=="'d'"):
                #print(self.msg1)
                self.op=3
                self.event()
            elif(self.msg1=="'Control_L'"  and self.msg2=="'r'"):
                #print(self.msg1)
                self.op=4
                self.event()
                self.msg1='0'
                self.msg2='0'
            elif(self.msg1=="'Control_L'"  and self.msg2=="'o'"):
                self.op=5
                self.event()
            
            #print (msg1)
        
        
        
        top.bind_all('<Key>', key)
        

        
        
if __name__ == '__main__':
    vp_start_gui()



