import json
import random


# Считываем Json файл
def get_word(mode: str):
    with open("words.json", "r") as json_file:
        words = json.load(json_file)
    return get_rand_word(words[mode])


# Выбираем рандомное слово из списка слов
def get_rand_word(words):
    words = random.choice(words)
    return words.lower()


if __name__ == '__main__':
    get_word('easy_words')
