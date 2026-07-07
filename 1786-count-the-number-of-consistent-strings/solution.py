class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        for word in words:
            if all(ch in allowed for ch in word):
                c+=1
        return c
