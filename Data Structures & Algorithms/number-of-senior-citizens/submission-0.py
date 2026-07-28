class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter=0

        for d in details:
            age = int(d[11:13])
            if age > 60:
                counter+=1
        
        return counter