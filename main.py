from random import choice

HANGMAN = (
    """
     ------
     | |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     | |
     | O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     | |
     | O
     | |
     |
     |
     |
    ----------
    """,
    """
     ------
     | |
     | O
     | /|
     |
     |
     |
    ----------
    """,
    """
     ------
     | |
     |  O
     | /|\\
     |
     |
     |
    ----------
    """,
    """
     ------
     | |
     | O
     | /|\\
     | /
     |
     |
    ----------
    """,
    """
     ------
     | |
     | O
     | /|\\
     | / \\
     |
     |
    ----------
    """
)

max_wrong = 2
WORDS = ('питон', 'игра', 'программирование', 'колесо', "танк", "мишь")
word = choice(WORDS)
so_far = '_' * len(word)
wrong = 0
used = []

while wrong < max_wrong and so_far != word:
    print(HANGMAN[wrong])
    print('\nВы использовали следующие буквы:\n', used)
    print('\nНа данный момент слово выглядит так:\n', so_far)

    guess = input('\n У Вас есть 2 попытки чтобы ответить не правильно. Введите свой вариант слова: ')

    while guess in used:
        print('Вы уже угадали букву', guess)
        guess = input('Введите своё предположение: ')

    used.append(guess)

    if guess in word:
        print('\nДа! \'' + guess + '\' эта буква есть в слове!')

        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print('\nИзвините, данной буквы \'' + guess + '\' нет в слове.')
        wrong += 1

if wrong == max_wrong:
    print(HANGMAN[wrong])
    print('\nТебя повесили! Было использованно 2 попыток')
else:
    print('\nПоздравляем Вы угадали слово!')

print('\nЗагаданное слово было \'' + word + '\'')