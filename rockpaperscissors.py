from random import randint
import tkinter as tk 

window = tk.Tk()
window.title("Rock Paper Scissor")
window.geometry("850x250")
window.resizable(0,0)
window.configure(background="bisque")

rockcimg="""
   ^^^^^^^^^^^^^^^^ 
   ^     ROCK     ^ 
   ^^^^^^^^^^^^^^^^
"""
papercimg ="""
   ^^^^^^^^^^^^^^^^ 
   ^     PAPER    ^ 
   ^^^^^^^^^^^^^^^^
"""

scissorscimg ="""
   ^^^^^^^^^^^^^^^^ 
   ^   SCISSOR    ^ 
   ^^^^^^^^^^^^^^^^
"""

rockimg = """
   ^^^^^^^^^^^^^^^^ 
   ^     ROCK     ^ 
   ^^^^^^^^^^^^^^^^
"""
paperimg ="""
   ^^^^^^^^^^^^^^^^ 
   ^    PAPER     ^ 
   ^^^^^^^^^^^^^^^^
"""
scissorsimg ="""
   ^^^^^^^^^^^^^^^^ 
   ^   SCISSOR    ^ 
   ^^^^^^^^^^^^^^^^
"""


labelc =tk.Label(window,text=rockcimg,bg="bisque")
labelc.grid(row=2,column=1)
label = tk.Label(window,text=rockimg,bg="bisque")
label.grid(row=2,column=5)

scorec = tk.Label(window,text=0,font=100,bg="bisque",fg="black")
scorec.grid(row=2,column=2)
score = tk.Label(window,text=0,font=100,bg="bisque",fg="black")
score.grid(row=2,column=4)

name = tk.Label(window,font=50,text="COMPUTER",bg="bisque",fg="black")
name.grid(row=1,column=1)
name2 = tk.Label(window,font=50,text="YOU",bg="bisque",fg="black")
name2.grid(row=1,column=5)

result = tk.Label(window,font=50,bg="bisque",fg="black")
result.grid(row=3,column=3)

def res(e):
    result['text'] = e

def scrc():
    scre = int(scorec["text"])
    scre += 1
    scorec["text"] = str(scre)

def scr():
    scre = int(score["text"])
    scre += 1
    score["text"] = str(scre)

def win(player,computer):
    if player == computer:
        res( "TIE !!!")
    elif player == "rock":
        if computer == "paper":
            res("YOU LOOSE !!")
            scrc()
        else:
            res("YOU WIN !!")
            scr()
    elif player == "paper":
        if computer == "scissor":
            res("YOU LOOSE !!")
            scrc()
        else:
            res("YOU WIN !!")
            scr()
    elif player == "scissor":
        if computer == "rock":
            res("YOU LOOSE !!")
            scrc()
        else:
            res("YOU WIN !!")
            scr()
    else:
        pass

choose=["rock","paper","scissors"]

def choice(e):

    choosec = choose[randint(0,2)]
    if choosec == "rock":
        labelc.configure(text=rockcimg)
    elif choosec == "paper":
        labelc.configure(text=papercimg)
    else:
        labelc.configure(text=scissorscimg)

    if e=="rock":
        label.configure(text=rockimg)
    elif e=="paper":
        label.configure(text=paperimg)
    else:
        label.configure(text=scissorsimg)

    win(e,choosec)


rockb = tk.Button(window,width=20,height=2,text="ROCK",bg="red",command=lambda:choice("rock"))
rockb.grid(row=4,column=2)
paperb = tk.Button(window,width=20,height=2,text="PAPER",bg="blue",command=lambda:choice("paper"))
paperb.grid(row=4,column=4)
scissorsb = tk.Button(window,width=20,height=2,text="SCISSORS",bg="yellow",command=lambda:choice("scissors"))
scissorsb.grid(row=4,column=3)

window.mainloop()
