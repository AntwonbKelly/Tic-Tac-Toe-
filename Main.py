import sys

#Things to fix
#-------------

#Fix all the spaces being filled and game not ending

#Fix player choosing row thats already full.

def Player1Method (): #Method for player 1's turn
    print("Player 1 you're up! Where would you like to go on the board?")
    print("Enter top to choose a space on the top row")
    print("Enter mid to choose a space on the middle row")
    print("Enter bot to choose a space on the bottom row")
    UserInput = input()
    Player1Choice = False;  # While player1 hasn't chosen a valid choice
    global TopCounter #Uses Global variable named TopCounter thats outside of method
    global MidCounter #Uses Global variable named MidCounter thats outside of method
    global BotCounter #Uses Global variable named BottomCounter thats outside of method
    while (Player1Choice == False):
        if (UserInput in ["top", "Top", "TOP"] and TopCounter < 3): #If User selects top, AND TopCounter isn't 3 (Top row isn't full)
            TopCounter = TopCounter + 1; #Increases TopCounter by 1
            print("Would you like to choose space 0, 1, or 2?")

            try: #Checks to see if user input is valid
                SpaceChoicePlayer1 = int(input())
            except:
                print("You chose an invalid choice, so you've selected 1 by default")
                SpaceChoicePlayer1 = 0;

            if SpaceChoicePlayer1 == 0 and gameboard1[0] not in [int(1), int(2)]:  # If player chooses space 1 in list
                gameboard1[0] = 1
                print("You choose space 0")
                return 1 #Returns so we break out of loop on incorrect input
            elif SpaceChoicePlayer1 == 1 and gameboard1[1] not in [int(1), int(2)]:  # If player chooses space 2 in list
                gameboard1[1] = 1
                print("You choose space 1")
                return 1 #Returns so we break out of loop on incorrect input
            elif SpaceChoicePlayer1 == 2 and gameboard1[2] not in [int(1), int(2)]:  # If player chooses space 3 in list
                gameboard1[2] = 1;
                print("You choose space 2")
                return 1 #Returns so we break out of loop on incorrect input
            else:
                print("Invalid Choice. Space is already taken or does not exist")
                print("Please try again")


        elif (UserInput in ["Mid", "mid", "MID"] and MidCounter < 3):  #If User selects Mid, AND MidCounter isn't 3 (Mid row isn't full)
            MidCounter = MidCounter + 1
            print("Would you like to choose space 0, 1, or 2?")
            try:  # Checks to see if user input is valid
                SpaceChoicePlayer1 = int(input())
            except:
                print("You chose an invalid choice, so you've selected 1 by default")
                SpaceChoicePlayer1 = 0;
            if SpaceChoicePlayer1 == 0 and gameboard2[0] not in [int(1), int(2)]:
                gameboard2[0] = 1
                print("You choose space 0")
                return 1 #Returns so we break out of loop on incorrect input
            elif SpaceChoicePlayer1 == 1 and gameboard2[1] not in [int(1), int(2)]:
                gameboard2[1] = 1
                print("You choose space 1")
                return 1 #Returns so we break out of loop on incorrect input
            elif SpaceChoicePlayer1 == 2 and gameboard2[2] not in [int(1), int(2)]:
                gameboard2[2] = 1;
                print("You choose space 2")
                return 1 #Returns so we break out of loop on incorrect input
            else:
                print("Invalid Choice. Space is already taken or does not exist")
                print("Please try again")

        elif (UserInput in ["Bot", "BOT", "bot"] and BotCounter < 3):  #If User selects Bot, AND BotCounter isn't 3 (Bot row isn't full)
            BotCounter = BotCounter + 1
            print("Would you like to choose space 0, 1, or 2?")
            try:  # Checks to see if user input is valid
                SpaceChoicePlayer1 = int(input())
            except:
                print("You chose an invalid choice, so you've selected 1 by default")
                SpaceChoicePlayer1 = 0;
            if SpaceChoicePlayer1 == 0 and gameboard3[0] not in [int(1), int(2)]:
                gameboard3[0] = 1
                print("You choose space 0")
                return 1 #Returns so we break out of loop on incorrect input
            elif SpaceChoicePlayer1 == 1 and gameboard3[1] not in [int(1), int(2)]:
                gameboard3[1] = 1
                print("You choose space 1")
                return 1 #Returns so we break out of loop on incorrect input
            elif SpaceChoicePlayer1 == 2 and gameboard3[2] not in [int(1), int(2)]:
                gameboard3[2] = 1;
                print("You choose space 2")
                return 1 #Returns so we break out of loop on incorrect input
            else:
                print("Invalid Choice. Space is already taken or does not exist")
                print("Please try again")
        elif(UserInput not in ["top", "Top", "TOP"],["Mid", "mid", "MID"],["Bot", "BOT", "bot"]):
            print("Invalid input. Row is either already full or input was incorrect. Try again.")
            return 0
