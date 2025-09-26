import tkinter
from tkinter import ttk

app=tkinter.Tk()
app.config(background="light blue")
app.geometry("400x500")
app.title("TOPS")

#tkinter.Label(text="Firstname").pack()
#tkinter.Label(text="Lastname").pack()

#tkinter.Label(text="Firstname").place(x=0,y=0)
#tkinter.Label(text="Lastname").place(x=0,y=30)

tkinter.Label(text="Firstname",bg="light blue",fg="red",font="Ebrima 15 bold").grid(row=0,column=0,sticky='w')
tkinter.Label(text="Lastname",bg="light blue",fg="red",font="Ebrima 15 bold").grid(row=1,column=0,sticky='w')

tkinter.Entry().grid(row=0,column=1,sticky='w')
tkinter.Entry().grid(row=1,column=1,sticky='w')

tkinter.Radiobutton(value=0, text="Male",bg="light blue",fg="red",font="Ebrima 15 bold").grid(row=2,column=0,sticky='w')
tkinter.Radiobutton(value=1,text="Female",bg="light blue",fg="red",font="Ebrima 15 bold").grid(row=2,column=1,sticky='w')

tkinter.Checkbutton(text="Gujarati",bg="light blue",fg="red",font="Ebrima 15 bold").grid(row=3,column=0,sticky='w')
tkinter.Checkbutton(text="Hindi",bg="light blue",fg="red",font="Ebrima 15 bold").grid(row=4,column=0,sticky='w')
tkinter.Checkbutton(text="English",bg="light blue",fg="red",font="Ebrima 15 bold").grid(row=5,column=0,sticky='w')

city=['Rajkot','Baroda','Surat','Ahmedabad','Jamnagar']
ttk.Combobox(values=city).grid(row=6,column=0,sticky='w')

def btnclick():
    print("Button Click!")

tkinter.Button(text="Submit",fg="red",font="Ebrima 15 bold",command=btnclick).place(x=150,y=270)

app.mainloop()
# sticky refer to alignment of text in grid .