# Task
# https://leetcode.com/problems/palindrome-number/

# Solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        is_palindrome = False
        if x < 0:
            return False
        number = x
        reverse_number = 0
        while number:
            number, temp = divmod(number, 10)
            reverse_number = reverse_number * 10 + temp
        return x == reverse_number