#----------------------------------------------------------------------------------------------
def Player1WinCases():
    #Each case will trigger in the event that player 1 wins

    #   [Vertical Wins]
    if (gameboard1[0] == 1 and gameboard2[0] == 1 and gameboard3[0] == 1):
        print("Player 1 wins!")
        EndGame()
    #   >
    #  [1, 1, 1] Vertical win 1
    #  [1, 2, 1]
    #  [1, 1, 2]

    if (gameboard1[1] == 1 and gameboard2[1] == 1 and gameboard3[1] == 1):
        print("Player 1 wins!")
        EndGame()
    #      >
    # >[1, 1, 1] Vertical win 1
    # >[2, 1, 1]
    # >[1, 1, 2]

    if (gameboard1[2] == 1 and gameboard2[2] == 1 and gameboard3[2] == 1):
        print("Player 1 wins!")
        EndGame()
    #         >
    # >[1, 1, 1] Vertical win 1
    # >[2, 2, 1]
    # >[1, 1, 1]

    #   [Horizontal Wins]
    if (gameboard1[0] == 1 and gameboard1[1] == 1 and gameboard1[2] == 1):
        print("Player 1 wins!")
        EndGame()

    # >[1, 1, 1] Horizontal win 1
    #  [2, 2, 1]
    #  [1, 1, 2]

    if (gameboard2[0] == 1 and gameboard2[1] == 1 and gameboard2[2] == 1):
        print("Player 1 wins!")
        EndGame()
    #  [2, 2, 1]
    # >[1, 1, 1] Horizontal win 2
    #  [1, 1, 2]

    if (gameboard3[0] == 1 and gameboard3[1] == 1 and gameboard3[2] == 1):
        print("Player 1 wins!")
        EndGame()
    #  [1, 2, 1]
    #  [2, 2, 1]
    # >[1, 1, 1] Horizontal win 3

#   [Diagonal Wins]
    if (gameboard1[0] == 1 and gameboard2[1] == 1 and gameboard3[2] == 1):
        print("Player 1 wins!")
        EndGame()
    # [>1, 2, 1] Horizontal win 1
    #  [2, >1, 1]
    #  [1, 1, >1]

    if (gameboard1[2] == 1 and gameboard2[1] == 1 and gameboard3[0] == 1):
        print("Player 1 wins!")
        EndGame()
    #  [2, 2, >1]
    #  [1, >1, 2] Horizontal win 2
    #  [>1, 1, 2]

