'''
Problem 1: Number of Palindrom Substring

Given a string, the task is to count all palindrome substring in a given string. 
Length of palindrome substring is greater then or equal to 2.

Examples:
Input : str = "abaab"
Output: 3
Explanation : All palindrome substring are : "aba" , "aa" , "baab" 
Input : str = "abbaeae"
Output: 4
Explanation : All palindrome substring are : "bb" , "abba" ,"aea","eae"
'''

def countPS(s):

    n = len(s)
    isPal = [[False] * (n+1) for _ in range(n+1)]
    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(i-1,-1,-1):
            if s[j-1] == s[i-1] and (i-j<=2 or isPal[j+1][i-1]):
                isPal[j][i] = True
            if isPal[j][i]: 
                dp[j][i] = dp[j][i-1] + dp[j+1][i] - dp[j+1][i-1] + 1
            else:
                dp[j][i] = dp[j][i-1] + dp[j+1][i] - dp[j+1][i-1]
    return dp[0][n-1]



print countPS("abaab")
print countPS("abbaeae")




'''
Problem 2: Number of Palindrom Subsequence
'''

def countPS(s):

    n = len(s)
    isPal = [[False] * (n+1) for _ in range(n+1)]
    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(i-1,-1,-1):
            if s[j-1] == s[i-1]:
                dp[j][i] = dp[j][i-1] + dp[j+1][i] + 1
            else:
                dp[j][i] = dp[j][i-1] + dp[j+1][i] - dp[j+1][i-1]
    return dp[0][n-1]



print countPS("abaab")
print countPS("abbaeae")

