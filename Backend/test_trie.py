import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        for w in ["car", "card", "care", "cat", "dog"]:
            self.trie.insert(w)

    def test_search_exact(self):
        self.assertTrue(self.trie.search("car"))
        self.assertFalse(self.trie.search("ca"))
        self.assertFalse(self.trie.search("bird"))

    def test_starts_with(self):
        self.assertTrue(self.trie.starts_with("ca"))
        self.assertFalse(self.trie.starts_with("x"))

    def test_autocomplete_alphabetical(self):
        self.assertEqual(self.trie.autocomplete("car"), ["car", "card", "care"])

    def test_autocomplete_limit(self):
        self.assertEqual(len(self.trie.autocomplete("ca", limit=2)), 2)

    def test_no_match_and_empty(self):
        self.assertEqual(self.trie.autocomplete("zzz"), [])
        self.assertEqual(self.trie.autocomplete(""), [])

    def test_case_insensitive(self):
        self.assertEqual(self.trie.autocomplete("CAR"), ["car", "card", "care"])

    def test_frequency_ranking(self):
        self.trie.increment_frequency("care")
        self.trie.increment_frequency("care")
        self.trie.increment_frequency("card")
        self.assertEqual(self.trie.autocomplete("car"), ["care", "card", "car"])


if __name__ == "__main__":
    unittest.main()