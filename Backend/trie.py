class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0  # how many times this word was searched


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the Trie -> O(L)
    def insert(self, word):
        word = word.strip().lower()
        if not word:
            return

        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        current.is_end_of_word = True

    # Find the node that matches a prefix -> O(L)
    def find_prefix_node(self, prefix):
        current = self.root
        for char in prefix.strip().lower():
            if char not in current.children:
                return None
            current = current.children[char]
        return current

    # Exact word search -> O(L)
    def search(self, word):
        node = self.find_prefix_node(word)
        return node is not None and node.is_end_of_word

    # Check if any word starts with the prefix -> O(L)
    def starts_with(self, prefix):
        return self.find_prefix_node(prefix) is not None

    # Increase popularity of a word (used for ranking)
    def increment_frequency(self, word):
        node = self.find_prefix_node(word)
        if node is not None and node.is_end_of_word:
            node.frequency += 1

    # Return top suggestions: most searched first, then alphabetical
    def autocomplete(self, prefix, limit=10):
        prefix = prefix.strip().lower()
        if not prefix:
            return []

        start = self.find_prefix_node(prefix)
        if start is None:
            return []

        matches = []  # (frequency, word)

        def collect(node, current_word):
            if node.is_end_of_word:
                matches.append((node.frequency, current_word))
            for char in sorted(node.children):
                collect(node.children[char], current_word + char)

        collect(start, prefix)

        matches.sort(key=lambda item: (-item[0], item[1]))
        return [word for _, word in matches[:limit]]