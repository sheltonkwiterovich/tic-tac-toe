import random
gameOver = False
player1=""
player2=""
startPlayer = ""
secondPlayer = ""
playList = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
# make 9 box grid 
def grid ():
    row1 = "  "+ playList[0] + " | "+playList[1] +" | "+playList[2] +" "
    row2 = "  "+ playList[3] + " | "+playList[4] +" | "+playList[5] +" "
    row3 = "  "+ playList[6] + " | "+playList[7] +" | "+playList[8] +" "
    
    print(row1)
    print("-------------")
    print(row2)
    print("-------------")
    print(row3)

# get player names for 1 and 2
def playerNames ():
    global player1
    global player2
    player1=input("player 1 enter name here: ")
    player2=input("player 2 enter name here: ")

# randomly select who goes first 
def randomPlayer ():
    global startPlayer
    global secondPlayer
    num = random.randint(1,2)
    if num == 1:
        startPlayer = player1
        secondPlayer = player2
        print(player1 + " goes first!")
    else:
        startPlayer = player2
        secondPlayer = player1
        print(player2 + " goes first")

# player 1 put x in a space on the grid 
# player 2 put o in a space on the grid  
def playLetter(player, letter):
    playerInput = input("where would you like to play " + player +"? enter a number 1-9, one is top left, 9 is bottom right: ")
    spot = int(playerInput) - 1
    spotFull = True
    
    while spot > 8 or spot < 0:
        playerInput = input("that spot doesn't exist stupid! Pick another one: ")
        spot = int(playerInput) - 1

    while spotFull == True:
        if playList[spot] != " ":
            playerInput = input("that spot is full! Pick another one: ")
            spot = int(playerInput) - 1
        else:
            playList[spot] = letter
            spotFull = False

# goal: get 3 x's or o's in a row 
def gameWon(spot):
    global gameOver
    gameOver = True
    if playList[spot] == "x":
        grid()
        print(startPlayer + " won!")
    else:
        grid()
        print(secondPlayer + " won!")

def checkWin():
    global gameOver
    if playList[0] == playList[1] == playList[2] and playList[0] != " ":
        gameWon(0)
    elif playList[3] == playList[4] == playList[5] and playList[3] != " ":
        gameWon(3)
    elif playList[6] == playList[7] == playList[8] and playList[6] != " ":
        gameWon(6)
    elif playList[0] == playList[3] == playList[6] and playList[0] != " ":
        gameWon(0)
    elif playList[1] == playList[4] == playList[7] and playList[1] != " ":
        gameWon(1)
    elif playList[2] == playList[5] == playList[8] and playList[2] != " ":
        gameWon(2)
    elif playList[0] == playList[4] == playList[8] and playList[0] != " ":
        gameWon(0)
    elif playList[2] == playList[4] == playList[6] and playList[2] != " ":
        gameWon(2)
    elif (" " not in playList):
        gameOver = True
        grid()
        print("CAT")

def playAgain():
    again = input("do you want to play again? y for yes, n for no: ")
    if again == "y":
        global playList
        global gameOver
        for i in range(0, len(playList)):
            playList[i] = " "
        gameOver = False
        playGame()

def playGame():
    global gameOver
    playerNames()
    randomPlayer()
    grid()
    playLetter(startPlayer,"x")
    while gameOver == False:
        grid()
        playLetter(secondPlayer,"o")
        checkWin()
        if gameOver == True:
            playAgain()
            break
        grid()
        playLetter(startPlayer,"x")
        checkWin() 
    else: 
        playAgain()
    
playGame()