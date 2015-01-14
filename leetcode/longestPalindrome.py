class Solution:
    # @return a string
    def longestPalindrome(self, s):
        max = 0 
        id = 0
        maxLen = 1
        site = 0 
        hash ={}
        arr = list(s)
        s = '#'+'#'.join(arr)+'#'
        arr = list(s)
        for index,i in enumerate(arr):
            if index < max :
                hash[index] = min(hash[2*id - index],max - index)
            else:
                hash[index] = 1
            while index >= hash[index] and index+hash[index] < len(arr) and arr[index+hash[index]] == arr[index-hash[index]]:
                hash[index] += 1
            if (hash[index] + index) > max:
                max = hash[index] + index -1
                id = index
            if maxLen < hash[index]:
                maxLen = hash[index]
                site = index
        return ''.join(arr[site-maxLen+1:site+maxLen]).replace("#", "")
str = 'a'
test = Solution()
res = test.longestPalindrome(str)
print(res)
