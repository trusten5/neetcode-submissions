class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count=len(words)
        for w in words:
            print(w)
            for l in w:
                print(l, l not in allowed)
                if l not in allowed:
                    count-=1
                    break
                print(count)

        return count