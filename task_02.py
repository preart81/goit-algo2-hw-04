from trie import Trie
from pprint import pprint


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        """
        Finds the longest common prefix among a list of strings.

        Args:
            strings (list): A list of strings to find the longest common prefix.

        Returns:
            str: The longest common prefix shared by all strings in the list.

        Raises:
            TypeError: If the input is not a non-empty list of strings.
        """

        if not isinstance(strings, list) or not strings:
            raise TypeError("Strings must be a non-empty list")

        for string in strings:
            if not isinstance(string, str):
                raise TypeError(
                    f"Expected a list of strings, but got {type(string)} '{string}'"
                )

        # Insert each string into trie
        for i, string in enumerate(strings):
            self.put(string, i)

        current_node = self.root
        longest_common_prefix = []

        for i in range(len(strings[0])):
            char = strings[0][i]
            if (
                char in current_node.children
                and len(current_node.children) == 1
                and current_node.value is None
            ):
                longest_common_prefix.append(char)
                current_node = current_node.children[char]
            else:
                break
        print(
            f"'{''.join(longest_common_prefix)}' is the longest common prefix for {strings}"
        )
        return "".join(longest_common_prefix)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = ["flower", "flow", "flounder", "f"]
    assert trie.find_longest_common_word(strings) == "f"

    print("All tests passed")
