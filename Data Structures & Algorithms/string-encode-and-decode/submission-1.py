class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) > 0:
            enc = strs[0]
            self.pointer = [len(strs[0])]
        else:
            self.pointer = None
            return ""
        for s in strs[1:]:
            enc += s
            self.pointer.append(len(s))
        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        if self.pointer:
            for s_len in self.pointer:
                dec.append(s[:s_len])
                s = s[s_len:]
            return dec
        else:
            return []
