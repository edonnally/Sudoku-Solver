#!/usr/bin/env python
# coding: utf-8

# our initial board
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]   
]

def solve(board): # lets us know whether we found the solution or not
    find = find_empty(board)
    if not find:
        return True
    else: 
        row, col = find
    
    for i in range(1,10):
        if valid(board,i,(row,col)):# if valid, we will plug in this number
            board[row][col] = i
            
            if solve(board):
                return True
            board[row][col] = 0
    
    return False

#checking to see if the board is valid or not
def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i]== num and pos[1] != i: #checks through each row to see if it equals the number we just added in
            return False
    # Check columns
    for i in range(len(board[0])):
        if board[i][pos[1]]== num and pos[0] != i: #checks through each column to make sure it's not the position we just added in
            return False
        
    # Checks what box from the sudoku board we are in
    box_x = pos[1] // 3
    box_y = pos[0] // 3 
    
    for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 + 3): 
            if board[i][j] ==num and (i,j) != pos:
                return False
    
    return True



# the below is to allow us to visualize what the board will look like in a sudoku format 
# as opposed to the matrix format above
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print ("- - - - - - - - - - - -")
        # for every 3rd row we will print a horizontal line to match a sudoku layout  
        for j in range(len(board[0])): #length of our row
            if j % 3 == 0 and j != 0: # checks for the 3rd element in each column
                print(" | ", end = "") # adding in the end keeps it from adding in a backslash and going to the next line
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")



#print_board(board)

#finding empty spaces
def find_empty(board):
    for i in range(len(board)): # finding an empty position to then return the empty position
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, column
    
    return None



print_board(board)
solve(board)
print("                     ")
print("                     ")
print_board(board)





