from tkinter import *
from tkinter import messagebox

root = Tk()
topFrame = Frame(root)
topFrame.pack()


def callback(event):
    event.widget['text'] = 'X'
    if not checkIfWin():
        botGo()
        checkIfLose()
    #wthread.wit(time)


def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxA(0, text, title, style)


def checkIfWin():
    if button1['text'] == "X" and button2['text'] == "X" and button3['text'] == "X":
        messagebox.showinfo("Message", "Congratulations!\nYou Win")
        return True
    elif button4['text'] == "X" and button5['text'] == "X" and button6['text'] == "X":
        messagebox.showinfo("Message", "Congratulations!\nYou Win")
        return True
    elif button7['text'] == "X" and button8['text'] == "X" and button9['text'] == "X":
        messagebox.showinfo("Message", "Congratulations!\nYou Win")
        return True
    elif button1['text'] == "X" and button4['text'] == "X" and button7['text'] == "X":
        messagebox.showinfo("Message", "Congratulations!\nYou Win")
        return True
    elif button2['text'] == "X" and button5['text'] == "X" and button8['text'] == "X":
        messagebox.showinfo("Message", "Congratulations!\nYou Win")
        return True
    elif button3['text'] == "X" and button6['text'] == "X" and button9['text'] == "X":
        messagebox.showinfo("Message", "Congratulations!\nYou Win")
        return True
    elif button1['text'] == "X" and button5['text'] == "X" and button9['text'] == "X":
        messagebox.showinfo("Message", "Congratulations!\nYou Win")
        return True
    elif button3['text'] == "X" and button5['text'] == "X" and button7['text'] == "X":
        messagebox.showinfo("Message", "Congratulations!\nYou Win")
        return True
    else:
        return False


def checkIfLose():
    if button1['text'] == "O" and button2['text'] == "O" and button3['text'] == "O":
        messagebox.showinfo("Message", "You Lose!")
        return True
    elif button4['text'] == "O" and button5['text'] == "O" and button6['text'] == "O":
        messagebox.showinfo("Message", "You Lose!")
        return True
    elif button7['text'] == "O" and button8['text'] == "O" and button9['text'] == "O":
        messagebox.showinfo("Message", "You Lose!")
        return True
    elif button1['text'] == "O" and button4['text'] == "O" and button7['text'] == "O":
        messagebox.showinfo("Message", "You Lose!")
        return True
    elif button2['text'] == "O" and button5['text'] == "O" and button8['text'] == "O":
        messagebox.showinfo("Message", "You Lose!")
        return True
    elif button3['text'] == "O" and button6['text'] == "O" and button9['text'] == "O":
        messagebox.showinfo("Message", "You Lose!")
        return True
    elif button1['text'] == "O" and button5['text'] == "O" and button9['text'] == "O":
        messagebox.showinfo("Message", "You Lose!")
        return True
    elif button3['text'] == "O" and button5['text'] == "O" and button7['text'] == "O":
        messagebox.showinfo("Message", "You Lose!")
        return True
    else:
        return False


def botGo():
    for button in allOptions:
        if button['text'] == "X" or button['text'] == "O":
            allOptions.remove(button)
    allOptions[0]['text'] = "O"
    allOptions.remove(allOptions[0])


button1 = Button(topFrame, text="  ", fg="black", font=("Arial", 14))
button1.bind("<Button-1>", callback)

button2 = Button(topFrame, text="  ", fg="black", font=("Arial", 14))
button2.bind("<Button-1>", callback)

button3 = Button(topFrame, text="  ", fg="black", font=("Arial", 14))
button3.bind("<Button-1>", callback)

button4 = Button(topFrame, text="  ", fg="black", font=("Arial", 14))
button4.bind("<Button-1>", callback)

button5 = Button(topFrame, text="  ", fg="black", font=("Arial", 14))
button5.bind("<Button-1>", callback)

button6 = Button(topFrame, text="  ", fg="black", font=("Arial", 14))
button6.bind("<Button-1>", callback)

button7 = Button(topFrame, text="  ", fg="black", font=("Arial", 14))
button7.bind("<Button-1>", callback)

button8 = Button(topFrame, text="  ", fg="black", font=("Arial", 14))
button8.bind("<Button-1>", callback)

button9 = Button(topFrame, text="  ", fg="black", font=("Arial", 14))
button9.bind("<Button-1>", callback)

allOptions = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

button1.grid(row=1, column=1)
button2.grid(row=1, column=2)
button3.grid(row=1, column=3)
button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
button6.grid(row=2, column=3)
button7.grid(row=3, column=1)
button8.grid(row=3, column=2)
button9.grid(row=3, column=3)
root.mainloop()
