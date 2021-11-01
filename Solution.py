"""
## Problem
The look-and-say sequence is defined as 
a = [1, 11, 21, 1211, 111221, ...], 
please include code in your application that calculates len(a[30])

## How to run
- Make sure the system have python3 installed.
- open a terminal and cd into the folder
- run `python3 solution.py`
"""
class Solution:
    """look at digits and return 
    next string in the sequence
    example: n = 11 will return 21 (two ones)
    """
    def __sayDigits(self, digits:str) -> str:
        current_digit = digits[0]
        counter = 0
        output = ""
        for d in digits:
            if d == current_digit:
                counter += 1
            else:
                output += str(counter)
                output += current_digit
                current_digit = d
                counter = 1
        output += str(counter)
        output += current_digit
        return output
    
    def __lookAndSay(self, n:int) -> str:
        if n == 1 :
            return "1"
        
        return self.__sayDigits(self.__lookAndSay(n-1))
    
    def getResult(self, n:int) -> int:
        sequence = self.__lookAndSay(n)
        return len(sequence)

# Run when file is directly called
if __name__ == '__main__':
    obj = Solution()
    print(obj.getResult(30))