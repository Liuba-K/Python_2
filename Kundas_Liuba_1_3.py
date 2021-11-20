''''
склонение слова процент
'''
N = 1
while N <= 100: # счетчик
    if N == 1:
        print(N, "процент")
    elif 1 < N < 5:
        print(N, "процента")
    elif N > 20:
        if (N % 10) == 1:
            print(N, "процент")
        elif 1 < (N%10) < 5:
            print(N, "процента")
        else:
            print(N, "процентов")
    else:
        print(N, "процентов")
    N = N + 1