'''
http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
 --- --- ---
|   |   |   |
 --- --- ---

#Notes to self
1. Take a user input of game board dimensions
2. Use a function to draw out the game board - function part WIP
'''

#Ask user for input
gameboard_height_user_input = input("Now enter the desired height: ")
gameboard_length_user_input = input("Enter the desired length of game board: ")

type(gameboard_height_user_input)
type(gameboard_length_user_input)
#Convert user input into integers
game_board_height = int(gameboard_height_user_input)
game_board_length = int(gameboard_length_user_input)
#Put the dashes used into variables
horizontal_dashes = "---"
vertical_dashes = "|"

for game_board_height_plus_one in range(game_board_height + 1):
    for height in range(game_board_height):
        if height == 0:
            print(" %s" % horizontal_dashes, end=" ")
        elif height == game_board_height - 1:
            print(horizontal_dashes)
        else:
            print(horizontal_dashes, end=" ")
    if game_board_height_plus_one == game_board_height:
        print("") #do nothing
    else:
        for length in range(game_board_length + 1):
            if length == game_board_length:
                print("%s  " % vertical_dashes)
            else:
                print("%s  " % vertical_dashes, end=" ")

