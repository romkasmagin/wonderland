def insert_letter(word, inserted_letter):

    find_letter = word.find(inserted_letter)

    return find_letter


def is_insert_word(word, inserted_word):
    word = word.lower()
    inserted_word = inserted_word.lower()
    if word == inserted_word:
        return True
    else:
        return False
