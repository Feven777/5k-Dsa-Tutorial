class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix=[]
        mini= float('inf')
        for word in strs:
            if len(word)<mini:
                mini=len(word)
        for i in range(mini):
            temp=strs[0][i]
            for word in strs:
                if word[i]!=temp:
                    return "".join(common_prefix)
            else:
                common_prefix.append(word[i])
        return strs[0][:mini]
