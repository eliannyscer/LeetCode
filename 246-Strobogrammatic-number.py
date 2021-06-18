#Here is the code using a Hash Map

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        
        rotated_string_builder = []
        
        for c in reversed(num):
            if c not in rotated_digits:
                return False
            rotated_string_builder.append(rotated_digits[c])
        
        rotated_string = "".join(rotated_string_builder)
        return rotated_string == num

'''' 
https://leetcode.com/problems/strobogrammatic-number/solution/
'''