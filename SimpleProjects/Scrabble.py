def parser(w):
    res_of_parsing = list(w)
    return res_of_parsing


def scrabble(w):
    score = int()
    parsed_word = parser(w)
    for i in range(len(parsed_word)):
        if parsed_word[i] == 'a':
            score += 1
        elif parsed_word[i] == 'e':
            score += 1
        elif parsed_word[i] == 'i':
            score += 1
        elif parsed_word[i] == 'o':
            score += 1
        elif parsed_word[i] == 'u':
            score += 1
        elif parsed_word[i] == 'l':
            score += 1
        elif parsed_word[i] == 'n':
            score += 1
        elif parsed_word[i] == 's':
            score += 1
        elif parsed_word[i] == 't':
            score += 1
        elif parsed_word[i] == 'r':
            score += 1
        elif parsed_word[i] == 'd':
            score += 2
        elif parsed_word[i] == 'g':
            score += 2
        elif parsed_word[i] == 'b':
            score += 3
        elif parsed_word[i] == 'c':
            score += 3
        elif parsed_word[i] == 'm':
            score += 3
        elif parsed_word[i] == 'p':
            score += 3
        elif parsed_word[i] == 'f':
            score += 4
        elif parsed_word[i] == 'h':
            score += 4
        elif parsed_word[i] == 'v':
            score += 4
        elif parsed_word[i] == 'w':
            score += 4
        elif parsed_word[i] == 'y':
            score += 4
        elif parsed_word[i] == 'k':
            score += 5
        elif parsed_word[i] == 'j':
            score += 8
        elif parsed_word[i] == 'x':
            score += 8
        elif parsed_word[i] == 'q':
            score += 10
        elif parsed_word[i] == 'z':
            score += 10
    return score


while True:
    word = input('Enter word or /quit for exit: ')
    if word == '/quit':
        break
    else:
        print(scrabble(word))
