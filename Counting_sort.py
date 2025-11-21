class Solution:
    def countSort(self,s):
        # code here
        freq = [0] * 26
        
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        result = []
        for i in range(26):
            result.append(chr(i + ord('a')) * freq[i])
        return "".join(result)    
