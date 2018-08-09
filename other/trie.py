class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False

    def __str__(self):
        return 'Trie node, is word: {}'.format(self.is_word)


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node


if __name__ == '__main__':
    t = Trie()
    print t.find('abc')

    t.insert('abc')
    print t.find('abc')
    print t.find('ab')

    
