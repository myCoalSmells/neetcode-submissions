from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_counts_to_word = defaultdict(list) # tuple of len 26 of the counts
        for word in strs:
            # get the hash key aka the letter counts of the word
            letter_counts = [0] * 26
            for c in word:
                index = ord(c) - ord('a')
                letter_counts[index] += 1
            letter_counts_to_word[tuple(letter_counts)].append(word)
        res = []
        for anagrams in letter_counts_to_word.values():
            res.append(anagrams)
        return res

        