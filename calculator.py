import tkinter as tk
import math
 
window = tk.Tk()
window.geometry("325x330")
window.resizable(0, 0)
window.title("Calculator")
window.eval('tk::PlaceWindow . center')

operation = ""
result = tk.StringVar()
 
def on_click(data):
    global operation
    operation = operation + str(data)
    result.set(operation)
 
def clear_click(): 
    global operation 
    operation = "" 
    result.set("")
  
def equal_click():
    global operation
    output = str(eval(operation))
    result.set(output)
    operation = ""

frame = tk.Frame(window, width=350, height=70, bd=0, highlightbackground="#EEE0E5", highlightcolor="#eee", highlightthickness=4)
frame.pack(side = tk.TOP)

field = tk.Entry(frame, font=('arial', 18, 'bold'), textvariable = result, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
field.grid(row=0, column=0)
field.pack(ipady=10)

framebutton = tk.Frame(window, width=312, height=272.5, bg="#eee")
framebutton.pack()

b0 = tk.Button(framebutton, text = "0", fg = "black", width = 23, height = 3, bd = 0, bg = "#EEE0E5", cursor = "hand2", command = lambda: on_click(0))
b0.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

b1 = tk.Button(framebutton, text = "1", fg = "black", width = 11, height = 3, bd = 0, bg = "#EEE0E5", command = lambda: on_click(1))
b1.grid(row = 3, column = 0, padx = 1, pady = 1)

b2 = tk.Button(framebutton, text = "2", fg = "black", width = 11, height = 3, bd = 0, bg = "#EEE0E5", cursor = "hand2", command = lambda: on_click(2))
b2.grid(row = 3, column = 1, padx = 1, pady = 1)

b3 = tk.Button(framebutton, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#EEE0E5", cursor = "hand2", command = lambda: on_click(3))
b3.grid(row = 3, column = 2, padx = 1, pady = 1)

b4 = tk.Button(framebutton, text = "4", fg = "black", width = 11, height = 3, bd = 0, bg = "#EEE0E5", cursor = "hand2", command = lambda: on_click(4))
b4.grid(row = 2, column = 0, padx = 1, pady = 1)
  
b5 = tk.Button(framebutton, text = "5", fg = "black", width = 11, height = 3, bd = 0, bg = "#EEE0E5", cursor = "hand2", command = lambda: on_click(5))
b5.grid(row = 2, column = 1, padx = 1, pady = 1)
  
b6 = tk.Button(framebutton, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#EEE0E5", cursor = "hand2", command = lambda: on_click(6))
b6.grid(row = 2, column = 2, padx = 1, pady = 1)

b7 = tk.Button(framebutton, text = "7", fg = "black", width = 11, height = 3, bd = 0, bg = "#EEE0E5", cursor = "hand2", command = lambda: on_click(7))
b7.grid(row = 1, column = 0, padx = 1, pady = 1)
  
b8 = tk.Button(framebutton, text = "8", fg = "black", width = 11, height = 3, bd = 0, bg = "#EEE0E5", cursor = "hand2", command = lambda: on_click(8))
b8.grid(row = 1, column = 1, padx = 1, pady = 1)
  
b9 = tk.Button(framebutton, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#EEE0E5", cursor = "hand2", command = lambda: on_click(9))
b9.grid(row = 1, column = 2, padx = 1, pady = 1)

clear= tk.Button(framebutton, text = "C", fg = "black", width = 23, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: clear_click())
clear.grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)
  
div = tk.Button(framebutton, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: on_click("/"))
div.grid(row = 0, column = 3, padx = 1, pady = 1)

pow = tk.Button(framebutton, text = "^", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: on_click("**"))
pow.grid(row = 0, column = 2, padx = 1, pady = 1)
  
mul= tk.Button(framebutton, text = "X", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: on_click("*"))
mul.grid(row = 1, column = 3, padx = 1, pady = 1)

sub = tk.Button(framebutton, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: on_click("-"))
sub.grid(row = 2, column = 3, padx = 1, pady = 1)
  
add = tk.Button(framebutton, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: on_click("+"))
add.grid(row = 3, column = 3, padx = 1, pady = 1)
  
dot= tk.Button(framebutton, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: on_click("."))
dot.grid(row = 4, column = 2, padx = 1, pady = 1)
  
equal = tk.Button(framebutton, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: equal_click())
equal.grid(row = 4, column = 3, padx = 1, pady = 1)

window.mainloop()