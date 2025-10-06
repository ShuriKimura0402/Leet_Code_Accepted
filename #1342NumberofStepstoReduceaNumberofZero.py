class Solution(object):
    def numberOfSteps(self, num):
        tries = 0
        while num > 0:
            if num % 2 == 1:
                num -= 1
            elif num % 2 == 0:
                num //= 2
            tries += 1
        return tries 
