"""
Необходимо вывести те его элементы, значения которых больше предыдущего
"""
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

final_result = [src[num] for num in range(1, len(src)) if src[num] > src[num - 1]]
print(*final_result)
