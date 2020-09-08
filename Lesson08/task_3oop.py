import collections
import operator


class Leaf:
    '''Leaf - Вспомогательный класс для создания дерева Хаффмана
    char - символ из кодируемой строки
    value - часлтота буквы в строке'''

    def __init__(self, char: str, *value: int):
        if isinstance(char, tuple):
            self.char, self.value = char
        else:
            self.char = char
            self.value = value

    def __repr__(self):
        return f'Leaf : char "{self.char}" value {self.value}'


class Node:
    """Вспомогательный  класс Node для построоения дерева Хаффмана"""

    def __init__(self, value: int, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        return f'Node : {self.value}\n left --> {self.left} \n right-->{self.right}'


class Haff_code:
    """Основной класс для реализации алгоритма Хаффмана"""

    def __init__(self):
        self.result_code = {}

    def _get_table(self, tree, code=''):
        if isinstance(tree, Node):
            self._get_table(tree.left, code=f'{code}0')
            self._get_table(tree.right, code=f'{code}1')
        elif isinstance(tree, Leaf):
            self.result_code[tree.char] = code  # сюда помещается уже накопленный код из 0 и 1

    def encode(self, string, detail=False):
        """Main метод для кодироывания строки"""
        self.result_code = {}  # {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
        count = collections.Counter(string)
        array = collections.deque(
            map(Leaf, count.most_common()))  # ПО УМОЛЧАНИЮ КОРТЕЖ  в Leaf есть учловие для кортежа
        if detail:
            print(array)  # массив из листьев пока неупорядоченно
            # deque([Leaf : char "e" value 2, Leaf : char "b" value 1, Leaf : char "p" value 1])
            print(count)  # Counter({'e': 2, 'b': 1, 'p': 1})

        while len(array) > 1:  # формируем дерево и сортируем по возрастанию
            array = collections.deque(sorted(array, key=operator.attrgetter('value')))
            left_small = array.popleft()
            right_bigger = array.popleft()
            array.append(Node(left_small.value + right_bigger.value, left_small, right_bigger))
        tree = array.pop()
        if detail:
            # print(array[0])  # Дерево хафмана
            print(tree)
        self._get_table(tree)
        if detail:
            print(self.result_code)  # таблица кодирования
        return ' '.join([self.result_code[char] for char in string])


if __name__ == '__main__':
    haff = Haff_code()
    print(haff.encode('beep boop beer!'))

    print('*' * 50)
    my_str = input('введите строку для кодирования ')  # beep
    print(haff.encode(my_str, detail=True))
