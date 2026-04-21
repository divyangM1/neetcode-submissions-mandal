class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = []
        final = 0
        sub = 0
        for i in s:
            if i-1 not in s:
                ans.append(i)
                
            
        j = 0  
        i=0
        while len(ans) != j:
            if ans[j]+i in s:
                sub+=1
                i+=1
                
            else:
                if final > sub:
                    sub = 0
                    j+=1
                    i=0
                    continue
                else:
                    final = sub 
                    sub = 0
                    j+=1
                    i=0
                    continue
        return final