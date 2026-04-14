class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # system ={}
        # for i in range (len(strs)):
        #     if "".join(sorted(strs[i])) not in system:
        #         system["".join(sorted(strs[i]))] = [strs[i]]

        #     else:
        #         system["".join(sorted(strs[i]))].append(strs[i])

        # output = []
        # for i,j in system.items():
        #     output.append(j)

        # return output

        system = {}

        for s in strs:


            count = [0] * 26

            for i in s:
                count[ord(i) - ord('a')] +=1


            key = tuple(count)

            if key not in system:
                system[key] = [s]
            else:
                system[key].append(s)


        return list(system.values())
        