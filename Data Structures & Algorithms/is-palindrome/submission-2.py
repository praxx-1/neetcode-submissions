class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new=""
        for x in s:
            if x.isalpha() or x.isdigit() :
                new+=x

        return new == new[::-1]