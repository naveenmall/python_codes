from tkinter import *
import tkinter.messagebox

#  This is my first game

root = Tk()
root.title("Tic Tac Toe")
click = True


def on_enter(event):
    b1.config(bg="#54a0ff")


def on_leave(event):
    b1.config(bg="#0abde3")


def tictactoe(button):
    global click
    if button["text"] == "" and click == True:
        #  button["text"] = "X"
        button.config(text="X")
        click = False
    elif button["text"] == "" and click == False:
        button["text"] = "O"
        click = True

    if (b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or
        b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" or
        b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or
        b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or
        b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or
        b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" or
        b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or
        b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X"):
        tkinter.messagebox.showinfo("player x wins", "player x wins")
    elif (b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or
        b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" or
        b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" or
        b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or
        b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" or
        b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O" or
        b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" or
        b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O"):
        tkinter.messagebox.showinfo("player o wins", "player o wins")


b1 = Button(root, text="", font="courier 30 bold", width=4, height=2, bg="#e67e22", bd=5, command=lambda: tictactoe(b1))
b1.grid(row=0, column=0, sticky=E+W+N+S)
b2 = Button(root, text="", font="courier 30 bold", width=4, height=2, bg="#16a085", bd=5, command=lambda: tictactoe(b2))
b2.grid(row=0, column=1, sticky=E+W+N+S)
b3 = Button(root, text="", font="courier 30 bold", width=4, height=2, bg="#e67e22", bd=5, command=lambda: tictactoe(b3))
b3.grid(row=0, column=2, sticky=E+W+N+S)
b4 = Button(root, text="", font="courier 30 bold", width=4, height=2, bg="#16a085", bd=5, command=lambda: tictactoe(b4))
b4.grid(row=1, column=0, sticky=E+W+N+S)
b5 = Button(root, text="", font="courier 30 bold", width=4, height=2, bg="#e67e22", bd=5, command=lambda: tictactoe(b5))
b5.grid(row=1, column=1, sticky=E+W+N+S)
b6 = Button(root, text="", font="courier 30 bold", width=4, height=2, bg="#16a085", bd=5, command=lambda: tictactoe(b6))
b6.grid(row=1, column=2, sticky=E+W+N+S)
b7 = Button(root, text="", font="courier 30 bold", width=4, height=2, bg="#e67e22", bd=5, command=lambda: tictactoe(b7))
b7.grid(row=2, column=0, sticky=E+W+N+S)
b8 = Button(root, text="", font="courier 30 bold", width=4, height=2, bg="#16a085", bd=5, command=lambda: tictactoe(b8))
b8.grid(row=2, column=1, sticky=E+W+N+S)
b9 = Button(root, text="", font="courier 30 bold", width=4, height=2, bg="#e67e22", bd=5, command=lambda: tictactoe(b9))
b9.grid(row=2, column=2, sticky=E+W+N+S)

b1.bind("<Enter>", on_enter)
b1.bind("<Leave>", on_leave)




root.mainloop()
