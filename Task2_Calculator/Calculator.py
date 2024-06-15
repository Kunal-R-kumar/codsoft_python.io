from tkinter import *
from PIL import Image,ImageTk
def AC(st=0,en=END):
    e.delete(st,en)
def eq():
    a,rs="",""
    for i in e.get():
        if i.isdigit(): 
            if rs!="" and rs[-1]==")":
                rs+="*"
            a+=i
        elif i in ['+','-','*','/']:
            if a=="":rs+=i
            else:
                rs+=str(int(a))+i
                a=''    
        elif i=="(" :
            if a=="":rs+=i
            else:
                rs+=str(int(a))+"*("
                a=""
        elif i==")" :
            if a=="":rs+=i
            else:
                rs+=str(int(a))+")"
                a=""
    rs=rs.replace(")(",")*(")
    AC()
    try:
        if a=='':
            b=eval(rs)
        else:
            b=eval((rs+str(int(a))))
    except:
        b="Wrong Expression"
        e.after(2000,AC)
    e.insert(e.index(INSERT),b)
    e.bind_all("<Button>",restart)
    e.bind_all("<Key>",restart)  
def restart(event):
    AC()
    e.insert(e.index(INSERT),event.keysym)
    e.unbind_all("<Button>")
    e.unbind_all("<Key>")
    for i in range(10):
        binder(str(i))
def key_click(value):
    if e!=base.focus_get():
        e.insert(e.index(INSERT),value)
        e.focus_set()
def create_button(value,r,c,cimg):
    Button(fr, image=cimg,bg="black",text=value, compound=CENTER, command=lambda: [e.focus_set(),e.insert(e.index(INSERT),value)],fg="white",font=(f"Times {20}")).grid(row=r,column=c)
def create_spbutton(txt,value,r,c,cimg,clr,cmd):
    Button(fr, image=cimg,bg="black",fg=clr,text=txt,command=cmd ,compound=CENTER,font=(f"Times {20}")).grid(row=r,column=c)
def only_number(ip):
    if ip=="" or ip=="Wrong Expression": return True
    else:
        for i in range(len(ip)):
            if ip[i].isdigit()==False and ip[i] not in ['(',')'] and (ip[i] in['+','-','*','/','.'] and (ip[i-1].isdigit() or ip[i-1]==")"))==False:return False
        else:return True
def piccorector(abc):
    return ImageTk.PhotoImage(Image.open(f'{abc}.png').resize((65,50)))
def binder(value):
    base.bind(value,lambda event:[key_click(value)])
    e.bind("<Return>",lambda event:eq())
    e.bind("<Escape>",lambda event:AC())
def bkt():
    idx=e.index(INSERT)
    e.insert(idx,'()')
    e.icursor(idx+1)
    e.focus_set()
#tkinter basic window 
base=Tk()
base.title("Calculator")
validd=base.register(only_number)
base.config(bg="black")
base.resizable(False,False)
#required images with entry and button widgets
mimg=piccorector('operand')
im=piccorector('operator')
eimg=piccorector('equal')
e=Entry(highlightthickness=2,highlightbackground="#73b8bf",highlightcolor="#73b8bf",font=("Times 20"),validate="key",validatecommand=(validd,"%P"))
e.pack(pady=10)
fr=Frame()
fr.pack(side=LEFT)
for i in range(3):
    for j in range(1,4):
        create_button(str(3*i+j),i+2,j,mimg)
for i in ['00','0','.']:
    create_button(i,5,1+(['00','0','.'].index(i)),mimg)
for i in ['+','-','*','/']:
    create_button(i,1+(['+','-','*','/'].index(i)),4,im)
create_spbutton("( )","()",1,3,im,"White",bkt)
create_spbutton("AC","AC",1,1,eimg,"black",AC)
create_spbutton("◀","◀",1,2,eimg,"black",lambda:AC(e.index(INSERT)-1,e.index(INSERT)))
create_spbutton("=",'=',5,4,eimg,"black",eq)
#binding the keys
for i in range(10):
    binder(str(i))
base.mainloop()