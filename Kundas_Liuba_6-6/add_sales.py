from sys import argv

with open("bakery.csv", "a", encoding="utf-8") as prices_a:
    print(argv[1], file=prices_a)
