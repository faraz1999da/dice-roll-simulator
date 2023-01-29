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

is_game_over = False

user_dices = []

def roll_dice():
    return random.randint(1, 6)

def show_dices(number_of_dices):

    for i in range(number_of_dices):
        random_key = roll_dice()
        random_dice = dice_arts[random_key]
        user_dices.append(random_dice)



while not is_game_over:
    print('How many dices do you want to roll? [ 1-6 ]')
    user_input = int(input('>> '))
    show_dices(user_input)
    for dice in user_dices:
        for i in dice:
            print(i)
    break
