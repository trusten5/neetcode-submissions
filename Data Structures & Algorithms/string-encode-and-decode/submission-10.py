class Solution:
    def encode(self, strs: List[str]) -> str:
        out=""
        for x in strs:
            out = out + str(len(x))+ '#'+x
        # print(out)
        return out

    def decode(self, s: str) -> List[str]:
        letters = s
        result = []
        i = 0
        while i<len(letters):
            j = i
            while letters[j] != '#':
                j+=1
            # print(letters[i:j])
            length = int(letters[i:j])
            i=j+1
            j=i+length
            word = "".join(letters[i:j])
            result.append(word)
            # print(result)
            i=j
        return result