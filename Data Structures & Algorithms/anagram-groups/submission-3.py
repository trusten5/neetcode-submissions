class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        stored_comb = {}

        for x in strs:
            characters = [0] * 26
            for pos in range(len(x)):
                characters[ord(x[pos]) - ord('a')] += 1

            characters = tuple(characters)

            if characters not in stored_comb:
                stored_comb[characters] = []
                stored_comb[characters].append(x)
            else:
                stored_comb[characters].append(x)
        
        answer = list(stored_comb.values())

        return answer