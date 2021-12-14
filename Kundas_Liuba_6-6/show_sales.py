from sys import argv

with open("bakery.csv", "r", encoding="utf-8") as prices:
    if 1 < len(argv) < 4:
        if len(argv) == 3:
            prices.seek(8 * (int(argv[1]) - 1))
            for i in range(int(argv[2]) - int(argv[1])):
                print(prices.readline(8), end="")
        else:
            prices.seek(8 * (int(argv[1]) - 1))
            print(prices.read().strip())
    else:
        print(prices.read())
