class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        len = 0
        maxLen = 0
        arr = list(s)
        for index,i in enumerate(arr):
            if i not in arr[index-len:index]:
              #print(arr[index-len:index])
              len +=1
            else:
              print(arr[index-len:index])
              maxLen = max(maxLen,len)
              len = index - (arr[index-len:index].index(i) + index-len) 
        return max(maxLen,len) 

str = 'qopubjguxhxdipfzwswybgfylqvjzhar'
test = Solution()
res = test.lengthOfLongestSubstring(str)
print(res)
