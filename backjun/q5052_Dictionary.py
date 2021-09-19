_end = '_end_'
def Trie(letters):
    root = dict()
    for letter in letters:
        current_dict = root
        for word in letter:
            if _end in current_dict :
                return 'NO'
            current_dict = current_dict.setdefault(word, {})
        current_dict[_end] = _end
    return 'YES'


for _ in range(int(input())):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(input())
    print(Trie(sorted(data)))