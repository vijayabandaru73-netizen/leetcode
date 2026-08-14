class Solution:
    def uniqueOccurrences(self, arr):
        freq = {}

        for i in arr:
            freq[i] = freq.get(i, 0) + 1

        values = list(freq.values())

        return len(values) == len(set(values))