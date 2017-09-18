# Motivated from:
# https://github.com/HalfMoonFatty/Interview-Questions/blob/master/072.%20Edit%20Distance.py
def minDistance(word1, word2):
    m = len(word1)
    n = len(word2)

    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(0,m+1):
        dp[i][0] = i
    for j in range(0,n+1):
        dp[0][j] = j

    for i in range(1,m+1):
        for j in range(1,n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
    return dp[m][n]

# Motivated from:
# https://stackoverflow.com/questions/4737791/how-to-convert-a-string-into-a-palindrome-with-minimum-number-of-operations
def minDistancePalendrome(word):
    opt = len(word)

    for pivot in range(len(word)):
        # Split at char.
        left, right = word[:pivot], word[pivot + 1:]
        opt = min(opt, minDistance(left, right[::-1]))

        # Split between chars.
        left, right = word[:pivot], word[pivot:]
        opt = min(opt, minDistance(left, right[::-1]))

    return opt

# Tests.
print minDistancePalendrome('tanbirahmed')
print minDistancePalendrome('shahriarmanzoor')
print minDistancePalendrome('monirulhasan')
print minDistancePalendrome('syedmonowarhossain')
print minDistancePalendrome('sadrulhabibchowdhury')
print minDistancePalendrome('mohammadsajjadhossain')

