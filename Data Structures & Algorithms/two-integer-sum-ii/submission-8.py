class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i,j = 0,1

        while i < j:
            print(i,j)
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]

            if j == len(numbers)-1:
                i+=1
                j=i

            j+=1




