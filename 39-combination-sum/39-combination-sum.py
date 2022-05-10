class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final=[]
        n=len(candidates)
        
       # self.func(0,target,[],len(candidates),candidates,final)
        def func(ind,target,arr):
            if target<sum(arr):
                return
            if target==sum(arr):
                print(arr)
                final.append(arr.copy())
                return

            if ind>=n:
                return
            arr.append(candidates[ind])
            func(ind,target,arr)
            arr.remove(candidates[ind])
            func(ind+1,target,arr)
        func(0,target,[])
        return final

    """
    def func(self,ind:int,target:int,arr:List[int],n:int,nums:List[int],final:List[int]):
        if target<sum(arr):
            return
        if target==sum(arr):
            final.append(arr)
            return

        if ind>=n:
            return
        arr.append(nums[ind])
        self.func(ind,target,arr,n,nums,final)
        arr.remove(nums[ind])
        self.func(ind+1,target,arr,n,nums,final)  
"""
 