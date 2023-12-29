import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql 

window = tk.Tk()
window.geometry("500x500")
window.resizable(0,0)
window.title("TO DO LIST")
window.configure(bg="mistyrose")

tasks = []

headingframe = tk.Frame(window,bg="mistyrose")
optionsframe = tk.Frame(window,bg="mistyrose")
listframe = tk.Frame(window,bg="mistyrose")
headingframe.pack(side="top",fill = "both")  
optionsframe.pack(expand = True,fill = "both")  
listframe.pack(side="bottom",expand = True,fill="both")  

headinglabel = ttk.Label(headingframe,text = "To Do List",font = ("arial", "30","bold"),background = "mistyrose",foreground = "indian red")  
headinglabel.pack(padx = 20, pady = 20)  
  
todolabel = ttk.Label(optionsframe,text = "WHAT TO DO:",font = ("arial", "11", "bold"),background = "mistyrose",foreground = "indian red")  
todolabel.place(x = 60, y = 40)

todofield = ttk.Entry(optionsframe,font = ("arial", "12"),width = 18,background = "mistyrose",foreground = "indian red")  
todofield.place(x =220, y = 38) 

todolist = tk.Listbox(listframe,width = 70,height = 10,selectmode = 'SINGLE',background = "white",foreground = "indian red",selectbackground = "mistyrose",selectforeground = "black")   
todolist.place(x = 25, y = 30)

def todo():
    todostring = todofield.get()
    if len(todostring)==0:
        messagebox.showinfo("Nothing to do")
    else:
        tasks.append(todostring)
        cursor.execute("insert into tasks values (?)",(todostring,))
        listupdate()
        todofield.delete(0,'end')

def listupdate():
    clearlist()
    for task in tasks:
        todolist.insert('end',task)

def delete():
    try:
        value = todolist.get(todolist.curselection())
        if value in tasks:
            tasks.remove(value)
            listupdate()
            cursor.execute('delete from tasks where title = ?',(value,))
    except:
        messagebox.showinfo("None selected")

def deleteall():
    message_box = messagebox.askyesno("delete all")
    if message_box == True:
        while(len(tasks)!=0):
            tasks.pop()
        cursor.execute("delete from tasks")
        listupdate()

def clearlist():
    todolist.delete(0,'end')

def close():
    print(tasks)
    window.destroy()

def retrieve():
    while(len(tasks)!=0):
        tasks.pop()
    for row in cursor.exectue('select title from tasks'):
        tasks.append(row[0])

addbutton = ttk.Button(optionsframe,text="ADD TODO",width=24,command=todo)
delbutton = ttk.Button(optionsframe,text="DELETE",width=24,command=delete)
delallbutton = ttk.Button(optionsframe,text="DELETE ALL",width=24,command=deleteall)
exitbutton = ttk.Button(optionsframe,text="EXIT",width=24,command=exit)

addbutton.place(x = 40, y = 110)  
delbutton.place(x = 40, y = 160)  
delallbutton.place(x = 250, y = 108)  
exitbutton.place(x = 250, y = 158)

connect = sql.connect('todo.db')
cursor = connect.cursor()
cursor.execute("create table if not exists tasks(title text)")

window.mainloop()