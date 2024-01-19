import players_setting
import word_for_game
import work_with_word


def main():
    # Лист, хранящий игровые правила для вывода их польхователю.
    game_rules = [
        "Чередование Ходов. Игроĸи по очереди предлагают буĸву",
        "Очĸи за Угадывание. Каждая правильно угаданная буĸва \n"
        "приносит игроĸу очĸи. Например, 100 очĸов за буĸву.",
        "Штраф за Ошибĸу. Если игроĸ предлагает буĸву, \n"
        "ĸоторой нет в слове, следующий ход переходит ĸ другому игроĸу.\n"
        "Можно таĸже ввести штрафные очĸи за неверный ответ.",
        "Угадывание Слова. В любой момент хода игроĸ может \n"
        "попытаться угадать всё слово. Если он угадывает, получает\n"
        "дополнительные очĸи, если ошибается - штраф.",
        "Победа. Игра заĸанчивается, ĸогда слово угадано. \n"
        "Побеждает игроĸ с наибольшим ĸоличеством очĸов.",
    ]

    print("Добро пожаловать на поле чудес! "
          "Сейчас я объясню вам несколько правил. "
          "Готовы? Тогда приступаем!"
          "\n")

    for game_rule in game_rules:
        print(f" * {game_rule}\n")

    players = players_setting.init_some_players()
    choose_difficult = input("Выберите сложность игры:"
                      "\n\t * Легкий режим игры (1)"
                      "\n\t * Средний режим игры (2)"
                      "\n\t * Сложный режим игры (3)\n")

    difficult = ''
    match choose_difficult:
        case '1':
            difficult = 'easy_words'
        case '2':
            difficult = 'normal_words'
        case '3':
            difficult = 'hard_words'
        case _:
            print("Данные введены не верно, ставлю режим игры на средний!")
            difficult = 'normal_words'

    # Слово, которое мы отгадываем.
    word = word_for_game.get_word(difficult)
    players_lives = players_setting.set_difficulty(difficult)

    for player in players:
        player['lives'] = players_lives

    # Итератор для переключения игроков.
    i = 0
    # Переменная, служащая для выключения цыкла при завершении игры.
    # Если True - игра идет, иначе завершаем.
    game = True

    # Тут будут хранится отгаданные символы нашего слова.
    guessed_word = '*' * len(word)

    while game:
        print("Для выхода введите 'q'\n")
        print(guessed_word)
        i = i % len(players)
        player = players[i]
        print(f"Сейчас очередь игрока {player['name']} отгадывать!\n")

        players_insert = \
            input("Введите предпологаемую букву или же все слово: ")
        print(f"Было введено: {players_insert}")

        if players_insert == 'q':
            break
        elif len(players_insert) == 1:
            find_letter = work_with_word.insert_letter(word, players_insert)
            if find_letter >= 0:
                # Меняем соответствующую звездочку на найденный символ
                guessed_word = \
                    guessed_word[:find_letter]\
                    + players_insert\
                    + guessed_word[find_letter + 1:]
                player['points'] += 5
            else:
                print('Нет такой буквы! Крутите... а, ну да...\n')
                player['lives'] -= 1
                i += 1
        else:
            find_word = work_with_word.is_insert_word(word, players_insert)
            if find_word:
                player['points'] += 25
                guessed_word = word
            else:
                player['lives'] -= 1
                i += 1

        if guessed_word.count('*') < 1 or player["lives"] == 0:
            if players[1]['points'] > players[0]["points"]:
                winner = players[1]
            else:
                winner = players[0]

            print(f"\nИгрок {winner['name']} выграл"
                  f" со счетом {winner['points']}\n")

            game = False


if __name__ == "__main__":
    main()