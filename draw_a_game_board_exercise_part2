'''
[[1,2,3],
 [4,5,6],
 [7,8,9]]

[[1,2,3,4],
 [5,6,7,8],
 [9,10,11,12]
 [13,14,15,16]]

 determining a winner in tic tac toe
'''

test_list =  [[1,2,3],
              [0,2,0],
              [2,1,0]]

test_list_length = len(test_list)

left_diagonal = []
def append_left_diagonally():
    #[x, 0, 0]
    #[0, x, 0]
    #[0, 0, x]
    #Takes the upper left to lower right diagonal items (marked x) and puts it in a list
    #Note to self: With this function, I need to learn how to loop the item into a proper matrix into the original list to avoid making a new list and later appending it
    for x in range(test_list_length):
        left_diagonal.extend([test_list[x][x]])

right_diagonal = []
def append_right_diagonally():
    #[0, 0, x]
    #[0, x, 0]
    #[x, 0, 0]
    #Takes the upper right to lower left diagonal items (marked x) and puts it in a list
    #Note to self: With this function, I need to learn how to loop the item into a proper matrix into the original list to avoid making a new list and later appending it
    y = test_list_length - 1
    for x in range(test_list_length):
        right_diagonal.extend([test_list[x][y]])
        y = y - 1

''' Appending up to down (vertically)
0,0  0,1  0,2
1,0  1,1  1,2
2,0  2,1  2,2
'''
def append_horizontally():
    #[x, 0, 0]
    #[x, 0, 0]
    #[x, 0, 0]
    #Take the values from top to bottom and puts it in a list
    #Note to self: With this function, I need to learn how to loop the item into a proper matrix into the original list to avoid making a new list and later appending it

#Append the items to the original list
append_left_diagonally()
test_list.append(left_diagonal)
append_right_diagonally()
test_list.append(right_diagonal)

print(test_list)
'''
for x in range(len(test_list)):
    if(len(set(test_list[x]))) == 1: #check if everything in the list is the same, set() delete all duplicates and then proceed to check if the len() is equal to 1
        if 0 in test_list[x]: #make sure the list does not contain any 0s to prevent [0, 0, 0] from being count as a win - more reading https://stackoverflow.com/questions/43690191/why-are-dict-lookups-always-better-than-list-lookups/43690671#43690671
            continue
        else: #if it doesn't contain any 0s then it is the winning row
            print(test_list[x])
    else: #if the list doesn't contain any duplicates then continue on
        continue
'''
'''
y = len(test_list) - 1
for x in range(len(test_list)):
    #print(x)
    print(test_list[x][y])
    y = y - 1
'''
