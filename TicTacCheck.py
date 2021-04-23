# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 22:04:03 2021

@author: proce
"""

def checkBoard(board, size, player):
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
                    if grid[row][col] == 0:
                        return False
            return True
        
        if checkCol(grid, size) or checkRow(grid, size) or checkDiagonal(grid, size):
            player.setWinner()

        

def ComputerPlayer(board, player, size):
    import random 
    #TODO implement
    def isFree(board, move):
        return board[move]==0
    
    move = random.randint(0,len(board)-1)
    if isFree(board, move) and onBoard(move, board):
        board[move] = player.marker
        return True
    else:
        return ComputerPlayer(board, player, size)

       
def onBoard(userMove, board):
    if userMove >= len(board) or userMove < 0:
        return False
    return True

def makeMove(board, player, userMove, size):
    def convertMove(userMove, size):
        return userMove[0] + userMove[1]*size

    #TODO: update for use of GUI 
    move = convertMove(userMove,size)
    if onBoard(move, board) and board[move] == 0:
        board[move] = player.marker
        return True
    else:
        print("Invalid move. Try again")
        return False