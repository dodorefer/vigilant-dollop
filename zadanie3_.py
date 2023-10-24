from queue import Queue # код реализует структуру данных бинарного дерева с методами вставки, обхода и анализа узлов.

queue = Queue()


class Node: # определяем класс node, который представляет узел в дереве
    def __init__(self, data): 
        # Метод __init__ инициализирует узел с заданными данными и устанавливает все атрибуты в значения по умолчанию
        # Узел имеет атрибуты leftChild, rightChild, data и parent //
        self.leftChild = None
        self.rightChild = None
        self.data = data
        self.parent = None

  
  #  1. Описать процедуру или функцию, которая:
  # a) присваивает параметру Е запись из самого левого листа непустого дерева Т (листвершина, из которого не выходит ни одной ветви);
  # b) определяет число вхождений записи Е в дерево Т.
    # Insert Node
    def insert(self, data): # Метод insert используется для вставки нового узла в дерево. 
    # Он рекурсивно проходит по дереву, сравнивая значение нового узла с текущим узлом. 
        if data >= self.data:
            if self.rightChild: # Если значение больше или равно текущему узлу, оно добавляется в правое поддерево.
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data) # Если правое поддерево уже существует, метод рекурсивно вызывается для этого поддерева.
                self.rightChild.parent = self
        else:
            if self.leftChild: # Если значение меньше текущего узла, оно добавляется в левое поддерево.
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data) # Если левое поддерево уже существует, метод рекурсивно вызывается для этого поддерева.
                self.leftChild.parent = self

    def preorderTraversal(self, root): # Метод preorderTraversal выполняет обход дерева в прямом порядке.
        ret = []
        if root:  # Он использует рекурсию и добавляет значения узлов в список ret в порядке: 
        # левый поддерево, корень, правое поддерево. В конце возвращает список ret.
            
            ret = ret + self.preorderTraversal(root.leftChild)
            ret.append(root.data)
            ret = ret + self.preorderTraversal(root.rightChild)
        return ret

# #возвращает список кортежей, где каждый кортеж содержит значение узла и строку, указывающую тип узла
# «К» для корневого узла, «Л» для конечного узла и «П» для конечного узла
    def get_type(self, root): # Метод get_type также выполняет рекурсивный обход дерева. 
        ret = []
        if root:
            ret = ret + self.get_type(root.leftChild) # Он использует рекурсию и добавляет в список ret типы узлов: 
            // 'П' (предок), 'К' (корень) или 'Л' (лист). 
            if root.parent and (root.leftChild or root.rightChild):
                ret.append([root.data, 'П'])
            elif root.parent is None:
                ret.append([root.data, 'К'])
            else:
                ret.append([root.data, 'Л'])
            ret = ret + self.get_type(root.rightChild) # Тип узла определяется наличием родительского узла и наличием потомков. 
            # В конце возвращает список ret.
        return ret


def getLevelUtil(node, data, level): # Функция getLevelUtil используется для определения уровня узла в дереве.
    # Она использует рекурсию и проверяет каждый узел дерева в поиске заданного значения.
    if (node == None): 
        return 0

    if (node.data == data): # Если значение найдено, функция возвращает уровень этого узла.
        return level

    downlevel = getLevelUtil(node.leftChild, data, level + 1) # Если значение не найдено, 
     # функция рекурсивно вызывается для левого и правого поддеревьев. 
    if (downlevel != 0):
        return downlevel

    downlevel = getLevelUtil(node.rightChild, data, level + 1)
    return downlevel


def getLevel(node, data): # Функция getLevel просто вызывает функцию getLevelUtil, передавая в нее корень дерева и заданное значение.
    return getLevelUtil(node, data, 1)


def height(node): # Функция height используется для определения высоты дерева. Она также использует рекурсию. 
    if node is None: # Если узел не существует (равен None), функция возвращает 0.
        return 0
    else:
        return max(height(node.leftChild), height(node.rightChild)) + 1 # Иначе функция рекурсивно вызывается для левого 
       # и правого поддеревьев и возвращает максимальное значение из двух высот, увеличенное на 1.


root = Node(27) # Затем создается корневой узел дерева с значением 27 и выполняются повторные вставки для добавления других узлов в дерево.
# Затем он выполняет различные операции с деревом, такие как поиск наиболее распространенных и наименее 
# распространенных значений узлов, вставка нового узла с заданным значением и копирование дерева.

root.insert(14)
root.insert(5)
root.insert(-10)
root.insert(-1)
root.insert(5)
root.insert(3)
root.insert(31)
root.insert(-2)
root.insert(6)
root.insert(27)
root.insert(9)
A = root.preorderTraversal(root)
E = A[0]
print('1)', E, root.preorderTraversal(root).count(E))
print('2)', sum(A) / len(A))
root.insert(sum(A) / len(A))
N = [i for i in A if i < 0]
newroot = Node(N[0])
for i in N[1:]:
    newroot.insert(i)
print('3)', N)
print("4)", max(A), min(A))
print("4)", A)
E = 18
if E in A:
    print(E)
else:
    root.insert(E)
A = root.preorderTraversal(root)
print("5)", A)
print('6)max height: ', height(root))
print('height of 31: ', getLevel(root, 31))
to_copy = [i for i in root.preorderTraversal(root)]
copy_root = Node(to_copy[0])
for i in to_copy[1:]:
    copy_root.insert(i)
print('7) ', copy_root.preorderTraversal(copy_root))
print('8) equal?', copy_root.preorderTraversal(copy_root) == root.preorderTraversal(root))
root.insert(2)
print('equal?', copy_root.preorderTraversal(copy_root) == root.preorderTraversal(root))
print('9)', root.get_type(root))
print('10)', max(root.preorderTraversal(root)))
root.insert(max(root.preorderTraversal(root)))
print(root.preorderTraversal(root))

# 11 Описать процедуру или функцию, которая:
# а) вставляет узел с записью Е в дерево, если ранее такой не было;
# b) считает и выдает на экран сумму значений всех ключей, если такая запись есть.
if 5 in root.preorderTraversal(root):
    root.insert(5)
    print('Вставили 5')
else:
    print('Запись есть, сумма всех полей', sum(root.preorderTraversal(root)))

# №12. Описать процедуру или функцию, которая:
# а) печатает запись, встречающуюся в дереве один раз;
# b) печатает запись, встречающееся в дереве максимальное число раз.
ll = root.preorderTraversal(root)
count_dict = {i: ll.count(i) for i in ll}
print(count_dict)
print(max(count_dict, key=lambda x: count_dict[x]), 'Больше всего встречается')
print(min(count_dict, key=lambda x: count_dict[x]), 'Меньше всего встречается')

