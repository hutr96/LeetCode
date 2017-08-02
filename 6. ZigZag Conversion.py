class Solution(object):                 # Accepted 169ms
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if numRows == 1:
            return s
        dic = {}
        count = 0
        count2 = 0
        ls =[]
        res = []
        for i, val in enumerate(s):
            if count < numRows:
                dic[i+count*length] = val
                count += 1
            elif count == numRows and count2 == 0:
                if count > 2:
                    count2 = count - 2
                else:
                    count2 = 0
                    count = 1
                dic[i + count2 * length] = val

            elif count == numRows and count2 != 0:
                count2 -= 1
                dic[i + count2 * length] = val
                if count2 == 0:
                    count = 1
        # print dic
        for key in dic:
            ls.append(key)
        ls.sort()
        # print ls
        for key in ls:
            res.append(dic[key])
        return ''.join(res)






if __name__ == "__main__":
    S = Solution()
    print S.convert("PAYPALISHIRING",4)
