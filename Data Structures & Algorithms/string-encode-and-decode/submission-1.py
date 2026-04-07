class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#"+ s
        return string
    def decode(self, string: str) -> List[str]:
        lists = []
        i = 0
        while i < len(string):
            j = i
            while string[j] != "#":
                j += 1
            lenght = int(string[i:j])
            lists.append(string[j+1:j+1+lenght])
            i = j+1+lenght
        return lists
