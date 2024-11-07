class Solution:
    def getLongestPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1: right]

    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        for i in range(0, len(s)):
            opt1 = self.getLongestPalindrome(s, i, i)
            opt2 = self.getLongestPalindrome(s, i, i + 1)

            if len(opt1) > len(longest_palindrome):
                longest_palindrome = opt1

            if len(opt2) > len(longest_palindrome):
                longest_palindrome = opt2

        return longest_palindrome