# код выполняет различные операции над массиво целых чисел

import math
arr = [20, 4, 200, 115, 240]

# 1 нах макс эл с помощью find
def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num
max_num = find_max(arr)
print("1. Максимальный элемент в массиве:", max_num)


# 2 нах мин массив с помощью цикла
min_val = arr[0]
for i in range(1, len(arr)):
    if arr[i] < min_val:
        min_val = arr[i]
print("2. Минимальный элемент в массиве:", min_val)

# 3 вычисляет лог по основанию 2
# Находим значение lg(x) для каждого элемента массива
log_values = [math.log2(x) for x in arr]

# Находим максимальное значение функции lg(x) в массиве
max_log_value = max(log_values)

# Находим индекс элемента, значение функции lg(x) которого равно максимальному значению
max_log_index = log_values.index(max_log_value)

# Переставляем найденный элемент на первое место в массиве
arr[0], arr[max_log_index] = arr[max_log_index], arr[0]

print("3. Исходный массив:", arr)


# 4  нах макс эл в массиве кот делится на 11
max_num = None
for num in arr:
    if num % 11 == 0:
        if max_num is None or num > max_num:
            max_num = num
if max_num is not None:
    print("4. Максимальное число, нацело делящееся на 11 в массиве:", max_num)
else:
    print("4. Чисел, нацело делящихся на 11, в массиве", arr, "нет.")

# 5 нах макс элемент в масс кот отличаетс от соседних не менее чем на 72
max_diff_elem = None

for i in range(1, len(arr)):
    diff = arr[i] - arr[i-1]
    if diff >= 72:
        if max_diff_elem is None or arr[i] > max_diff_elem:
            max_diff_elem = arr[i]

if max_diff_elem is None:
    print("5. Таких элементов нет")
else:
    print("5. Максимальный элемент с разностью соседних элементов не менее 72: ", max_diff_elem)

# 6
max_element = float('-inf')
min_element = float('inf')
found = False
for i in range(1, len(arr)):
    if (arr[i] % arr[i-1]) == 0 and (arr[i] // arr[i-1]) % 2 == 0:
        found = True
    if arr[i] > max_element:
        max_element = arr[i]
    if arr[i] < min_element:
        min_element = arr[i]
if found:
    print("6. Максимальный элемент:", max_element)
    print("6. Минимальный элемент:", min_element)
else:
    print("6. Нет подходящих элементов в массиве.")

# 7
result = []
for i in range(len(arr)-1):
    if (arr[i] - arr[i+1]) % 2 == 0:
        result.append(arr[i])
if len(result) == 0:
    print("7. Нет элементов, разность соседних которых четная")
else:
    min_element = min(result)
    max_element = max(result)
    print("7. Минимальный элемент: ", min_element,
          " Максимальный элемент: ", max_element)

# 8
elem = arr[2]  # ищем элемент со значением 40
sum_before = 0  # сумма элементов до искомого элемента
count_before = 0  # количество элементов до искомого элемента
for i in range(len(arr)):
    if arr[i] == elem:
        if count_before == 0:
            print("8. Нет элементов, среднее арифметическое которых равно 12")
        else:
            avg_before = sum_before / count_before
            print(f"8. ", arr[i])
            break
    else:
        sum_before += arr[i]
        count_before += 1
#else:
    #print("8. Нет элементов со значением", elem)

# 9
max_num = 0
for num in arr:
    if num % 10 == 0 and num > max_num:
        max_num = num
if max_num == 0:
    
    print("9. Нет элементов в массиве, делящихся на 10.")
else:
    print("9. Максимальный элемент в массиве, делящийся на 10, равен", max_num)

# 10 четное число и делится на 3
for i in range(1, len(arr)):
    if (arr[i] - arr[i-1]) % 2 == 0 and (arr[i] - arr[i-1]) % 3 == 0:
        print("10. Элемент = ", arr[i])
        break
else:
    print("10. Такого элемента нет")

# 11 
sum_sq = 0
count = 0
max_el = None
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        sum_sq += arr[j]**2
        count += 1
    if sum_sq / count <= 10:
        print("11. ", arr[i])
        break
    else:
        print("Не найдено")
# 12
max_tg = -math.inf
max_index = -1
for i in range(len(arr)):
    tg_x = math.tan(arr[i])
    if tg_x > max_tg:
        max_tg = tg_x
        max_index = i
        arr[i] = tg_x
        arr[0], arr[max_index] = arr[max_index], arr[0]
