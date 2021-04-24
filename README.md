# Tic-Tac-Toe-SoftwareCarpentry

## Have you ever wanted to play Tic Tac Toe on the computer using a GUI window, just for fun? Do you want to try playing 3x3, 4x4, or 5x5 boards? Are you bored? Look no further. Grab a friend (or not) and check out this hand GUI-based game! This repository generates a customizable Tic Tac Toe game using GUIs in python.
#### Author: 
* Linda Procell, email: lprocel1@jhu.edu
### This code will generate a series of GUI windows with integrated buttons that allows users to play singe or multi=player Tic Tac Toe games. User input is required for use of this software. 

## INSTALLATION
### Download the entire code package, and make sure that you are able to access the tkinter, PIL, and random libraries. All files must be in the same folder, including image (*png) files.

## OPERATING INSTRUCTIONS
### 
In order to run the code successfully, download the entire package into an accessible location. There are two ways to run the software: one is to open the RUN.py file in a python console and run it. Another is to open a command prompt, type "import tictactoe", then "tictactoeGame()". Both should launch the initial Selection GUI needed to customize the Tic Tac Toe game board for play. 
Game Progression:
* Selection window allows user to select Single or Multiplayer game as well as board size
* Startup windows asks for player names to be input
* Board is generated and users can click on buttons to make moves
* Game ends when all buttons have been clicked or if a player wins the game
Upon completion of the game (if a player wins or the board is filled) the board will terminate and a new window displaying a message is generated. This message differs based on the output of the game and is tied to the *.png files included in this repository. 
 
Good Luck! 
###

## FILE MANIFEST 
###  Python Code List:
* ButtonCommands.py
* ComputerWindow.py
* Player.py
* RUN.py
* SelectionMenu.py
* StartUpWindow.py
* TicTacCheck.py
* tictactoe.py
* WindowAttempt.py
### Images:
* loser.png (created with Pusheen icons in Microsoft PowerPoint)  
* congratz.png (created with Pusheen icons in Microsoft PowerPoint) 
* tie.png (created with Pusheen icons in Microsoft PowerPoint)  


## TROUBLESHOOTING
### 
This code is designed to take user input for the game to run and will throw errors if closed early. Potential errors that may occur happen when users do not select parameters during the initial selection window, or do not enter their names and click the 'submit' buttons present on each window. Attempts were made to account for lack of user input for critical parameters, but potential bugs may arise during use of software. 
Once critical input that could not be corrected for is the 'size' parameter generated during the first GUI interaction. No selection of this parameter leads to program termination.
As mentioned in the Installation instructions, files should be stored in a single location together, alongside the *png imgaes.
Finally, there is a discrepancy in use of tkinter vs. Tkinter (note the capital T) between python3 and python2. please ensure that, if using python2, all files incuding the statement "import tkinter as tk" are corrected to read "import Tkinter as tk".
###

## FUTURE IMPROVEMENTS
### 
Due to inexperience with AI and prediction modelling, Single Player Game mode is incredibly easy to beat. Future improvements should be made to create a harder computer opponent that is not based on random moves. Corrections could also be made to circumvent immediate failure if no 'size' parameter is selected.
Stylistically, improvements can also be made to the GUI windows to encorporate more color, fonts, and button functionalities. Future updates could also allow for wasily resizable windows that maintian their dimensions. 
###
