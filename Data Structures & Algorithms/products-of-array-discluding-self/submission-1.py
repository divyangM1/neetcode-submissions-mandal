class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        n = 1
        for i in range (len(nums)):
            output.append(n)
            n *= nums[i]
        
        n = 1 
        for i in range(len(nums)-1,-1,-1):
            output[i] *= n
            n *= nums[i]

        return output



            

        