#----------------------------------------------------------------------------------------------
def Player2Method (): #Method for player 2's turn
    print("Player 2 you're up! Where would you like to go on the board?")
    print("Enter top to choose a space on the top row")
    print("Enter mid to choose a space on the middle row")
    print("Enter bot to choose a space on the bottom row")
    UserInput = input()
    Player2Choice = False;  # While player1 hasn't chosen a valid choice
    global TopCounter
    global MidCounter
    global BotCounter
    while (Player2Choice == False):
        if (UserInput in ["top", "Top", "TOP"] and TopCounter < 3):  # If player1 enters top, use the top game board
            TopCounter = TopCounter + 1
            print("Would you like to choose space 0, 1, or 2?")

            try: #Checks to see if user input is valid
                SpaceChoicePlayer2 = int(input())
            except:
                print("You chose an invalid choice, so you've selected 1 by default")
                SpaceChoicePlayer2 = 0;

            if SpaceChoicePlayer2 == 0 and gameboard1[0] not in [int(1), int(2)]:  # If player chooses space 1 in list
                gameboard1[0] = 2
                print("You choose space 0")
                return 1 #Returns so we break out of loop on incorrect input
            elif SpaceChoicePlayer2 == 1 and gameboard1[1] not in [int(1), int(2)]:  # If player chooses space 2 in list
                gameboard1[1] = 2
                print("You choose space 1")
                return 1 #Returns so we break out of loop on incorrect input
            elif SpaceChoicePlayer2 == 2 and gameboard1[2] not in [int(1), int(2)]:  # If player chooses space 3 in list
                gameboard1[2] = 2
                print("You choose space 2")
                return 1 #Returns so we break out of loop on incorrect input
            else:
                print("Invalid Choice. Space is already taken or does not exist")
                print("Please try again")

        elif (UserInput in ["Mid", "mid", "MID"] and MidCounter < 3):  # If player1 enters mid , use gameboard2
            MidCounter = MidCounter + 1
            print("Would you like to choose space 0, 1, or 2?")
            try:  # Checks to see if user input is valid
                SpaceChoicePlayer2 = int(input())
            except:
                print("You chose an invalid choice, so you've selected 1 by default")
                SpaceChoicePlayer2 = 0;
            if SpaceChoicePlayer2 == 0 and gameboard2[0] not in [int(1), int(2)]:
                gameboard2[0] = 2
                print("You choose space 0")
                return 1 #Returns so we break out of loop on incorrect input
            elif SpaceChoicePlayer2 == 1 and gameboard2[1] not in [int(1), int(2)]:
                gameboard2[1] = 2
                print("You choose space 1")
                return 1 #Returns so we break out of loop on incorrect input
            elif SpaceChoicePlayer2 == 2 and gameboard2[2] not in [int(1), int(2)]:
                gameboard2[2] = 2;
                print("You choose space 2")
                return 1 #Returns so we break out of loop on incorrect input
            else:
                print("Invalid Choice. Space is already taken or does not exist")
                print("Please try again")

        elif (UserInput in ["Bot", "BOT", "bot"] and BotCounter < 3):  # If player1 enters bot , use gameboard3
            BotCounter = BotCounter + 1
            print("Would you like to choose space 0, 1, or 2?")
            try:  # Checks to see if user input is valid
                SpaceChoicePlayer2 = int(input())
            except:
                print("You chose an invalid choice, so you've selected 1 by default")
                SpaceChoicePlayer2 = 0;
            if SpaceChoicePlayer2 == 0 and gameboard3[0] not in [int(1), int(2)]:
                gameboard3[0] = 2
                print("You choose space 0")
                return 1 #Returns so we break out of loop on incorrect input
            elif SpaceChoicePlayer2 == 1 and gameboard3[1] not in [int(1), int(2)]:
                gameboard3[1] = 2
                print("You choose space 1")
                return 1 #Returns so we break out of loop on incorrect input
            elif SpaceChoicePlayer2 == 2 and gameboard3[2] not in [int(1), int(2)]:
                gameboard3[2] = 2;
                print("You choose space 2")
                return 1 #Returns so we break out of loop on incorrect input
            else:
                print("Invalid Choice. Space is already taken or does not exist")
                print("Please try again")
        elif(UserInput not in ["top", "Top", "TOP"],["Mid", "mid", "MID"],["Bot", "BOT", "bot"]):
            print("Invalid input or Row is already full")
            return 0
#----------------------------------------------------------------------------------------------
def Player2WinCases():
    #Each case will trigger in the event that player 1 wins

    #   [Vertical Wins]
    if (gameboard1[0] == 2 and gameboard2[0] == 2 and gameboard3[0] == 2):
        print("Player 2 wins!")
        EndGame()
    #   >
    #  [2, 1, 1] Vertical win 1
    #  [2, 2, 1]
    #  [2, 1, 2]

    if (gameboard1[1] == 2 and gameboard2[1] == 2 and gameboard3[1] == 2):
        print("Player 2 wins!")
        EndGame()
    #      >
    # >[1, 2, 1] Vertical win 2
    # >[2, 2, 1]
    # >[1, 2, 2]

    if (gameboard1[2] == 2 and gameboard2[2] == 2 and gameboard3[2] == 2):
        print("Player 2 wins!")
        EndGame()
    #         >
    # >[1, 1, 2] Vertical win 3
    # >[2, 1, 2]
    # >[1, 2, 2]

    #   [Horizontal Wins]
    if (gameboard1[0] == 2 and gameboard1[1] == 2 and gameboard1[2] == 2):
        print("Player 2 wins!")
        EndGame()

    # >[2, 2, 2] Horizontal win 1
    #  [2, 2, 1]
    #  [1, 1, 2]

    if (gameboard2[0] == 2 and gameboard2[1] == 2 and gameboard2[2] == 2):
        print("Player 2 wins!")
        EndGame()
    #  [2, 2, 1]
    # >[2, 2, 2] Horizontal win 2
    #  [1, 1, 2]

    if (gameboard3[0] == 2 and gameboard3[1] == 2 and gameboard3[2] == 2):
        print("Player 2 wins!")
        EndGame()
    #  [1, 2, 1]
    #  [2, 1, 1]
    # >[2, 2, 2] Horizontal win 3

