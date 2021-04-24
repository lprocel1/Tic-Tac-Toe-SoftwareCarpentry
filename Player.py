
MARKER = ['+','o', 'x']

class CurrentPlayer:
    def __init__(self, player1, player2):
        self.setMarker(player1,player2)
        self.setName(player1, player2)
        self.playerStorage=[player1,player2]
        self.full=False
    
    def setMarker(self, player1, player2):
        if player1.playing:
            self.marker=player1.marker
        else: self.marker=player2.marker
        
    def setName(self, player1, player2):
        if player1.playing:
            self.name=player1.name
        else: self.name=player2.name
    
    def switchPlayers(self):
        player1 = self.playerStorage[0] 
        player2 = self.playerStorage[1]
        if player1.playing == True:
            player1.setPlayStatus(False)
            player2.setPlayStatus(True)
        else:
            player2.setPlayStatus(False)
            player1.setPlayStatus(True)
        self.setMarker(player1, player2)
        self.setName(player1, player2)
        
    def isFull(self):
        self.full = True
        print(self.full)
        
    def gameOver(self):
        if self.playerStorage[0].win or self.playerStorage[1].win:
            return True
        
    def setWinner(self):
        for user in self.playerStorage:
            if user.marker == self.marker:
                user.winner(True)
    
    def getPlayerName(self,playerNum):
        return self.playerStorage[playerNum-1].name

class Player:
    def __init__(self, playerVal, playerName, marker=None):
        self.player = playerVal
        self.name = playerName
        self.setMarker(playerVal,marker)
        self.setPlayStatus(playBool = False)
        self.winner(False)
        
    def __call__(self):
        if self.player == 0:
            return [str(self.name), 'Player #2', 'Marker = "' + str(self.marker) + '"']
        else:
            return [str(self.name),'Player #' + str(self.player), 'Marker = "' + str(self.marker) + '"']
    
    def setPlayStatus(self, playBool):
        self.playing = playBool
        
    def setMarker(self, playerVal, marker):
        if marker is not None:
            self.marker = marker
        else:
            self.marker = MARKER[playerVal]
            
    def winner(self, winBool):
        self.win = winBool