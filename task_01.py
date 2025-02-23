from trie import Trie


class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        """
        Counts the number of words in the Trie that end with a given suffix.

        Args:
            pattern (str): The suffix to search for

        Returns:
            int: The number of words with the given suffix
        """
        # Перевірка вхідних даних
        if not isinstance(pattern, str) or not pattern:
            raise TypeError("Prefix must be a non-empty string")

        count = sum(1 for key in self.keys() if key.endswith(pattern))
        # print(f"Words with suffix '{pattern}': {count}")
        return count

    def has_prefix(self, prefix) -> bool:
        """
        Checking for words with a given prefix in the Trie.

        Args:
            prefix (str): The prefix to search for.

        Returns:
            bool: True if the prefix is found, False otherwise.

        Raises:
            TypeError: If the prefix is not a non-empty string.
        """
        # Перевірка вхідних даних
        if not isinstance(prefix, str) or not prefix:
            raise TypeError("Prefix must be a non-empty string")

        current_node = self.root
        path = []
        # Пошук префікса
        for char in prefix:
            if char not in current_node.children:
                print(f"Prefix '{prefix}' not found. Found part: '{''.join(path)}'")
                return False
            path.append(char)
            current_node = current_node.children[char]
        return True


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка наявності префікса
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

    print("All tests passed")
