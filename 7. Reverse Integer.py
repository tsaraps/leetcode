# Task
# https://leetcode.com/problems/reverse-integer/

# Solution
class Solution:
    def reverse(self, x: int) -> int:
        number = x
        reverse_number = 0
        if x < 0:
            number *= -1
        while number:
            number, temp = divmod(number, 10)
            reverse_number = reverse_number * 10 + temp
        reverse_number = reverse_number if x >= 0 else reverse_number * -1
        if reverse_number < -2147483648 or reverse_number > 2147483647:
            reverse_number = 0
        return reverse_number
