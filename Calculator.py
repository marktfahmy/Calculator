import tkinter as tk
import math

def takeInput(input):
    global out_str
    if input != "=":
        out_str += str(input)
        out_box.configure(text=out_str)
    else:
        orig_str = out_str
        out_str = str(eval(out_str))
        out_box.configure(text=orig_str+"="+out_str)
        
def clear():
    global out_str
    out_str = ""
    out_box.configure(text="")

root = tk.Tk()

out_box = tk.Label(font=('Verdana',36),bg='white')
out_str = ""
out_box.grid(row=0,column=0)
button_frame = tk.Frame()
button_frame.grid(row=1, column=0)
buttons = [0 for i in range(9)]
nums = "123456789"
operators = [0 for i in range(4)]
ops = ["+","-","*","/"]
for i in range(9):
    buttons[i] = tk.Button(button_frame,font=('Verdana', 36),text=nums[i],command=lambda x=i:takeInput(nums[x]))
    buttons[i].grid(row=math.floor(i/3),column=i%3,sticky="EW")
for i in range(4):
    button_frame.grid_columnconfigure(i,weight=1)
    operators[i] = tk.Button(button_frame,font=('Verdana', 36),text=ops[i],command=lambda x=i:takeInput(ops[x]))
    operators[i].grid(row=i,column=3,sticky="EW")
clear_button = tk.Button(button_frame,font=('Verdana', 36),text="C",command=clear)
zero_button = tk.Button(button_frame,font=('Verdana', 36),text="0",command=lambda:takeInput(0))
equal_button = tk.Button(button_frame,font=('Verdana', 36),text="=",command=lambda:takeInput("="))
clear_button.grid(row=3,column=0,sticky="EW")
zero_button.grid(row=3,column=1,sticky="EW")
equal_button.grid(row=3,column=2,sticky="EW")

tk.mainloop()
