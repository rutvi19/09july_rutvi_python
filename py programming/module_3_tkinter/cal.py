import tkinter
app=tkinter.Tk()
app.title("TOPS")
app.geometry("300x300")
app.config(bg="light blue")

tkinter.Label(text="Firstnumber",bg="light blue",fg="red",font='Constantia 15 bold').grid(row=0,column=0)

tkinter.Label(text="Lastnumber:",bg="light blue",fg="red",font='Constantia 15 bold').grid(row=1,column=0)

fno=tkinter.Entry()
fno.grid(row=0,column=1)
lno=tkinter.Entry()
lno.grid(row=1,column=1)

def getval():
    print("Firstnumber:",fno.get())
    print("Lastnumber:",lno.get())
    print("sum:",int(fno.get())+int(lno.get()))
    
def getval1():
    print("Firstnumber:",fno.get())
    print("Lastnumber:",lno.get())
    print("sub:",int(fno.get())-int(lno.get())) 

def getval2():
    print("Firstnumber:",fno.get())
    print("Lastnumber:",lno.get())
    print("mul:",int(fno.get())*int(lno.get())) 

def getval3():
    print("Firstnumber:",fno.get())
    print("Lastnumber:",lno.get())
    print("mul:",int(fno.get())*int(lno.get()))           
    

tkinter.Button(text="+",fg="red",font='Constantia 15 bold',command=getval).place(x=100,y=100)
tkinter.Button(text="-",fg="red",font='Constantia 15 bold',command=getval1).place(x=200,y=100)
tkinter.Button(text="*",fg="red",font='Constantia 15 bold',command=getval2).place(x=100,y=150)
tkinter.Button(text="/",fg="red",font='Constantia 15 bold',command=getval3).place(x=200,y=150)
app.mainloop()