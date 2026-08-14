class Solution:
    def maxFreqSum(self, s: str) -> int:
        c= Counter(s)
        vowel = max((c[ch] for ch in c if ch in "aeiou"), default=0)
        consonant = max((c[ch] for ch in c if ch not in "aeiou"), default=0)
        return vowel + consonant     