import random

items = {1: 'rock', 2: 'paper', 3: 'scissors'}


# 0 - rock, 1 - paper, 2 - scissors

def rock_paper_scissors(p_ch, i):
    result = ''
    print(i)
    r = random.randint(1, 3)
    if (p_ch == 'rock' and i[r] == 'scissors') or (p_ch == 'scissors' and i[r] == 'paper') or (
            p_ch == 'paper' and i[r] == 'rock'):
        result = 'You win!'
    elif (p_ch == 'scissors' and i[r] == 'rock') or (p_ch == 'paper' and i[r] == 'scissors') or (
            p_ch == 'rock' and i[r] == 'paper'):
        result = 'You lose!'
    elif p_ch == i[r]:
        result = 'Draw!'
    else:
        result = 'Error!'
    return result, r


while True:
    menu_mode = input('''Rock, Paper or Scissors? \n> ''')
    if menu_mode == '/quit':
        break
    else:
        print(rock_paper_scissors(menu_mode, items))
