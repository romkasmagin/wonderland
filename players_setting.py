DIFFICULT_FOR_EASY_MODE = 15
DIFFICULT_FOR_NORMAL_MODE = 10
DIFFICULT_FOR_HARD_MODE = 7


def create_player():
    """
    Создаем игрока с нулевыми жизнями и очками,
    а так же задаем ему имя.
    """
    name = set_name()
    player = {'name': name, 'lives': 0, 'points': 0}
    return player


def set_name():
    name = input("Введите имя для игрока: ")
    return name


def init_some_players(count_players=2) -> list:
    """
    Создаем двух игроков по умолчанию.
    Записываем из в список и возвращаем его
    """
    players = list()
    for _ in range(count_players):
        players.append(create_player())
    return players[:]


def set_difficulty(difficulty):
    # Устонавливаем количесво жизней в
    # зависимости от сложности игры
    if difficulty == 'easy_words':
        return DIFFICULT_FOR_EASY_MODE

    if difficulty == 'normal_words':
        return DIFFICULT_FOR_NORMAL_MODE

    if difficulty == 'hard_words':
        return DIFFICULT_FOR_HARD_MODE
    else:
        return 10
