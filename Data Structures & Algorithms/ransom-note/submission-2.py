class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen={}
        seen1={}

        for n in ransomNote:
            if n not in seen:
                seen[n]=1
            else:
                seen[n]+=1

        for n in magazine:
            if n in seen1:
                seen1[n]+=1
            else:
                seen1[n]=1
            
        for keys, vals in seen.items():
            if keys not in seen1 or seen1[keys]<vals:
                return False

        return True


        