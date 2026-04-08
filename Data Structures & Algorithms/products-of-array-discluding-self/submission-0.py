class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[0]*len(nums)
        for i in range(0,len(nums)):
            prod=1
            for j in range(0,len(nums)):
                if (i!=j):
                    prod*=nums[j]
            print(i)
            output[i]=prod
        return output