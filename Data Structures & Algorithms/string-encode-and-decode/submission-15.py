class Solution:

    def encode(self, strs: List[str]) -> str:
        out=''
        for s in strs:
            out=out+str(len(s))+'#'+s
        print(out)
        return out
    def decode(self, s: str) -> List[str]:
        out=[]
        i=0
        j=0

        while i < len(s):
            while s[j] != '#':
                j+=1

            length = int(s[i:j])

            i=j+1
            j=i+length

            word = s[i:j]
            out.append(word)
            
            i=j

        return out