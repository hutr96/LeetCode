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


    def twosum2(self,nums,target): #Pass
        for i, num in enumerate(nums):
            try:
                j = nums.index(target-num)
                if j != i:
                    return [i,j]
                else:
                    continue
            except ValueError:
                continue




if __name__ == "__main__":
    Solution=Solution()
    print Solution.twosum2([3,2,4],6)
