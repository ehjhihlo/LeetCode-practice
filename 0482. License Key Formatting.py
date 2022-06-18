class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        new_str = s.upper().replace('-','')
        first = len(new_str) % k
        res = []
        if first > 0:
            res.append(new_str[:first])
        i = first
        while i < len(new_str):
            res.append(new_str[i:i+k])
            i += k
        result = '-'.join(res)
        return result
