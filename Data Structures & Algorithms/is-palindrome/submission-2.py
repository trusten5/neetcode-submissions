class Solution:
    def isPalindrome(self, s: str) -> bool:


        ct = "".join(char for char in s if char.isalnum())
        letters=list(ct.lower())
        back = len(list(letters))-1
        front=0
        print(letters)

        while front<back:
            if letters[front] != letters[back]:
                return False
            front+=1
            back-=1

        return True