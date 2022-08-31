import random

word_list = []
with open("./word_list.txt", "r") as file:
    word_list = list(map(str, file.read().split()))


def get_word():
    return random.choice(word_list)
