'''
Problem:

写两个函数 addInterval, getTotalBusyTime。写出两种不同的实现 分析trade off(基本就是根据两个函数的调用频率决定)
(1) LinkedList 插入使得每次插入后start保持有序并保持所有的节点都是disjointed 同时计算totalbusy。 O(N)的add时间和O(1)get时间
(2) Binary search tree. 也就是map，treemap这种。 保持插入后有序，O(logN) add O(N) get时间
follow up 如果需要remove interval 用哪种方式？

第二题是merge interval 那道题。有 add 和getcoverlength 两个method。要求不是以前的那种根据call frequency写而是假定两个method的频率是随机的。
要求达到时间复杂度最佳。。最先用了直接add 到list 然后call get 的时候sort 的方法。然后讨论了很久最后说用treeSet 在add 里面，这样总时间复杂度更小。
选择这个数据结构就是要达到add 和get的时间复杂度都是最优，也就是说在100次操作里面add get出现的几率是一样的。可以按照add 50 get 50 来计算。
现在就要在这样的情况下让总的时间最小。自然treeset就是最好的
'''

'''
Solution 1:
Insert time: O(n)
getTotalLength: O(1)
'''


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class DisjointIntervals(object):
    def __init__(self):
        self.intervals = []
        self.total_length = 0


    def getTotalLength(self):
        return self.total_length


    def insert(self, newInterval):

        ret = []
        self.total_length = 0
        hasInsert = False

        for i in range(len(self.intervals)):
            
            if hasInsert:   
                ret.append(self.intervals[i])
                self.total_length += self.intervals[i].end - self.intervals[i].start
                
            # newInterval before the current interval
            elif newInterval.end < self.intervals[i].start:
                ret.append(newInterval)
                ret.append(self.intervals[i])
                self.total_length += self.intervals[i].end - self.intervals[i].start
                self.total_length += newInterval.end - newInterval.start
                hasInsert = True
                
            # merge 2 intervals
            elif newInterval.start <= self.intervals[i].end and newInterval.end >= self.intervals[i].start:
                newInterval.start = min(newInterval.start,self.intervals[i].start)
                newInterval.end = max(newInterval.end,self.intervals[i].end)
                
            # newInterval after the curent interval
            else:
                self.total_length += self.intervals[i].end - self.intervals[i].start
                ret.append(self.intervals[i])

        if not hasInsert:   
            ret.append(newInterval)
            self.total_length += newInterval.end - newInterval.start

        self.intervals = ret

        
        

# Test cases.
i1 = Interval(1, 4)
i2 = Interval(6, 7)
i3 = Interval(2, 5)
intervals = DisjointIntervals()
intervals.insert(i1)
print intervals.getTotalLength()
intervals.insert(i2)
print intervals.getTotalLength()
intervals.insert(i3)
print intervals.getTotalLength()





'''
Solution 2:
Insert time: O(1)
getTotalLength: O(n)
'''
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class DisjointIntervals(object):
    def __init__(self):
        self.intervals = []


    def insert(self, interval):
        self.intervals.append(interval)


    def getTotalLength(self):

        intervals = self.intervals
        totalLength = 0
        
        if intervals and len(intervals) < 2:
            return intervals[0].end - intervals[0].start

        intervals.sort(key = lambda interval: interval.start)

        cur_item = intervals[0]
        for item in intervals[1:]:
            if item.start <= cur_item.end:
                cur_item.end = max(cur_item.end,item.end)
                intervals.remove(item)
            else:
                totalLength += cur_item.end - cur_item.start
                cur_item = item
        totalLength += cur_item.end - cur_item.start
        self.intervals = intervals
        return totalLength
    

        
        

# Test cases.
i1 = Interval(1, 4)
i2 = Interval(6, 7)
i3 = Interval(2, 5)
intervals = DisjointIntervals()
intervals.insert(i1)
print intervals.getTotalLength()
intervals.insert(i2)
print intervals.getTotalLength()
intervals.insert(i3)
print intervals.getTotalLength()
