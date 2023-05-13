# board = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']
# ]

# def display_board():
#     print('TIC TAC TOE')
#     print("*********************")
#     for row in board :
#         print("*     " + row[0] + "   |   " + row[1] + "  |   " + row[2] + "     *")
#         print("*    --- | --- | ---    * ")
#     print("*********************")
    
# for row in board :
#     if row[]
#         col = new_col
#         new_col[1] = 'x'



#Board using dictionaries    


spot = {
    1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7:' ', 8:' ', 9: ' '
} 

def display_board() :
    print('TIC TAC TOE')
    print(f"********************\n*    {spot[1]} | {spot[2]} | {spot[3]}     *\n*   ---|---|---    *\n*    {spot[4]} | {spot[5]} | {spot[6]}     *\n*   ---|---|---    *\n*    {spot[7]} | {spot[8]} | {spot[9]}     *\n********************")
 
print()
print('Welcome to TIC TAC TOE!')
print()   
display_board()
print()

spot[1] = 'x'
display_board()

playing = True