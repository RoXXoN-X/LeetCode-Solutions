class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert to string and compare with reverse
        str_x = str(x)
        return str_x == str_x[::-1]