cub_odd = []
idx = 1
while idx <= 1000:# счетчик
    if idx % 2 == 1:
        cub_odd.append(idx**3)
    idx += 1

seven_num = 0
for num, item in enumerate(cub_odd):
    num_total = 0
    while item > 0:
        num_total += item % 10
        item //= 10
    if num_total % 7 == 0:
        seven_num += cub_odd[num]
seven_num2 = 0
for num, item in enumerate(cub_odd):
    item += 17
    num_total = 0
    while item > 0:
        num_total += item % 10
        item //= 10
    if num_total % 7 == 0:
        seven_num2 += cub_odd[num]

print(seven_num, seven_num2)
