
def checkBoard(board, size, player):
    """
    Check the Tic Tac Toe board for a winner

    Parameters
    ----------
    board : list
        List of strings that represent the game board button text.
    size : int
        Dimensions of Tic Tac Toe baord: size x size.
    player : CurrentPlayer object
        Current player making a move.

    Returns
    -------
    None.

    """
    grid = [[0 for a in range(size)] for b in range(size)]
    for i in range(len(board)):
        grid[int(i/size)][int(i%size)] = board[i]
        
    def checkCol(grid, size):
        for col in range(size):
            markersum=0
            for row in range(size):
                if grid[row][col] == player.marker:
                    markersum +=1
            if markersum == size:
                return True
        return False    
                    
    def checkRow(grid, size):
        for row in range(size):
            markersum=0
            for col in range(size):
                if grid[row][col] == player.marker:
                    markersum +=1
            if markersum == size:
                return True
        return False
    
    def checkDiagonal(grid, size):
        forwardDiag = 0
        backwardDiag = 0
        for i in range(size):
            if grid[i][i] == player.marker:
                forwardDiag +=1
            if grid[size-i-1][size-i-1] == player.marker:
                backwardDiag+=1
        if forwardDiag == size or backwardDiag == size:
            return True
        return False
    
    def isFull(grid, size):
        for row in range(size):
            for col in range(size):
                if grid[row][col] == ' ':
                    return False
        return True
    
    if isFull(grid,size):
        player.isFull()

    if checkCol(grid, size) or checkRow(grid, size) or checkDiagonal(grid, size):
        player.setWinner()

def ComputerPlayer(board, player, size, buttonlist):
    """
    Make a computer move for Single Player games.

    Parameters
    ----------
    board : list
        List of strings that represent the game board button text.
    player : CurrentPlayer object
        Current player making a move.
    size : int
        Dimensions of Tic Tac Toe baord: size x size.
    buttonlist : list
        list of buttons on GUI window.

    Returns
    -------
    None.

    """
    import random
    def isFree(board, move):
        return board[move] == ' '
    
    move = random.randint(0,size*size)
    if isFree(board, move):
        board[move] = player.marker
        buttonlist[int(move/size)][int(move%size)]['text'] = player.marker
        buttonlist[int(move/size)][int(move%size)]['state']= 'disabled'
        checkBoard(board, size, player)
    else:
        ComputerPlayer(board, player, size, buttonlist)

       
def onBoard(userMove, board):
    """ Check to see if move is on board"""
    if userMove >= len(board) or userMove < 0:
        return False
    return True
