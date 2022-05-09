class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        dict={}
        for i in range(n):
            diff=target-nums[i]
            if diff not in dict:
                dict[nums[i]]=i
            else:
                return [i,dict[diff]]
                
                
            
                
                

            
            
        