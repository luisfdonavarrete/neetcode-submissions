class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}*{s}"
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        while len(s) > 0:
            limiter = s.find('*')
            length = int(s[0:limiter])
            start = limiter + 1
            stop = start + length
            res.append(s[start:stop])
            print(length)
            s = s[stop:]
        return res
