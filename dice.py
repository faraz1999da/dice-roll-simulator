import random


dice_arts = { 1 :(
    '-----------',
    '|         |',
    '|    0    |',
    '|         |',
    '-----------',
),
2 :(
     '-----------' ,
     '| 0       |' ,
     '|         |' ,
     '|       0 |' ,
     '-----------' ,
),
3 :(
    '-----------',
    '| 0       |',
    '|    0    |',
    '|       0 |',
    '-----------',
),
4 :(
    '-----------',
    '| 0     0 |',
    '|         |',
    '| 0     0 |',
    '-----------',
),
5 :(
    '-----------',
    '| 0     0 |',
    '|    0    |',
    '| 0     0 |',
    '-----------',
),
6 :(
    '-----------',
    '| 0     0 |',
    '| 0     0 |',
    '| 0     0 |',
    '-----------',
)

}

DIE_HEIGHT = len(dice_arts[1])
DIE_WIDTH = len(dice_arts[1][0])
DIE_FACE_SEPARATOR = "   "



is_game_over = False



def roll_dice():
    return random.randint(1, 6)

def show_dices(number_of_dices):
    
    die_faces_rows = []

    for i in range(number_of_dices):
        random_key = roll_dice()
        random_dice = dice_arts[random_key]
        user_dices.append(random_dice)

    
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in user_dices:
            row_components.append(die[row_idx])
        # print(row_components)
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        die_faces_rows.append(row_string)

    width = len(die_faces_rows[0])
    results_bar = " Results ".center(width, '=')
    
    print(results_bar)


    
    for row in die_faces_rows:
        print(row)
         


while not is_game_over:
    user_dices = []
    print('How many dices do you want to roll? [ 1-6 ]')
    dice_count = int(input('>> '))
    show_dices(dice_count)
    # print(user_dices)

    print('------------------------------------------------ Result ------------------------------------------------')


    

    print('Do you want to roll again? (yes/no)')
    play_again = input('>> ').lower()

    if play_again == 'no':
        is_game_over = True
        print('Goodbye 😊👋')
        
    
