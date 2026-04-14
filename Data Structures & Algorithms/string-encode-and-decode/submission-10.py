class Solution:

    def encode(self, strs: List[str]) -> str:
        # encoded = ""
        # for i in strs:
        #     encoded += "@#$#@&" + s + 
        if len(strs) == 0:
            return "emptylist"
        return "@#$#@&".join(strs)

    def decode(self, s: str) -> List[str]:

        key = "@#$#@&"
        if s == "emptylist":
            return []
        return s.split(key)



