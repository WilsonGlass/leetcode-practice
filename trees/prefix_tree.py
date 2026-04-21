"""
A trie (pronounced as "try") or prefix tree is a tree data
structure used to efficiently store and retrieve
keys in a dataset of strings. There are various applications
of this data structure, such as autocomplete and spellcheckers.

Implement the trie class:
* Trie() initializes the trie object
* def insert(word: str) -> None: inserts the string word into the trie
* def search(word: str) -> bool: returns true if the string word is in the trie
(i.e., was inserted before), and false otherwise
* def starts_with(prefix: str) -> bool: returns true if there is a previously inserted
string _word_ that has the prefix _prefix_, and false otherwise.

E.g.
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
"""

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.word

    def starts_with(self, prefix) -> bool:
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True




