###### error solution ########
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        Len = 3
        maxLen = 1 
        flag = True
        site = 1 
        #   a#b#b
        #   c#c#c
        arr = list(s)
        s2 = '^'+'#'.join(arr)+'$'
        arr = list(s2)
        arrLen = len(arr) 
        for index,i in enumerate(arr):
            if flag:
                if index > 0 and i == arr[index - 2]:
                    flag = False
                    Len = 3
            else:
                if index >= Len and i == arr[index-Len-1]:
                    Len += 2
                else:
                    flag = True
                    if maxLen < Len:
                        site = index-1
                        maxLen = Len
                    elif maxLen == Len:
                        if not arr[index - 1] == '#':
                          site = index-1
                          maxLen = Len
                    if i == arr[index - 2]:
                        flag = False
                        Len = 3
        if arrLen == 1:
            return s
        return ''.join(arr[site-maxLen+1:site+1]).replace("#", "")
str = 'bbbbbb'
test = Solution()
res = test.longestPalindrome(str)
print(res)
