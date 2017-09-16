'''
Problem 1:
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
1. All numbers (including target) will be positive integers.
2. Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
3. The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
'''

class Solution:

    def combinationSum(self, candidates, target):

        def helper(candidates, index, target, res, results):
            if target == 0:
                results.append(res[:])
                return
            elif target < 0:
                return
            
            for i in range(index, len(candidates)):
                res.append(candidates[i])
                helper(candidates, i, target-candidates[i], res, results)   # note: i not i+1
                res.pop()          
            return


        results = []
        candidates = sorted(list(set(candidates)))  # note
        helper(candidates, 0, target, [], results)
        return results


'''
Problem 2:
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used ONCE in the combination.
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
'''

class Solution(object):
    def combinationSum2(self, candidates, target):

        def helper(candidates, index, target, res, result):
            if target == 0:
                result.append(res[:])
                return
            elif target < 0:
                return
            
            for i in range(index, len(candidates)):
                if i == index or candidates[i] != candidates[i-1]:   # remove duplicate
                    res.append(candidates[i])
                    helper(candidates, i+1, target-candidates[i], res, result)
                    res.pop()
            return


        result = []
        candidates.sort()  
        helper(candidates, 0, target, [], result)
        return result




'''
Problem 3:
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
Ensure that numbers within the set are sorted in ascending order.
Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
            :type k: int
            :type n: int
            :rtype: List[List[int]]
            """
        def helper(nums, s, k, n, res, result):
            if k == 0 and n == 0:
                result.append(res[:])
                return
            if n < 0 or k <= 0:
                return
            for i in range(s,len(nums)):
                res.append(nums[i])
                helper(nums,i+1,k-1,n-nums[i],res,result)
                res.pop()
            return


        result = []
        nums = [i for i in range(1,10)]
        helper(nums,0,k,n,[],result)
        return result
        
        

'''
Problem 4:
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
Example:
nums = [1, 2, 3]
target = 4
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations. Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
'''

'''
Solution: 1 demension DP solution
Time: o(n*m)
Space: O(n)
'''

class Solution(object):
    def combinationSum4(self, nums, target):

        nums.sort()
        res = [0] * (target + 1)
        res[0] = 1
        for i in range(1,target+1):
            for n in nums:
                if n <= i:
                    res[i] += res[i-n]

        return res[target]    
        
        
        
'''
Problem 5:
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
For example,
If n = 4 and k = 2, a solution is:
[
[2,4],
[3,4],
[2,3],
[1,2],
[1,3],
[1,4],
]
'''


class Solution(object):

    def combine(self, n, k):

        def helper(n,index,res,result):
            if len(res) == k:
                result.append(res[:])
                return
            for i in range(index,n):
                res.append(i+1)
                helper(n,i+1,res,result)
                res.pop()
            return

        result = []
        helper(n,0,[],result)
        return result
