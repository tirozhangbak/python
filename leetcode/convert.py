class Solution:
    # @return a string
    def convert(self, s, nRows):
        arr = list(s)
        arrLen = len(arr)
        if nRows == 1:
            return s
        str = ''
        i = 0
        j = 1 
        while i < nRows and i < arrLen:
            str += arr[i];
            while j*(nRows - 1)*2 + i < arrLen:
                if i != 0 and i != nRows-1 and j != 0:
                    str += arr[j*(nRows - 1)*2 - 2*i]
                str += arr[j*(nRows - 1)*2];
                j += 1
            i +=1
            j = 0
        return str
test = Solution()
res = test.convert('ABCDEFGHIGKLMN',4)
print(res)
