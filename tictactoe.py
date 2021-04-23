# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 22:28:31 2021

@author: proce
"""


def tictactoeGame():
    import StartUpWindow as start
    from Player import Player, CurrentPlayer
    import WindowAttempt as wd

    players = start.StartUpWindow()
    size = 3
    player1 = Player(1, players[0])
    player1.setPlayStatus(True)
    player2 = Player(2, players[1])
    player = CurrentPlayer(player1, player2)
    wd.Window(player, size)
