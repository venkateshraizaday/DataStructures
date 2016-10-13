class Node:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.words = []
        self.isTerminal = False


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        if word[0] not in self.root:
            self.root[word[0]] = Node()
        temp = self.root[word[0]]
        for i in range(len(word)):
            # print(temp.children,temp.count)
            temp.count += 1
            temp.words.append(word)
            if i == len(word) - 1:
                temp.isTerminal = True
            else:
                if word[i + 1] not in temp.children:
                    temp.children[word[i + 1]] = Node()
                temp = temp.children[word[i + 1]]

    def getCount(self, word):
        if word[0] not in self.root:
            return 0
        temp = self.root[word[0]]
        if len(word) == 1:
            return temp.count
        for c in word[1:]:
            if c not in temp.children:
                return 0
            temp = temp.children[c]
        return temp.count


n = int(input())
trie = Trie()
for iter in range(n):
    (mode, word) = input().split()
    if mode == "add":
        trie.insert(word)
        # print(trie.root)
    else:
        print(trie.getCount(word))