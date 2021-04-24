

def tictactoeGame():
    """
    Wrapper for the TicTacToe game.

    Returns
    -------
    None.

    """
    import SelectionMenu as sm
    import StartUpWindow as start
    from Player import Player, CurrentPlayer
    import WindowAttempt as wd
    import ComputerWindow as cwd

    [size, comp] = sm.Selection()
    if comp == "Single Player":
        players = start.StartUpCompWindow()
    else:
        players = start.StartUpWindow()
    player1 = Player(1, players[0])
    player1.setPlayStatus(True)
    player2 = Player(2, players[1])
    player = CurrentPlayer(player1, player2)
    if comp == "Single Player":
        cwd.CompWindow(player, size)
    else:
        wd.Window(player, size)
