class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}|{s}"
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        chars = ""
        i = 0 
        while i < len(s):
            if s[i] == '|':
                stop = i + int(chars) + 1
                res.append(s[i + 1:stop])
                i = stop
                chars = ""
            else:
                chars += s[i]
                i = 1 + i

        return res
