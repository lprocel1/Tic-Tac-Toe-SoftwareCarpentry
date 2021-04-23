# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 01:42:36 2021

@author: proce
"""


def StartUpWindow():
    import tkinter as tk

    def getinput():
        global player1
        global player2
        player1 = player1name.get()
        player2 = player2name.get()
        startup.destroy()

    startup = tk.Tk()
    # label_object.grid(row,col)
    startup.title("tic-tac-toe startup!")
    tk.Label(startup, text="welcome to two-player tic-tac-toe!", font="20").grid(
        columnspan=2, row=0, column=0
    )
    tk.Label(startup, text="enter player names below, then click 'submit'").grid(
        columnspan=2, row=1, column=0
    )

    tk.Label(startup, text="User 1: ").grid(row=2, column=0)
    tk.Label(startup, text="User 2: ").grid(row=3, column=0)
    # https://codeloop.org/how-to-create-textbox-in-python-tkinter/
    # e1 = tk.StringVar()
    player1name = tk.Entry(startup)
    player1name.grid(row=2, column=1)
    # e2 = tk.StringVar()
    player2name = tk.Entry(startup)
    player2name.grid(row=3, column=1)
    submit = tk.Button(startup, text="Submit", command=getinput)
    submit.grid(columnspan=2, row=4, column=0)
    startup.mainloop()
    return [player1, player2]


if __name__ == "__main__":
    players = StartUpWindow()
    print(players)
