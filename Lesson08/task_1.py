import hashlib


def h_papa(s):
    h_s = set()
    sub_s = set()
    count = 0
    for i in range(len(s)):
        for j in range(len(s) + 1):
            if len(s[i:j]) != len(s) and s[i:j] != '':
                h_s.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
                sub_s.add(s[i:j])
                count += 1

    return f'количество подстрок в строке \'{s}\' = {len(h_s)}'


egg = input('Enter any string :')
print(h_papa(egg))
