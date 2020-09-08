from collections import Counter, deque
import operator


def haff_tree(s_start):
    s_start = Counter(s_start)
    s_start = sorted(s_start.items(), key=lambda xxx: xxx[1])
    s_start = deque(s_start)

    if len(s_start) != 1:
        while len(s_start) > 1:
            wt_two = s_start[0][1] + s_start[1][1]
            char_two = {0: s_start.popleft()[0],
                        1: s_start.popleft()[0]}
            connect_two = char_two, wt_two
            for i, item in enumerate(s_start):
                if wt_two > item[1]:
                    continue
                s_start.insert(i, connect_two)
                break

            else:
                s_start.append(connect_two)

    return s_start[0][0]


s = "beep boop beer!"
result_tree = haff_tree(s)
print(result_tree)  # словарь-дерево
# {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'},

result_code = {}


def haff_code(h_tree, code=''):
    if isinstance(h_tree, str):
        result_code[h_tree] = code
    else:
        haff_code(h_tree[0], code=f'{code}0')
        haff_code(h_tree[1], code=f'{code}1')


haff_code(result_tree)
print(result_code)  # словарь символов и кода
# {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
for k, v in result_code.items():
    print(v, end=' ')  # отсепапрированный код 00 010 011 1000 1001 101 11
