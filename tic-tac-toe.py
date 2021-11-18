grid = [[' ', ' ', ' '],[' ',' ',' '],[' ',' ',' ']]
step = 'X'
stopped = False
amount_of_steps = 0
game_finished = False
x_wins = False
o_wins = False

def print_grid():
    global grid
    print()
    print('| ', grid[0][0],' ', grid[0][1], ' ', grid[0][2], ' |')
    print('| ', grid[1][0],' ', grid[1][1], ' ', grid[1][2], ' |')
    print('| ', grid[2][0],' ', grid[2][1], ' ', grid[2][2], ' |')
    print()
    pass

def fill_grid():
    global grid
    correct_enter = False
    while correct_enter == False:
        coordinates = input("Enter the coordinates:").split()
        if coordinates[0].isdigit() and coordinates[1].isdigit():
            if int(coordinates[0]) <= 3 and int(coordinates[0]) >= 1 and int(coordinates[1]) <= 3 and int(coordinates[1]) >= 1:
                if grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] == ' ':
                    correct_enter = True
                else:
                    print("This is place is already filled!")
            else:
                print("The coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")
    grid[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = step
    pass

def check_if_finished():
    global game_finished
    global x_wins
    global o_wins
    global grid
    global step
    #FOR ROWS:
    for row in [0, 1, 2]:
        if grid[row][0] == grid[row][1] == grid[row][2] == step:
            if step == 'X':
                x_wins = True
            else:
                o_wins = True
            game_finished = True
    #FOR COLMS:
    for col in [0, 1, 2]:
        if grid[0][col] == grid[1][col] == grid[2][col] == step:
            if step == 'X':
                x_wins = True
            else:
                o_wins = True
            game_finished = True
    #FOR HORIZONTAL:
    if grid[0][0] == grid[1][1] == grid[2][2] == step:
        if step == 'X':
             x_wins = True
        else:
            o_wins = True
        game_finished = True
    elif grid[0][2] == grid[1][1] == grid[2][0] == step:
        if step == 'X':
             x_wins = True
        else:
            o_wins = True
        game_finished = True
    if amount_of_steps == 9:
        game_finished = True
    pass

while not stopped:
    while game_finished == False:
        print_grid()
        fill_grid()
        amount_of_steps += 1
        check_if_finished()
        if step == 'X':
            step = 'O'
        else:
           step = 'X'
    print_grid()
    if o_wins == True:
        print("O wins!")
    elif x_wins == True:
        print("X wins!")
    else:
        print("Draw!")
    command = input('Enter command:')
    if command == 'STOP':
        stopped = True
    grid = [[' ', ' ', ' '],[' ',' ',' '],[' ',' ',' ']]
    game_finished = False
    amount_of_steps = 0

