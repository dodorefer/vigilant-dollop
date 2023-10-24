from queue import Queue //

queue = Queue()


class Node:
    def __init__(self, data):
        self.leftChild = None
        self.rightChild = None
        self.data = data
        self.parent = None

    # Insert Node
    def insert(self, data):
        if data >= self.data:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                self.rightChild.parent = self
        else:
            if self.leftChild:
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                self.leftChild.parent = self

    def preorderTraversal(self, root):
        ret = []
        if root:
            ret = ret + self.preorderTraversal(root.leftChild)
            ret.append(root.data)
            ret = ret + self.preorderTraversal(root.rightChild)
        return ret

    def get_type(self, root):
        ret = []
        if root:
            ret = ret + self.get_type(root.leftChild)
            if root.parent and (root.leftChild or root.rightChild):
                ret.append([root.data, 'П'])
            elif root.parent is None:
                ret.append([root.data, 'К'])
            else:
                ret.append([root.data, 'Л'])
            ret = ret + self.get_type(root.rightChild)
        return ret


def getLevelUtil(node, data, level):
    if (node == None):
        return 0

    if (node.data == data):
        return level

    downlevel = getLevelUtil(node.leftChild, data, level + 1)
    if (downlevel != 0):
        return downlevel

    downlevel = getLevelUtil(node.rightChild, data, level + 1)
    return downlevel


def getLevel(node, data):
    return getLevelUtil(node, data, 1)


def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.leftChild), height(node.rightChild)) + 1


root = Node(27)
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

# Описать процедуру или функцию, которая:
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

