class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        d = 1
        while x/d >= 10:
            d *= 10
        while x > 0 :
            if int(x/d) != x%10:
                return False
            else:
                x = int(x%d/10);
                d = d/100
        return True        
test = Solution()
if test.isPalindrome(1001):
	print(1)
