class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        len = 0
        maxLen = 0
        arr = list(s)
        for index,i in enumerate(arr):
            if i not in arr[index-len+1:index]:
              len +=1
              print(arr[index-len+1:index])
            else:
              print(arr[index-len+1:index])
              maxLen = max(maxLen,len)
              len = index - (arr[index-len+1:index].index(i) + index-len+1) 
              print(len)
        return maxLen 

str = 'hchzvfrkmlnozjk'
test = Solution()
res = test.lengthOfLongestSubstring(str)
print(res)
