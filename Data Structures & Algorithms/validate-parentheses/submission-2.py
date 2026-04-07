class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        mapping = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c not in mapping:
                l.append(c)
            else:
                if not l:
                    return False
                else:
                    s = l.pop()
                    if s != mapping[c]:
                        return False
        return not l


        