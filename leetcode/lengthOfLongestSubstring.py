class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        len = 0
        arr = list(s)
        for index,i in enumerate(arr):
            if i not in arr[index-len+1:index]:
                len +=1
                print(arr[index-len+1:index])
        return len 

str = 'wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco'
test = Solution()
res = test.lengthOfLongestSubstring(str)
print(res)
