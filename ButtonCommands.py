
import TicTacCheck as TTC
from PIL import Image, ImageTk
import tkinter as tk

def displayWinner(root,player):

    """
    Display the winning Player's name along with congratulations image.

    Parameters
    ----------
    root : TK() window
        Board Window containing the game board.
    player : CurrentPlayer object
        Current player to select a button.

    Returns
    -------
    None.

    """

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
    

def displayCompWinner(root,player):
    """
    Display the end results of the single person game.

    Parameters
    ----------
    root : TK() window
        Board Window containing the game board.
    player : CurrentPlayer object
        Current player to select a button.

    Returns
    -------
    None.

    """
    root.destroy()
    winDoe = tk.Tk()
    winDoe.geometry('500x500')
    if player.name != 'Computer':
        tk.Label(winDoe, text="Congratulations, " + player.name+"!").grid(column=0,row=0, columnspan=3,sticky=tk.N+tk.E+tk.S+tk.W)
        im = Image.open('congratz.png')
    else:
        player.switchPlayers()
        tk.Label(winDoe, text="Sorry, " + player.name+"!").grid(column=0,row=0, columnspan=3,sticky=tk.N+tk.E+tk.S+tk.W)
        im = Image.open('loser.png')
    pic = ImageTk.PhotoImage(im)
    cv=tk.Canvas(winDoe)

    tk.Label(winDoe, image=pic).grid(row=1,column=0,columnspan=3,sticky=tk.N+tk.E+tk.S+tk.W)
    quitbtn = tk.Button(winDoe,text='Exit',command = lambda: winDoe.destroy()).grid(column=1, row=3)
    winDoe.mainloop()
    
def playCompButton(buttonlist, player, r, c, frame, size, root):
    """
    Command linked to button clicks during Single Player game, makes computer move.

    Parameters
    ----------
    buttonlist : list
        list of buttons on GUI window.
    player : CurrentPlayer object
        Current player to select a button.
    r : int
        Row of button selected by the computer.
    c : int
        Column of the button selected by the computer.
    frame : tk.Frame()
        Frame of board game window GUI.
    size : int
        Dimensions of Tic Tac Toe baord: size x size.
    root : Tk() window
        Board game window containing board of buttons.

    Returns
    -------
    None.

    """
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
        TTC.ComputerPlayer(board, player,size,buttonlist)
        if player.gameOver():
            displayWinner(root,player)
        else:
            player.switchPlayers()
          
    
def playButton(buttonlist, player, r, c, frame, size, root):
    """
    Make a move in Two-Player game by selecting a button.

    Parameters
    ----------
    buttonlist : list
        list of buttons on GUI window.
    player : CurrentPlayer object
        Current player to select a button.
    r : int
        Row of button selected by the player.
    c : int
        Column of the button selected by the player.
    frame : tk.Frame()
        Frame of board game window GUI.
    size : int
        Dimensions of Tic Tac Toe baord: size x size.
    root : Tk() window
        Board game window containing board of buttons.

    Returns
    -------
    None.

    """

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


    
    
    