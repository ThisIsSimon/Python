'''
http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
 --- --- ---
|   |   |   |
 --- --- ---

#Notes to self
1. Take a user input of game board dimensions
2. Use a function to draw out the game board
'''

def draw_game_board(game_board_height, game_board_length):
    #This function takes two parameters, a height and length
    #It then proceeds to loop through specific conditions to draw the game board horizontally
    #Put the dashes used into variables
    horizontal_dashes = "---"
    vertical_dashes = "|"
    for game_board_height_plus_one in range(game_board_height + 1):
        for height in range(game_board_height):
            if height == 0: #if drawing the first line, then add a space to the left to accommodate
                print(" %s" % horizontal_dashes, end=" ")
            elif height == game_board_height - 1: #if printing the last dash on the row, print it and then drop off to the next line (default)
                print(horizontal_dashes)
            else: #otherwise just print the lines normally horizontally (using end=" ")
                print(horizontal_dashes, end=" ")
        if game_board_height_plus_one == game_board_height: #if the height is equal to the last row, don't print the extra row of pipes |
            print("")
        else:
            for length in range(game_board_length + 1):
                if length == game_board_length: #if printing the last pipe on the row, drop off to the next line
                    print("%s  " % vertical_dashes)
                else:
                    print("%s  " % vertical_dashes, end=" ") #otherwise print horizontally using end=" "


#Ask user for input
gameboard_height_user_input = input("Now enter the desired height: ")
gameboard_length_user_input = input("Enter the desired length of game board: ")

type(gameboard_height_user_input)
type(gameboard_length_user_input)

#Convert user input into integers
game_board_height = int(gameboard_height_user_input)
game_board_length = int(gameboard_length_user_input)

#Calls function to draw the game board
draw_game_board(game_board_height, game_board_length)