#   [Diagonal Wins]
    if (gameboard1[0] == 2 and gameboard2[1] == 2 and gameboard3[2] == 2):
        print("Player 2 wins!")
        EndGame()
    # [>2, 2, 1] Horizontal win 1
    #  [2, >2, 1]
    #  [1, 1, >2]

    if (gameboard1[2] == 2 and gameboard2[1] == 2 and gameboard3[0] == 2):
        print("Player 2 wins!")
        EndGame()
    #  [2, 1, >2]
    #  [1, >2, 2] Horizontal win 2
    #  [>2, 1, 2]

#----------------------------------------------------------------------------------------------
def EndGame(): #Ends program upon encountering a win case. Prints the final game board and exists
    print("     0  1  2")
    print("Top", gameboard1)
    print("Mid", gameboard2)
    print("Bot", gameboard3)
    print("Thanks for playing!")
    sys.exit("GoodBye!")
#----------------------------------------------------------------------------------------------

print("Welcome to Tic Tac Toe!")
print("The rules are simple. Player1 controls 1, and Player 2 controls 2")
print("First one to get three in a row wins!")

TopCounter = 0; #Keeps track of how many space are left in Top row
MidCounter = 0; #Keeps track of how many space are left in Middle row
BotCounter = 0; #Keeps track of how many space are left in Bottom row
Turns = int(0); #Tracks how many turns have passed. Once it equals 9, the game ends in a tie.
GameEnd = False; #Control Var for main loop
MaxRecur = int(1000);
GameInSession = False; #Control var for game in session
#--------------------------------------------------------------------------------------------------------------------------------------
while(GameEnd == False):

    #Creates base game board
    gameboard1 = [int(0), int(0), int(0)]  # Our game board
    gameboard2 = [int(0), int(0), int(0)]  # Our game board
    gameboard3 = [int(0), int(0), int(0)]  # Our game board

    while(GameInSession == False): #Controls current game session

        if (Turns == 9): #If Turns isn't 9 (If the game hasn't tied yet) then ignore and continue
            print("Looks like its a tie!")
            EndGame()

        # prints game board for player 1
        print("     0  1  2")
        print("Top",gameboard1)
        print("Mid",gameboard2)
        print("Bot",gameboard3)

        ReturnedVal = 0
        while(ReturnedVal == 0): #Will continue to loop until input from player 1 is valid
            ReturnedVal = Player1Method()

            # Checks through each case to see if player1 has won before going to player 2's turn
            # ------------------------------------------------------------------------------------------
            Player1WinCases()
            # ------------------------------------------------------------------------------------------

        Turns = Turns + 1; #Increase turn after player1 has gone

        if (Turns == 9): #If Turns isn't 9 (If the game hasn't tied yet) then ignore and continue
            print("Looks like its a tie!")
            EndGame()

        #Reprints game board for player 2
        print("     0  1  2")
        print("Top", gameboard1)
        print("Mid", gameboard2)
        print("Bot", gameboard3)

        ReturnedVal2 = 0
        while (ReturnedVal2 == 0):  # Will continue to loop until input from player 2 is valid
            ReturnedVal2 = Player2Method()

        # Checks through each case to see if player2 has won before going to player 1's turn
        # ------------------------------------------------------------------------------------------
        Player2WinCases()
        # ------------------------------------------------------------------------------------------
        Turns = Turns + 1;#Increase Turn after player2 has gone


