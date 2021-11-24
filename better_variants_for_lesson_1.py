#____________________________Lesson 1-1
duration = int(input("Введите время в секундах"))
timepiece = [duration // 86400, duration // 3600 % 24, duration // 60 % 60, duration % 60]
print(f'duration = {duration} сек\n{timepiece[0]} дн {timepiece[1]} час {timepiece[2]}  мин {timepiece[3]} сек')

#__________________________lesson 1-3
for percent in range(101):
    if percent % 10 == 1 and percent % 100 != 11:
        print(percent, 'процент,', end='')
    elif 1 < percent % 10 < 5 and not 11 < percent % 100 < 15:
        print(percent, 'процента,', end='')
    else:
        print(percent, 'процентов,', end='')

#________________________lesson 1-2
list_of_cubes = []
add_list_of_cubes = []
all_sum = 0
for i in range(1, 1000, 2):
    list_of_cubes.append(i**3)

for ind, val in enumerate(list_of_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits %7 ==0:
        all_sum += list_of_cubes[ind]
print(all_sum)
for m in list_of_cubes:
    add_list_of_cubes.append(m+17)
all_sum = 0
for ind, val in enumerate(list_of_cubes):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        all_sum += list_of_cubes[ind]

print(all_sum)