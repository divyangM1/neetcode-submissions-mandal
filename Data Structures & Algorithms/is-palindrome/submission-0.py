class Solution:
    def isPalindrome(self, s: str) -> bool:

        p = []

        for i in s:
            if i.isalnum():
                p.append(i.lower())
        
        i,j = 0, len(p)-1


        while i <= j:
            if p[i] == p[j]:
                print(p[i],p[j])
                i+=1
                j-=1

            else:
                return False

        else:
            return True

        