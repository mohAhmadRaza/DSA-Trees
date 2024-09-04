class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])
            
        common = list(words[0])
        for i in range(1, len(words)):
            curr = Counter(words[i])
            newCommon  =[]
            for i in common:
                if curr[i] > 0:
                    newCommon.append(i)
                    curr[i] -= 1
            
            common = newCommon
        
        return common

        
