from queue import Queue

def swap_first_and_last(s): // поменять местами первый и последний элементы стека
    if len(s) == 0:
        return
    last = s[-1]
    s.pop()
    if len(s) == 0:
        s.append(last)
        return
    first = s[-1]
    s.pop()
    s.append(last)
    while len(s) > 0:
        temp = s[-1]
        s.pop()
        if len(s) == 0:
            s.append(first)
            s.append(temp)
        else:
            s.append(temp)

def remove_middle(s): // удалить элемент, находящийся в середине стека
    if len(s) == 0:
        return
    size = len(s)
    middle = size // 2
    if size % 2 == 0:
        middle -= 1
    temp = []
    for i in range(size):
        if i == middle:
            s.pop()
        else:
            temp.append(s[-1])
            s.pop()
    while len(temp) > 0:
        s.append(temp[-1])
        temp.pop()

def remove_every_second(s): // удаляем каждый второй элемент стека
    size = len(s)
    for i in range(1, size + 1):
        if i % 2 == 0:
            s.pop()

def search_min_zero(s): //  Находим минимальный элемент и вставляем 0
    minElement = s[-1]
    while len(s) > 0:
        if s[-1] < minElement:
            minElement = s[-1]
        s.pop()
        
s.append(minElement)
s.append("0")

def search_max_zero(s): // Находим максимальный элемент и вставляем 0
    maxElement = s[-1]
    while len(s) > 0:
        if s[-1] > maxElement:
            maxElement = s[-1]
        s.pop()
    s.append(maxElement)
    s.append("0")

def delete_min(s): //  удаляем минимальный элемент
    minElement = s[-1]
    tempStack = []
    while len(s) > 0:
        if s[-1] < minElement:
            minElement = s[-1]
        tempStack.append(s[-1])
        s.pop()

def delete_pervomu(s): //  удаляем элементы, равные первому
    tempStack = []
    tempStack.append(s[-1])
    s.pop()
    while len(s) > 0:
        if s[-1] != tempStack[-1]:
            tempStack.append(s[-1])
        s.pop()
    while len(tempStack) > 0:
        s.append(tempStack[-1])
        tempStack.pop()
