class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        seen={}
        if len(pattern) != len(words):
            return False
        else:
            for l in range(len(pattern)):
                print(pattern[l], words[l])
                if pattern[l] in seen:
                    if seen[pattern[l]] != words[l]:
                        return False
                else:
                    seen[pattern[l]]=words[l]
        
        seens=[]
        for keys, vals in seen.items():
            if vals in seens:
                return False
            seens.append(vals)
        
        return True
