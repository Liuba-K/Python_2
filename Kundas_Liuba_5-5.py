src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#result = [23, 1, 3, 10, 4, 11]

result_2 = sorted(src)
result_3 = [result_2[i] for i in range(1, len(result_2)) if result_2[i] == result_2[i-1]]
#result = [val for key, val in enumerate(src[1:], start=1) if val != src[key - 1] and if val not in result_3]

result = []
for key, val in enumerate(src[1:], start=1):
    if val != src[key - 1]:
        if val not in result_3:
            result.append(val)
        #if val == result[key - 1]:

print(result)

