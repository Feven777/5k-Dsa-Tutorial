class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        i=0
        j=len(x)-1
        while i<j:
            if x[i]==x[j]:
                i+=1
                j-=1
            else:
                return False
        return True
