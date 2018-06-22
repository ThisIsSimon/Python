'''
http://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
 --- --- ---
|   |   |   |
 --- --- ---
#Notes to self
1. Take a user input of game board dimensions
2. Use a function to draw out the game board
'''
def draw_horizontal(length):
    horizontal_dashes = " ---"
    print(horizontal_dashes * length)

def draw_vertical(length):
    vertical_dashes = "|   "
    print(vertical_dashes * (length + 1))

def draw_game_board(length, height):
    for h in range(height):
        draw_horizontal(length)
        draw_vertical(length)
    draw_horizontal(length)


#Ask user for input
game_board_length = int(input("Enter the desired length of game board: "))
game_board_height = int(input("Now enter the desired height: "))

#Calls function to draw the game board
draw_game_board(game_board_length, game_board_height)
