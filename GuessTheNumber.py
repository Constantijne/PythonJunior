"""Забавный проект Python для групп или мероприятий, где необходим случайный генератор.
Это полезно для проведения лотерей, настольных игр или просто угадывания случайного числа между игроками."""
import random


def guesser(s, p_num):
    random_num = random.randint(s[0], s[1])
    if p_num == random_num:
        return 'You win!'
    elif p_num != random_num:
        return 'You lose!'
    else:
        return 'Unknown error!'


while True:
    menu_mode = input('Enter mode: ')
    if menu_mode == '/about':
        print(__doc__)
    elif menu_mode == '/help':
        print(
            "/about - О программе\n/help - Вывод справки с командами\n/game - Старт игры\n/quit - Завершание работы "
            "программы")
    elif menu_mode == '/game':
        print(guesser([int(input('Введите нижний диапазон генерации: \n> ')),
                       int(input('Введите верхний диапазон генерации: \n> '))],
                      int(input(' Введите Ваше число: \n> '))))
    elif menu_mode == '/quit':
        break
    else:
        print('Wrong command! Use correct command!')
