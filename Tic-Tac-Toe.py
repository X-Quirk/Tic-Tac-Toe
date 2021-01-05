
board=[' ' for i in range(10)] #Board is a list to hols the position from 1 to 9
                               #i.e all the positions in the board
                               #We are usinf 10 indices and avoiding the 0th index to identify the
                               #positions easily , also used to empty the board for new game

def characterInput(char,pos): #Input for X or O in board at the specified position
    board[pos]=char #Placinng the character in the correct position

def isSpaceFree(pos): #Checking if the position is free
    return board[pos]==" "

def isBoardFull(board): #Checking if board is full
    if board.count(' ') > 1: #If there exists atleast one free space on board, it is not full
        return False
    else:
        return True

def isWinner(b,l): #Checking for all win states
    return ((b[1]==l and b[2]==l and b[3]==l)or
            (b[4]==l and b[5]==l and b[6]==l)or
            (b[7]==l and b[8]==l and b[9]==l)or
            (b[1]==l and b[4]==l and b[7]==l)or
            (b[2]==l and b[5]==l and b[8]==l)or
            (b[3]==l and b[6]==l and b[9]==l)or
            (b[1]==l and b[5]==l and b[9]==l)or
            (b[3]==l and b[5]==l and b[7]==l))     

def playerMove(): #For move made by Player
    while True:
        print()
        move=input("Select a Position to place X : ") #Inputting the position
        print()
        try:
            move=int(move) #Converting position to int, as we need position to to integer type
                           #in the list
            if move>0 and move<10: #Checking for valid position
                if isSpaceFree(move): #Checking whether the position is free or not
                    characterInput("X",move) #Placing X on the board
                    break
                else: #If the position is already occupied
                    print(move,"th space is already occupied !") 
            else: #If the position was out of range 
                  #i.e not in between 1 and 9
                print("Please select a position between 1 and 9")
                
        except: #If player inputted something else
            print("Please enter a Number !") 


def computerMove(): #For move by computer
    possibleMoves=[x for x ,i in enumerate(board) if i==" " and x!=0 ] #Finding free spaces for computer to place the character
    move=0
    for i in ["O","X"]: #For computer to place the character in the board
        for j in possibleMoves: #Checking if free space available
            boardcopy=board[:]  #Makes a copy of the board 
            boardcopy[j]=i      #Places the character in the free space
            if isWinner(boardcopy,i): #Checks if computer can win 
                move=j
                return move


    #Best way to win, is to check the corners first then the middle piece then the edges

    corners=[] #Checking if corners are available
    for i in possibleMoves:
        if i in [1,3,7,9]:
            corners.append(i)
    if len(corners)>0: #If corners are available selecting a random corner
        move=selectRandom(corners)
        return move


    if 5 in possibleMoves: #Checking if the middle piece is available
        move=5
        return move


    edges=[] #Checking if edges are available
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edges.append(i)
        if len(edges)>0:
            move=selectRandom(edges)
            return move
    return move


def selectRandom(li):
    import random
    r=random.choice(li) #Choosing a random position from the list
    return r

def main():
    print()
    print("Welcome to Tic Tac Toe !")
    print("Take a look at the positions")
    demoBoard()
    while not(isBoardFull(board)):
        if not(isWinner(board,"O")):
            playerMove()
            printBoard(board)
        else:
            print("You LOST !")
            print("COMPUTER WON !")
            break
        if not(isWinner(board,"X")):
            move=computerMove()
            if move==0:
                print("")
            else:
                characterInput("O",move)
                print("COMPUTER Places O in Position : {} .".format(move))
                printBoard(board)
        else:
            print("CONFRATULATIONS !!!")
            print("You WON !")
            print("COMPUTER LOST !")
            break
            

    if isBoardFull(board):
        print()
        print("TIE GAME !!")
        print()



def demoBoard(): #Shows the positions in the board
    print()
    print(" ----------------- ")
    print("|     |     |     |")
    print("|  1  |  2  |  3  |")
    print("|     |     |     |")
    print(" ----------------- ")
    print("|     |     |     |")
    print("|  4  |  5  |  6  |")
    print("|     |     |     |")
    print(" ----------------- ")
    print("|     |     |     |")
    print("|  7  |  8  |  9  |")
    print("|     |     |     |")
    print(" ----------------- ")
    print()

def printBoard(board): #Shows the basic Board
                       #Problem with using the GUI for board like this is that
                       #we can only use a single character in a box to get the perfect board interface
    print()
    print(" ----------------- ")
    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(board[1],board[2],board[3]))
    print("|     |     |     |")
    print(" ----------------- ")
    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(board[4],board[5],board[6]))
    print("|     |     |     |")
    print(" ----------------- ")
    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(board[7],board[8],board[9]))
    print("|     |     |     |")
    print(" ----------------- ")
    print()


b=1   #Varible used to detemine whether this is the first game or not.
while b>0:
    if b==1: #Checking whether this is the first game or not
        board=[" " for i in range(10)] #Emptying the board for the new game
        print("===============================================")
        print()
        main()
    else:
        print("Do you want to Play again ? (Y/N)")
        respos=["yes","y","yeah","yea","yup","yep"]
        resneg=["nope","n","never","no"]
        r=input()
        r=r.lower()
        if r in respos:
            board=[" " for i in range(10)] #Emptying the board for the new game
            print("===============================================")
            print()
            print("----------------- NEW GAME -------------------")
            main()
        elif r in resneg:
            exit(0)
        else:
            while r not in respos or resneg:
                print()
                print("Sorry I didn't get that !")
                print("Please input again ,")
                print("Do you want to Play agian ? Y/N")
                r=input()
                r=r.lower()
                if r in respos:
                    board=[" " for i in range(10)]
                    print("===============================================")
                    print()
                    print("----------------- NEW GAME -------------------")
                    main()
                    break
                elif r in resneg:
                    exit(0)
    b=2

        