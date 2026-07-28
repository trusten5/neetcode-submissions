class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        seen={}
        store = set()
        if len(pattern) != len(words):
            return False
        for l in range(len(pattern)):
            if pattern[l] in seen:
                if seen[pattern[l]] != words[l]:
                    return False
            else:
                if words[l] in store:
                    return False
                seen[pattern[l]]=words[l]
                store.add(words[l])
        
        
        return True
