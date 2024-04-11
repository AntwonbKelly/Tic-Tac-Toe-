import os

#Display all of the rows.
def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

#Map
Row1 = ["_","_","_"];
Row2 = ["_","_","_"];
Row3 = ["_","_","_"];
Blank = "_";

#Winning cases
def Logic(row1,row2,row3):

    #Vertical 1
    if(row1[0] != "_" and row1[0] == row2[0] and row2[0] == row3[0]):
        
        if(row1[0] == "X"):
            print("Player 1 is the winner!");

            Tes = input("GameOver");
            quit();
        else:
            print("Player 2 is the winner!");

            Tes = input("GameOver");
            quit();

    #Vertical 2
    if(row1[1] != "_" and row1[1] == row2[1] and row2[1] == row3[1]):
        
        if(row1[1] == "X"):
            print("Player 1 is the winner!");

            Tes = input("GameOver");
            quit();
        else:
            print("Player 2 is the winner!");

            Tes = input("GameOver");
            quit();
    
    #Vertical 3
    if(row1[2] != "_" and row1[2] == row2[2] and row2[2] == row3[2]):
        
        if(row1[0] == "X"):
            print("Player 1 is the winner!");

            Tes = input("GameOver");
            quit();
        
        else:
            print("Player 2 is the winner!");

            Tes = input("GameOver");
            quit();
    
    #Horizontal 1
    if(row1[0] != "_" and row1[0] == row1[1] and row1[1] == row1[2]):
        
        if(row1[0] == "X"):
            print("Player 1 is the winner!");

            Tes = input("GameOver");
            quit();
        
        else:
            print("Player 2 is the winner!");

            Tes = input("GameOver");
            quit();
    
    #Horizontal 2
    if(row2[0] != "_" and row2[0] == row2[1] and row2[1] == row2[2]):
        
        if(row2[0] == "X"):
            print("Player 1 is the winner!");

            Tes = input("GameOver");
            quit();
        
        else:
            print("Player 2 is the winner!");

            Tes = input("GameOver");
            quit();
    
    #Horizontal 3
    if(row3[0] != "_" and row3[0] == row3[1] and row3[1] == row3[2]):
        
        if(row3[0] == "X"):
            print("Player 1 is the winner!");

            Tes = input("GameOver");
            quit();
        
        else:
            print("Player 2 is the winner!");

            Tes = input("GameOver");
            quit();
    
    #Diagonal 1
    if(row1[0] != "_" and row1[0] == row2[1] and row2[1] == row3[2]):
        
        if(row1[0] == "X"):
            print("Player 1 is the winner!");

            Tes = input("GameOver");
            quit();
        
        else:
            print("Player 2 is the winner!");

            Tes = input("GameOver");
            quit();
    
    #Diagonal 2
    if(row3[0] != "_" and row3[0] == row2[1] and row2[1] == row1[2]):
        
        if(row3[0] == "X"):
            print("Player 1 is the winner!");

            Tes = input("GameOver");
            quit();
        
        else:
            print("Player 2 is the winner!");

            Tes = input("GameOver");
            quit();
    
    #All Spaces filled
    if("_" not in row1 and "_" not in row2 and "_" not in row3):
        
        print("Well, nobody wins!")
        Tes = input("GameOver");
        quit();
        
    



#Controls entire program
GameEnd = False;

