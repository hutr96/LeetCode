class Solution(object):
    def lengthOfLongestSubstring(self, s):      # Accepted 82ms
        """
        :type s: str
        :rtype: int
        """
        start = 0
        result =0
        dic = {}
        for i, val in enumerate(s):
            if val in dic:
                result = max(result, i-start)
                start = max(start, dic[val]+1)

            dic[val] = i
        return max(result, len(s)-start)






if __name__ == "__main__":
    Solution=Solution()
    print Solution.lengthOfLongestSubstring('abcabcbb')
