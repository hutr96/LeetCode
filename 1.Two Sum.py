class Solution:
    def twosum(self,nums,target): ##Time Limit Exceeded
        i = 0
        while i < len(nums):
            j=i+1
            while j < len(nums):
                if nums[i]+nums[j] == target:
                    return [i,j]
                j+=1
            i+=1


    def twosum2(self,nums,target):      #Pass 1200ms
        for i, num in enumerate(nums):
            try:
                j = nums.index(target-num)
                if j != i:
                    return [i,j]
                else:
                    continue
            except ValueError:
                continue

    def twosum3(self, nums, target):      #Pass 32ms
        """
        Hash Map: dictionary {}
        """
        hash_map = {}
        for i, val in enumerate(nums):
            hash_map[val] = i

        for i, val in enumerate(nums):
            if target-val in hash_map:
                j = hash_map[target-val]
                if i != j:
                    return [i, j]


if __name__ == "__main__":
    Solution=Solution()
    print Solution.twosum3([3,2,4],6)
