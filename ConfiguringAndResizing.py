from tkinter import *
root=Tk()
root.geometry("600x400")
root.title("GUI Application")

frame = Frame(root,bg="skyblue",width=600,height=400)
frame.pack()
lbl = Label(frame,text = "Enter Name : ",font=("Times new roman",14),bg="skyblue")
lbl.place(x=70,y=100)

ent = Entry(frame,width = 20,font=("Times new roman",20),bg="skyblue")
ent.place(x=200,y=100)

mess=Label(frame,text="Hello",font=("Times new roman",20),bg="skyblue")
mess.place(x=200,y=200)

btn=Button(frame,text="Click me", command=lambda : mess.config(text = f"Hello {ent.get()}"),width=20,font=("Times new roman",20),bg="yellow")

btn.place(x=150,y=300)

root.resizable(True,True)
root.mainloop()