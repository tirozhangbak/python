class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        ans = 1
        while n > 1:
            ans *= n
            n -= 1
        num = 0
        while True:
            if ans%10 == 0:
              ans = ans/10
              num +=1
            else:
              break
        return num
    def trailingZeroesTwo(self, n):
        ans = 0
        x = 5
        while n >= x:
          ans += n / x
          x *= 5
        return ans


test = Solution()
res = test.trailingZeroes(15555)
res2 = test.trailingZeroesTwo(15555)
print(res)
print(res2)
