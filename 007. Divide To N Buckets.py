'''
Problem:

Given number array and k, see if array could be divided to k buckets which all have same sum. 
'''


def divideNBucket1(nums, n):
    """
    :type nums: List[int]
    :rtype: bool
    """
    def canDivide(nums, index, buckets, target):
        if index == len(nums): 
            for i in range(len(buckets)):
                if buckets[i] != target:
                    return False
            return True
        else:
            for i in range(n):
                if buckets[i] + nums[index] > target: continue
                buckets[i] += nums[index]
                if canDivide(nums, index+1, buckets, target):
                    return True
                buckets[i] -= nums[index]
        return False
    
    
    if not nums or len(nums) < n or sum(nums)%n != 0:
        return False
    
    #nums.sort(reverse=True)
    buckets = [0]*n
    return canDivide(nums, 0, buckets, sum(nums)/n)



def divideNBucket2(nums, n):
    """
    :type nums: List[int]
    :rtype: bool
    """
    def isValid(buckets, target):
        for i in range(len(buckets)):
            if sum(buckets[i]) != target:
                return False
        return True

    def canDivide(nums, index, buckets, target, result):
        if index == len(nums): 
            if len(result) == 0 and isValid(buckets,target):
                result.append([b[:] for b in buckets])
            return result
        else:
            for i in range(n):
                if sum(buckets[i]) + nums[index] > target: continue
                buckets[i].append(nums[index])
                canDivide(nums, index+1, buckets, target, result)
                buckets[i].pop()

    
    
    if not nums or len(nums) < n or sum(nums)%n != 0:
        return False
    
    #nums.sort(reverse=True)
    buckets = [[0]*n for _ in range(n)]
    result = []
    canDivide(nums, 0, buckets, sum(nums)/n, result)
    return result



nums = [1,2,3,4,5]
n = 3
print divideNBucket1(nums, n)
print divideNBucket2(nums, n)


