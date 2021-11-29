from random import choice #обязательно для выполнения функции


def get_jokes(n):
    jokes = ""
    for i in range(n):
        sentence = choice(nouns), choice(adverbs), choice(adjectives)
        joke = " ".join(sentence)
        jokes += joke
        jokes += ", "
    return jokes


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
print(get_jokes(int(input("Введите целое число"))))

