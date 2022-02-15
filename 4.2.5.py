"""https://stepik.org/lesson/13239/step/5?unit=3425"""


class Node:
    def __init__(self, left=None, right=None, parent=None, val=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.val = val

    def __repr__(self):
        return f'Node {self.val}'


class Queue:
    def __init__(self, letters: list, freqs: list):
        self.queue = letters
        self.values = freqs

    def insert(self, obj, val):
        if not self.values:
            self.queue.append(obj)
            self.values.append(val)
        elif self.values[0] > val:
            self.queue.insert(0, obj)
            self.values.insert(0, val)
        elif self.values[-1] <= val:
            self.queue.append(obj)
            self.values.append(val)
        else:
            for i in range(len(self.values)):
                if val < self.values[i]:
                    self.queue.insert(i, obj)
                    self.values.insert(i, val)
                    break


def fwdict(root: Node, code_dict: dict, s=''):
    if isinstance(root, str):
        code_dict[root] = s
    else:
        fwdict(root.left, code_dict, s + '0')
        fwdict(root.right, code_dict, s + '1')


freq = {}
s = input()
for letter in set(s):
    freq[letter] = s.count(letter)
freq = dict(sorted(freq.items(), key=lambda x: x[1]))
f_list = Queue(list(freq.keys()), list(freq.values()))
while len(f_list.queue) > 1:
    # print(f_list.queue)
    # print(f_list.values)
    new_node = Node(left=f_list.queue.pop(0), right=f_list.queue.pop(0),
                    val=f_list.values.pop(0) + f_list.values.pop(0))
    f_list.insert(new_node, new_node.val)

root = f_list.queue[0]
key_dict = {}
if isinstance(root, str):
    key_dict[root] = '0'
else:
    fwdict(root, key_dict)
s_incode = ''
for letter in s:
    s_incode += key_dict[letter]
print(len(key_dict), len(s_incode))
for letter, code in sorted(key_dict.items(), key=lambda x: x[0]):
    print(f'{letter}: {code}')
print(s_incode)
