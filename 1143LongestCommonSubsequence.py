class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
    
    #Save O(m)
    class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0]*(len(text2)+1) for _ in range(2)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[1-i%2][j]=dp[i%2][j-1]+1
                else:
                    dp[1-i%2][j] = max(dp[i%2][j], dp[1-i%2][j-1])
        return dp[1-len(text1)%2][-1]

        
        
