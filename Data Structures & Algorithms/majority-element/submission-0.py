class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen ={}
        for n in nums:
            seen[n]=seen.get(n,0)+1
        for num, count in seen.items():
            if count> len(nums)//2:
                return num