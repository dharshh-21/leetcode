class TrieNode:
    def __init__(self):
        self.children = {}   # dictionary to store child nodes
        self.isEnd = False   # marks end of a word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    # Search for a full word
    def search(self, word):
        node = self._find(word)
        return node is not None and node.isEnd

    # Check if any word starts with given prefix
    def startsWith(self, prefix):
        return self._find(prefix) is not None

    # Helper function
    def _find(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


# Example usage
trie = Trie()
trie.insert("apple")

print(trie.search("apple"))    # True
print(trie.search("app"))      # False
print(trie.startsWith("app"))  # True

trie.insert("app")
print(trie.search("app"))      # True