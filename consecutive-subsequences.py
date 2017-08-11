# https://www.hackerrank.com/contests/w6/challenges/consecutive-subsequences
import sys

def GetCount(vec, k):
    # Initialize count array.
    cnt_mod = [0] * k
    cnt_mod[0] = 1
    pref_sum = 0
    # Iterate over input sequence.
    for elem in vec:
        pref_sum += elem
        pref_sum %= k
        cnt_mod[pref_sum] += 1
    # Compute the answer.
    res = 0
    for mod in range(k):
        res += cnt_mod[mod] * (cnt_mod[mod] - 1) / 2
    return res

num_tests = int(raw_input().strip())
for _ in xrange(num_tests):
    n, k = [int(elem) for elem in raw_input().strip().split(' ')]
    arr = [int(elem) for elem in raw_input().strip().split(' ')]
    print GetCount(arr, k)
