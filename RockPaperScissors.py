import random


# 0 - rock, 1 - paper, 2 - scissors

def rock_paper_scissors(p_ch):
    result = ''
    r = random.randint(0, 2)
    if (p_ch < r) > -1:
        result = 'You win!'
    elif (p_ch > r) < 3:
        result = 'You lose!'
    elif 3 < (p_ch == r) < -1:
        result = 'Draw!'
    else:
        result = 'Check your input!'
    return result


print(rock_paper_scissors(int(input('''Rock, Paper or Scissors? 
> '''))))
