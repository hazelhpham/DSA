"""
1. traverse to the prefix node
- start at the root of the trie and follow the characters of the 
input prefix one by one. If you reach the end of prefix, you're at the node
where the suggestions should branch out. 

2. DFS to collect words:
- from the prefix node, perform DFS to traverse all possible paths. 
- each path you traverse forms a complete word by concatenating the characters
along the path from the root to terminal node. 

3. Word Formation:

During the DFS, whenever you encounter a node marked as the "end of a word," the characters traversed so far (from the prefix node to this node) form a valid auto-complete suggestion.

4. Additional Features (Optional):

If you store metadata (e.g., word frequency or recency) in each node, use it to rank or filter the suggestions.

"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def find_prefix_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    
    def dfs(self, node, prefix, suggestions):
        if node.is_end_of_word:
            suggestions.append(prefix)
        for char, child_node in node.children.items():
            self.dfs(child_node, prefix + char, suggestions)

    def autocomplete(self, prefix):
        node = self.find_prefix_node(prefix)
        if not node:
            return []
        suggestions = []
        self.dfs(node, prefix, suggestions)
        return suggestions

# Example Usage
trie = Trie()
words = ["apple", "approval", "banana", "band", "bandana"]
for word in words:
    trie.insert(word)

print(trie.autocomplete("ap"))  # Output: ['apple', 'approval']
print(trie.autocomplete("ban"))  # Output: ['banana', 'band', 'bandana']
