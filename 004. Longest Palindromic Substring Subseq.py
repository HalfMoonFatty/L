'''
Problem 1: Longest Palindromic Substring
    Given a string S, find the longest palindromic substring in S. 
    You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''



'''
A simpler approach “expand from every possible center” O(N2) time and O(1) space:
find every possible center and try to expand to left and right and remember the longest palindrome along the way.
'''

class Solution(object):
    def longestPalindrome(self, s):
        def expand(left,right):
            while left >=0  and right <= len(s)-1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
            # note: real right index is: right-1; but we need to +1 to the interval to be inclusive

        longestPali = s[0:1]
        for i in range(len(s)-1):   # note
            odd = expand(i,i)
            even = expand(i,i+1)
            if len(odd) > len(longestPali): longestPali = odd
            if len(even) > len(longestPali): longestPali = even
        return longestPali


    
'''
Problem 2: Longest Palindromic Subsequence
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
Example 1:
Input: "bbbab"
Output: 4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input: "cbbd"
Output: 2
'''

'''
Solution: DP
dp[i][j] = dp[i + 1][j - 1] + 2               if s[i] == s[j]
dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])    otherwise
'''

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0]* n for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
        return dp[0][n-1]
    
