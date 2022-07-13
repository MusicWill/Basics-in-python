

'''
str = "heLLO"
stri = ""
n = 4

for i in range(0, len(str)):
    str.isupper()
    if str[i].islower():
        stri += (str[i] * n)
print(stri)

'''

'''
Given a String str
Scrambled
str = “lelho”
Given an Array of indices
[2,1,3,0,4]
L  E L H O
0 1 2 3 4
 hello

0 1 2 3 4
F L I E S

2 1 3 0 4
I L E F S
'''

'''
str = "ilefs"
arr = [2, 1, 3, 0, 4]
result = ""
correct_placement = [''] * len(str) # ['', '', '', '', '']


for i in range(0, len(str)):
    index_to_be_placed = arr[i] # first loop i = 0
    # first loop -> arr[i] = arr[0] = 2 = index_to_be_placed
    # second loop: index_to_be_placed = 1
    correct_placement[arr[i]] = str[i]


for i in range(0, len(str)):
    # [ "h", "e", "l", "l", "o']
    #    0    1    2    3    4
    # get "h" add to result
    # get "e" add to result
    # get "h"
    result += correct_placement[i]
    print(result)
'''

'''
[]-allows you to get something out of strings, array/lists. 
()-are usually method calls, to call methods like len or range.
{}-for dictionaries
'''

'''
str = "hello"
#print(str[2])

for i in range(0, len(str)):
    print(str[i])
'''

'''
str = [ "hello", "willis", "this", "is", "a", "test", "maybe"]

for i in range(0, len(str)):
    if len(str[i]) < 2:
        print("no second letter :(")
    else:
        print(str[i][1])
'''

#str = [[1, 2, 3, 4, 5], ["hhhhhhhhhhhhhhhhhhhh"], ["hhhhhhhhhhhhhhhhhhhhhajlsfhaldskjfhs;fahs;f"]]

#print(len(str))

'''

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(0, len(list)):
#    print("this is i" + str(i))
#    print(list[i][i])
    for j in range(0, len(list[i])):
        print(list[i][j])

'''


#Tic Tac Toe game


tic_tac_toe_board = [   ["", "", ""],
                        ["", "", ""],
                        ["", "", ""]
                    ]
for i in range(0,9):
    user_requested_row = int
    position = input("Enter your position: ")
    position_input_is_valid = True
    if int(position[0]) > 2 or int(position[0]) < 0:
        print("invalid row input")
        position_input_is_valid = False
        #re-ask user for correct input so they still have a turn
    if int(position[1]) > 2 or int(position[1]) < 0:
        print("invalid col input")
        position_input_is_valid = False
    while position_input_is_valid == False:
        position = input("Enter your position: ")
        if int(position[0]) <= 2 and int(position[0]) >= 0 and int(position[1]) <= 2 and int(position[1]) >= 0:
            position_input_is_valid = True
    Player1 = "0"
    Player2 = "X"
    if i % 2 == 0:
        tic_tac_toe_board[int(position[0])][int(position[1])] = Player1

    else:
        tic_tac_toe_board[int(position[0])][int(position[1])] = Player2
    for j in range(0,3):
        print(tic_tac_toe_board[j])




