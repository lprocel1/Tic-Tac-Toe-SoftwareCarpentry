
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
    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo #avoid garbage collection
    
    root.destroy()
    winDoe = tk.Tk()
    winDoe.geometry('900x600')
    tk.Label(winDoe, text="Congratulations, " + player.name+"!").pack()
    im = Image.open('congratz.png')

    copy_of_image = im.copy()
    photo = ImageTk.PhotoImage(im)
    label = tk.Label(winDoe, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=tk.BOTH, expand = tk.YES)

    cv=tk.Canvas(winDoe)
    quitbtn = tk.Button(winDoe,text='Exit',command = lambda: winDoe.destroy()).pack() 
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
    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo #avoid garbage collection
    
    root.destroy()
    winDoe = tk.Tk()
    winDoe.geometry('900x600')
    if player.name != 'Computer':
        tk.Label(winDoe, text="Congratulations, " + player.name+"!").pack()
        im = Image.open('congratz.png')
    else:
        player.switchPlayers()
        tk.Label(winDoe, text="Sorry, " + player.name+"!").pack()
        im = Image.open('loser.png')
    
    copy_of_image = im.copy()
    photo = ImageTk.PhotoImage(im)
    label = tk.Label(winDoe, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=tk.BOTH, expand = tk.YES)

    cv=tk.Canvas(winDoe)
    quitbtn = tk.Button(winDoe,text='Exit',command = lambda: winDoe.destroy()).pack() 
    winDoe.mainloop()
    
def displayTie(root,player):
    """
    Display the end results of the tied person game.

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
    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        label.config(image = photo)
        label.image = photo #avoid garbage collection
        
    root.destroy()
    winDoe = tk.Tk()
    winDoe.geometry('900x600')
    tk.Label(winDoe, text="Oops, it's a tie!").pack() 
    im = Image.open('tie.png')
    
    copy_of_image = im.copy()
    photo = ImageTk.PhotoImage(im)
    label = tk.Label(winDoe, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=tk.BOTH, expand = tk.YES)

    cv=tk.Canvas(winDoe)
    quitbtn = tk.Button(winDoe,text='Exit',command = lambda: winDoe.destroy()).pack() 
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
    if player.full and not player.gameOver():
        displayTie(root,player)
    elif player.gameOver():
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
    if player.full:
        displayTie(root,player)
    elif player.gameOver():
        displayWinner(root,player)
    else:
        player.switchPlayers()
        tk.Label(frame,text="It is "+ player.name + "'s turn").grid(column=0, row=1, columnspan=size+2)


    
    
    