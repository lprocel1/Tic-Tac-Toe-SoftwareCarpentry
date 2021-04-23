# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 17:37:32 2021

@author: proce
"""

import ButtonCommands as BC
import tkinter as tk


def Window(player, size):
    root = tk.Tk()
    tk.Grid.rowconfigure(root, 0, weight=1)
    tk.Grid.columnconfigure(root, 0, weight=1)
    root.geometry("500x500")
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
    tk.Label(frame, text="This is the Tic Tac Toe Board").grid(
        column=0, row=0, columnspan=5
    )
    tk.Label(frame, text="It is " + player.name + "'s turn").grid(
        column=0, row=1, columnspan=size + 2
    )
    widget = 2

    buttonlist = [[0 for i in range(size)] for h in range(size)]
    for row in range(size):
        tk.Grid.rowconfigure(frame, row + widget, weight=1)
        for col in range(size):
            tk.Grid.columnconfigure(frame, col, weight=1)
            button1 = tk.Button(
                frame,
                text=" ",
                command=lambda r=row, c=col: BC.playButton(
                    buttonlist, player, r, c, frame, size, root
                ),
            )
            button1.grid(column=col, row=row + widget, sticky=tk.N + tk.E + tk.S + tk.W)
            buttonlist[row][col] = button1
    tk.Grid.rowconfigure(frame, size + widget + 1, weight=1)
    tk.Grid.columnconfigure(frame, int(size / 2), weight=1)
    quitbtn = tk.Button(frame, text="Exit", command=lambda: root.destroy()).grid(
        column=int(size / 2), row=size + widget + 1
    )
    root.mainloop()
