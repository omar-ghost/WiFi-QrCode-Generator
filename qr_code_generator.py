from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo, showwarning
from turtle import update
import customtkinter as ct
from PIL import ImageTk
import wifi_qrcode_generator as qr
import os ,sys
import subprocess

# main win
win=ct.CTk()
# width = win.winfo_screenwidth()
# height = win.winfo_screenheight()
# win.geometry("%dx%d" % (width,height))
win.attributes('-fullscreen',True)
win.title("Qr-Code Generator")
ct.set_appearance_mode("dark")
# win.resizable(False,False)
win.state('withdrawn')


#Functions
def savefile():
    global path
    if len(txt1.get()) > 1 and len(txt2.get()) >= 8:
        path = filedialog.asksaveasfilename(defaultextension=".png",initialdir="D:\\",initialfile=txt1.get())
        global g
        g.save(path)
        showinfo("Success", "QrCode is Saved")
    else:
        showwarning("Warning","Please, fill the information")
    

def clear():
    txt1.delete(0,END)
    txt2.delete(0,END)
    qr_canvas.create_image(168,168,image=cover)
    

def gen():
    if len(txt1.get()) > 1 and len(txt2.get()) >= 8:
        global g
        g= qr.wifi_qrcode(txt1.get(),"False","WPA",txt2.get())
        
        img = ImageTk.PhotoImage(g)
        
        qr_canvas.create_image(168,168,image= img)
        qr_canvas.image = img
    else:
        showwarning("Warning","Please, fill the information")

def showImage():
    global path
    os.startfile(path)

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

def explore():
    global path
    path = os.path.normpath(path)

    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        #PyInstaller creates a tem foler and stores in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)


# Frame
Frame1= ct.CTkFrame(win,width=800,height=250)
Frame1.pack(expand = True)

Frame2= ct.CTkFrame(Frame1,width=200,height=200)
Frame2.grid(column=1,row=0,rowspan=3,padx=10,pady=0,sticky='NS')



# Canvas
qr_canvas= ct.CTkCanvas(Frame1,width=330,height=330)
cover= PhotoImage(file= resource_path("my_project.png"))
qr_canvas.create_image(168,168,image=cover)
qr_canvas.grid(column=0,row =0,padx=220,pady=30,sticky='NW')





# Lbl
lbl2= ct.CTkLabel(Frame1,text="SSID",text_font=('arial',21))
lbl2.grid(column=0,row =1,padx=(0,0), pady= (50,0),sticky='NW')

lbl3= ct.CTkLabel(Frame1,text="password",text_font=('arial',21))
lbl3.grid(column=0,row =2,padx=(0,0), pady= (10,70),sticky='NW')

# #Entery
txt1= ct.CTkEntry(Frame1,width=250)
txt1.grid(column=0,row =1,padx=(180,0), pady= (50,0),sticky='NW')

txt2= ct.CTkEntry(Frame1,width=250)
txt2.grid(column=0,row =2,padx=(180,0), pady= (10,70),sticky='NW')


# #btn
btn_clear= ct.CTkButton(Frame2,text="Clear",command=clear,text_font=('arial',18))
btn_clear.grid(column=0,row=0,padx=20,pady=(70,10))

btn_gen= ct.CTkButton(Frame2,text="Generate",command= gen,text_font=('arial',18))
btn_gen.grid(column=0,row=1,padx=20,pady=10)

btn_save= ct.CTkButton(Frame2,text="Save",command= savefile,text_font=('arial',18))
btn_save.grid(column=0,row=2,padx=20,pady=10)

btn_open= ct.CTkButton(Frame2,text="Show In Folder",command= explore,text_font=('arial',15))
btn_open.grid(column=0,row=3,padx=20,pady=10)

btn_show= ct.CTkButton(Frame2,text="Open Saved Image",command=showImage,text_font=('arial',12))
btn_show.grid(column=0,row=4,padx=20,pady=10)

btn_exit= ct.CTkButton(Frame2,text="Exit",command=lambda:Frame2.quit(),text_font=('arial',18))
btn_exit.grid(column=0,row=5,padx=20,pady=10)

win.mainloop()