class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        system = {}

        for i in nums:
            if i not in system:
                system[i] = 1
            else:
                system[i]+=1

        output = []

        return sorted(system, key=system.get, reverse = True)[:k]

        