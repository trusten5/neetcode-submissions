class Solution:

    def encode(self, strs: List[str]) -> str:
        out=''
        for word in strs:
            out=out+str(len(word))+'#'+word
        return out
    def decode(self, s: str) -> List[str]:
        out=[]
        i=0
        j=0
        while i<len(s):
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i=j+1
            j=i+length
            out.append(s[i:j])
            i=j+1
            i=j
        
        return out