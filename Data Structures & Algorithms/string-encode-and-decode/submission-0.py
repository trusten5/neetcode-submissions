class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for x in strs:
            output.append(str(len(x)))
            output.append('#')
            output.append(x)

        return ''.join(output)
        
        

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                length = int(s[:i])
                string_val = s[i+1:i+1+length]
                output.append(string_val)
                s = s[i+1+length:]
                i = 0
            else:
                i += 1
            

        return output
