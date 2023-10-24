stack = [1, 2, 3, 4, 5]

stack = list(map(str, stack))

# 1. Поменять местами первый и последний элементы стека
stack[0], stack[-1] = stack[-1], stack[0]
print(stack)  

# 2. Развернуть стек
stack.reverse()
print(stack)  

# 3. Удалить элемент в середине стека
if len(stack) % 2 == 0:
    del stack[len(stack) // 2 - 1: len(stack) // 2 + 1]
else:
    del stack[len(stack) // 2]
print(stack) 

# 4. Удалить каждый второй элемент стека
del stack[1::2]
print(stack)  

# 5. Вставить символ ‘*’ в середину стека
if len(stack) % 2 == 0:
    stack.insert(len(stack) // 2, '*')
print(stack)  

# 6. Найти минимальный элемент и вставить после него 0
min_index = stack.index(min(stack))
stack.insert(min_index + 1, 0)
print(stack)  

stack = list(map(str, stack))

# 7. Найти максимальный элемент и вставить после него 0
max_index = stack.index(max(stack))
stack.insert(max_index + 1, 0)
print(stack)  

stack = list(map(str, stack))

# 8. Удалить минимальный элемент
stack.remove(min(stack))
print(stack)  

# 9. Удалить все элементы, равные первому
stack = [x for x in stack if x != stack[0]]
print(stack)  # [0, 2, 5, 0]

# 10. Удалить все элементы, равные последнему
stack = [x for x in stack if x != stack[-1]]
print(stack)  # [2]

# 11. Удалить максимальный элемент
stack.remove(max(stack))
print(stack)  # [2]

stack = [1, 2, 3, 4, 5]

# 12. Найти минимальный элемент и вставить на его место 0
min_index = stack.index(min(stack))
stack[min_index] = 0
print(stack)  # [0]
