class Solution:
    def reverse(self, x: int) -> int:
        min_num = -2**31
        max_num = 2**31 -1

        default_num = 1 

        if x < 0:
            default_num = -1
            x = -x
        
        reversed_num = 0

        while x > 0:
            digit = x % 10
            x = x // 10

            if reversed_num > (max_num) // 10:
                return 0
            
            reversed_num = reversed_num * 10 + digit 

        return default_num * reversed_num
