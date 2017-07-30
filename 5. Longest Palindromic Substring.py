# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         best = 0
#         sig = -1
#         type = 0
#         dic = {}
#         length = 1
#         for i, val in enumerate(s):
#             dic[i] = val
#             if i == 1:
#                 if dic[i]==dic[i-1]:
#                     sig = i
#                     type = 2
#                     # length = 2 * (i - sig) + 2
#                     # best = sig
#                     # length = 2
#             if i>1:
#                 if dic[i]==dic[i-2]:
#                     sig = i-1
#                     type = 1
#                 elif dic[i]==dic[i-1]:
#                     sig = i
#                     type = 2
#
#             if sig != -1:
#                 if type==1 and i-2*(i-sig)>=0:
#                     if dic[i]==dic[i-2*(i-sig)] and 2*(i-sig)+1 > length:
#                         length = 2*(i-sig)+1
#                         best = sig
#
#                 if type==2 and i-1-2*(i-sig)>=0:
#                     if dic[i]==dic[i-1-2*(i-sig)] and 2*(i-sig)+2 > length:
#                         length = 2*(i-sig)+2
#                         best = sig
#
#
#         print "bestsig = "+str(best)
#         print "length = "+str(length)
#         if length%2 ==0:
#             result = s[best-length/2:best+length/2]
#         if length%2 ==1:
#             result = s[best-(length-1)/2:best+(length+1)/2]
#
#         return result


# Solution from LeetCode@caikehe    Accepted 1242ms
def longestPalindrome(self, s):
    res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i + 1)
        if len(tmp) > len(res):
            res = tmp
    return res
# To make it short, we can use "max":
# res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)

# get the longest palindrome, l, r are the middle indexes
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1;
        r += 1
    return s[l + 1:r]

# Solution from LeetCode@Chomolungma 88ms
def longestPalindrome2(self, s):
    if len(s) == 0:
        return 0
    maxLen = 1
    start = 0
    for i in xrange(len(s)):
        if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:  # [::-1]represent reverse the list
            start = i - maxLen - 1
            maxLen += 2
            continue

        if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
            start = i - maxLen
            maxLen += 1
    return s[start:start + maxLen]

if __name__ == "__main__":
    Solution = Solution()
    # s ="babad"
    # print  s[1:3]
    print Solution.longestPalindrome("ababad")
