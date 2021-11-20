cub_odd = []
idx = 1
while idx <= 1000: # счетчик
    if idx % 2 == 1:
        cub_odd.append(idx**3)
    idx += 1

seven_num = 0
for num in cub_odd:
    num_total = 0
    num_copia = num
    while num // 10 > 10:
        remainder = num % 10
        whole = num // 10
        num_total += remainder
        num = whole
    remainder = num % 10
    whole = num // 10
    num_total = num_total + remainder + whole
    if num_total % 7 == 0:
        seven_num += num_copia
print(seven_num)
seven_num2 = 0
for num, item in enumerate (cub_odd):
    item += 17
    num_total = 0
    num_copia = item
    while item // 10 > 10:
        remainder = item % 10
        whole = item // 10
        num_total += remainder
        item = whole
    remainder = item % 10
    whole = item // 10
    num_total = num_total + remainder + whole
    if num_total % 7 == 0:
        seven_num2 += num_copia
print(seven_num2)
