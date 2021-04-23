# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:49:11 2021

@author: proce
"""
import TicTacCheck as TTC
from PIL import Image, ImageTk
import tkinter as tk

def displayWinner(root,player):
    root.destroy()
    winDoe = tk.Tk()
    winDoe.geometry('500x500')
    tk.Label(winDoe, text="Congratulations, " + player.name+"!").grid(column=0,row=0, columnspan=3,sticky=tk.N+tk.E+tk.S+tk.W)
    im = Image.open('congratz.png')
    pic = ImageTk.PhotoImage(im)
    cv=tk.Canvas(winDoe)

    tk.Label(winDoe, image=pic).grid(row=1,column=0,columnspan=3,sticky=tk.N+tk.E+tk.S+tk.W)
    quitbtn = tk.Button(winDoe,text='Exit',command = lambda: winDoe.destroy()).grid(column=1, row=3)
    winDoe.mainloop()
    
    
    
def playButton(buttonlist, player, r, c, frame, size, root):
    buttonlist[r][c]['text']=player.marker
    buttonlist[r][c]['state'] = 'disabled'
    board = []
    for row in buttonlist:
        for btn in row:
            board.append(btn['text'])
    
    TTC.checkBoard(board, size, player)
    if player.gameOver():
        displayWinner(root,player)
    else:
        player.switchPlayers()
        tk.Label(frame,text="It is "+ player.name + "'s turn").grid(column=0, row=1, columnspan=size+2)


    
    
    