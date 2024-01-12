game = [["" for x in range(3)] for i in range(3)]

c_p = 2
game_over = False

def make_move():
    row = int(input(f"Player {c_p} select row: "))
    col = int(input(f"Player {c_p} select col: "))
    if game[row][col] == "":
        game[row][col] = "X" if c_p == 1 else "O"

def  check_win():
    global game_over
    #check row
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] and game[i][0] != "":
            return True
        
    # check column
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i] and game[0][i] != "":
            return True
    
    #diagonal 
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != "":
        return  True
    elif game[0][2] == game[1][1] == game[2][0] and game[0][2] != "":
        return True
        
    
while game_over == False:
    c_p = 3 - c_p
    print(game)
    make_move()
    if check_win():
        print(f"{c_p} wins!")
        game_over = True
