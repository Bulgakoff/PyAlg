from collections import Counter, deque


def haff_tree(s_start):
    s_start = Counter(s_start)
    s_start = sorted(s_start.items(), key=lambda xxx: xxx[1])
    s_start = deque(s_start)

    if len(s_start) != 1:
        while len(s_start) > 1:
            wt_two = s_start[0][1] + s_start[1][1]
            char_two = {0: s_start.popleft()[0], 1: s_start.popleft()[0]}
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

result_code = {}


def haff_code(h_tree, path=''):
    if not isinstance(h_tree, dict):
        result_code[h_tree] = path
    else:
        haff_code(h_tree[0], path=f'{path}0')
        haff_code(h_tree[1], path=f'{path}1')


haff_code(result_tree)
print(result_code)  # словарь символов и кода
for k, v in result_code.items():
    print(v, end=' ')  # отсепапрированный код
