class Solution:
    def countPalindromes(self, s, i, j):
        count = 0
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break

            i -= 1
            j += 1
            count += 1

        return count

    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.countPalindromes(s, i, i)
            count += self.countPalindromes(s, i, i+1)
            
        return count