class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        system ={}
        for i in range (len(strs)):
            if "".join(sorted(strs[i])) not in system:
                system["".join(sorted(strs[i]))] = [strs[i]]

            else:
                system["".join(sorted(strs[i]))].append(strs[i])

        output = []
        for i,j in system.items():
            output.append(j)

        return output

        