#While the game is not over
while(GameEnd != True):
    
    #Clear screen before Player 1 goes
    os.system('cls')
    
    #Display game board
    display(Row1,Row2,Row3);

    #Check to see if a player won
    Logic(Row1,Row2,Row3);

    #Player 1 goes first
    print("Player 1's turn (X)");
    RowResult = input("Select a Row, Player 1 - [1,2,3]: ");
    IsRowValid = False;



    while(IsRowValid != True):
        #If the user chooses row 1, and there is a free space in row1
        if(RowResult == "1"  and Blank in Row1):

            IsSpaceValid = False;
            while(IsSpaceValid != True):
                print(f"Now select a space you'd like to mark in {RowResult} ")
                SpotResult = input("Select space 0, 1, or 2: ")

                #If spot the user selected isn't blank
                if(SpotResult not in ["0","1","2"]or Row1[int(SpotResult)] != Blank ):
                    #Clear screen before Player 1 goes
                    os.system('cls')
                    
                    #Display game board
                    display(Row1,Row2,Row3);
                    print("Invalid movement.");
                    tes = input("Select anything to continue")
                    continue;

                #If the spot the user select IS valid
                else:
                    Row1[int(SpotResult)] = "X";
                    IsSpaceValid = True;
                    IsRowValid = True;
                    
        
        
        if(RowResult == "2" and Blank in Row2):

            IsSpaceValid = False;
            while(IsSpaceValid != True):
                print(f"Now select a space you'd like to mark in {RowResult} ")
                SpotResult = input("Select space 0, 1, or 2: ")

                #If spot the user selected isn't blank
                if(SpotResult not in ["0","1","2"]or Row2[int(SpotResult)] != Blank ):
                    #Clear screen before Player 1 goes
                    os.system('cls')
                    
                    #Display game board
                    display(Row1,Row2,Row3);
                    print("Invalid movement.");
                    continue;

                #If the spot the user select IS valid
                else:
                    Row2[int(SpotResult)] = "X";
                    IsSpaceValid = True;
                    IsRowValid = True;
        
        if(RowResult == "3" and Blank in Row3):

            IsSpaceValid = False;
            while(IsSpaceValid != True):
                print(f"Now select a space you'd like to mark in {RowResult} ")
                SpotResult = input("Select space 0, 1, or 2: ")

                #If spot the user selected isn't blank

                if(SpotResult not in ["0","1","2"]or Row3[int(SpotResult)] != Blank ):
                    #Clear screen before Player 1 goes
                    os.system('cls')
                    
                    #Display game board
                    display(Row1,Row2,Row3);
                    print("Invalid movement.");
                    continue;

                #If the spot the user select IS valid
                else:
                    Row3[int(SpotResult)] = "X";
                    IsSpaceValid = True;
                    IsRowValid = True;


        elif(IsRowValid == True):
            break;
            
        else:
            print("Row is already full... Select a differen't row")
            tes = input("Select anything to continue")
            continue;   
    
    #Set IsRowValid back to false
    IsRowValid = False;

    #Clear screen
    os.system('cls')

    #Display map
    display(Row1,Row2,Row3);

    #Check to see if a player won
    Logic(Row1,Row2,Row3);

    #Player 2's turn start
    print("Player 2's Turn!");

    RowResult = input("Select a Row, Player 2 - [1,2,3]: ");
    IsRowValid = False;

    while(IsRowValid != True):
        #If the user chooses row 1, and there is a free space in row1
        if(RowResult == "1"  and Blank in Row1):

            IsSpaceValid = False;
            while(IsSpaceValid != True):
                print(f"Now select a space you'd like to mark in {RowResult} ")
                SpotResult = input("Select space 0, 1, or 2: ")

                #If spot the user selected isn't blank
                if(SpotResult not in ["0","1","2"]or Row1[int(SpotResult)] != Blank ):
                    #Clear screen before Player 1 goes
                    os.system('cls')
                    
                    #Display game board
                    display(Row1,Row2,Row3);
                    print("Invalid movement.");
                    tes = input("Select anything to continue")
                    continue;

                #If the spot the user select IS valid
                else:
                    Row1[int(SpotResult)] = "O";
                    IsSpaceValid = True;
                    IsRowValid = True;
                    
        
        
        if(RowResult == "2" and Blank in Row2):

            IsSpaceValid = False;
            while(IsSpaceValid != True):
                print(f"Now select a space you'd like to mark in {RowResult} ")
                SpotResult = input("Select space 0, 1, or 2: ")

                #If spot the user selected isn't blank
                if(SpotResult not in ["0","1","2"]or Row2[int(SpotResult)] != Blank ):
                    #Clear screen before Player 1 goes
                    os.system('cls')
                    
                    #Display game board
                    display(Row1,Row2,Row3);
                    print("Invalid movement.");
                    continue;

                #If the spot the user select IS valid
                else:
                    Row2[int(SpotResult)] = "O";
                    IsSpaceValid = True;
                    IsRowValid = True;
        
        if(RowResult == "3" and Blank in Row3):

            IsSpaceValid = False;
            while(IsSpaceValid != True):
                print(f"Now select a space you'd like to mark in {RowResult} ")
                SpotResult = input("Select space 0, 1, or 2: ")

                #If spot the user selected isn't blank
                
                if(SpotResult not in ["0","1","2"]or Row3[int(SpotResult)] != Blank ):
                    #Clear screen before Player 1 goes
                    os.system('cls')
                    
                    #Display game board
                    display(Row1,Row2,Row3);
                    print("Invalid movement.");
                    continue;

                #If the spot the user select IS valid
                else:
                    Row3[int(SpotResult)] = "O";
                    IsSpaceValid = True;
                    IsRowValid = True;


        elif(IsRowValid == True):
            break;
            
        else:
            print("Row is already full... Select a differen't row")
            tes = input("Select anything to continue")
            continue; 


    






