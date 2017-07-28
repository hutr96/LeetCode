class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        best = 0
        sig = -1
        type = 0
        dic = {}
        length = 1
        for i, val in enumerate(s):
            dic[i] = val
            if i == 1:
                if dic[i]==dic[i-1]:
                    sig = i
                    type = 2
                    # length = 2 * (i - sig) + 2
                    # best = sig
                    # length = 2
            if i>1:
                if dic[i]==dic[i-2]:
                    sig = i-1
                    type = 1
                elif dic[i]==dic[i-1]:
                    sig = i
                    type = 2

            if sig != -1:
                if type==1 and i-2*(i-sig)>=0:
                    if dic[i]==dic[i-2*(i-sig)] and 2*(i-sig)+1 > length:
                        length = 2*(i-sig)+1
                        best = sig

                if type==2 and i-1-2*(i-sig)>=0:
                    if dic[i]==dic[i-1-2*(i-sig)] and 2*(i-sig)+2 > length:
                        length = 2*(i-sig)+2
                        best = sig


        print "bestsig = "+str(best)
        print "length = "+str(length)
        if length%2 ==0:
            result = s[best-length/2:best+length/2]
        if length%2 ==1:
            result = s[best-(length-1)/2:best+(length+1)/2]

        return result


if __name__ == "__main__":
    Solution = Solution()
    # s ="babad"
    # print  s[1:3]
    print Solution.longestPalindrome("ababad")
