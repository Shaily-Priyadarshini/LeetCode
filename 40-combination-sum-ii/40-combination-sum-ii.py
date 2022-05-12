class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def func(ind, target, arr, final, candidates):
            if target ==0:
                final.append(arr.copy())
                return
            for i in range(ind, n):
                if (i > ind) and (candidates[i] == candidates[i - 1]):
                    continue
                if target < candidates[i]:
                    break

                arr.append(candidates[i])
                func(i + 1, target - candidates[i], arr, final, candidates)
                arr.pop()
        candidates.sort()
        n=len(candidates)
        final=[]
        func(0, target, [],final, candidates)

        return final