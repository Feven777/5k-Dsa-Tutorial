import string 
class Solution:
    def freqAlphabets(self, s: str) -> str:
        letters=list(string.ascii_lowercase)
        ans = []
        i = len(s)-1
        while i >= 0:
            if s[i] == "#":
                ans.append(letters[int(s[i-2: i]) - 1])
                i -= 3
            else:
                ans.append(letters[int(s[i])-1])
                i -= 1
        ans.reverse()
        return ''.join(ans)
