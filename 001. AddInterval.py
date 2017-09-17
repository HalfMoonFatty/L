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


class Intervals(object):
    def __init__(self):
        self.intervals = []
        self.total_length = 0


    def Insert(self, new_interval):
        def IsOverlap(i1, i2):
            if i1.start >= i2.start:
                i1,i2 = i2,i1
            return i1.end >= i2.start and i1.start <= i2.end
        
        def Merge(i1, i2):
            return Interval(min(i1.start, i2.start), max(i1.end, i2.end))

        intervals_to_remove = []
        for i in range(len(self.intervals)):
            if not IsOverlap(self.intervals[i], new_interval):
                continue
            new_interval = Merge(self.intervals[i], new_interval)
            intervals_to_remove.append(i)

        # update total_length
        for i in intervals_to_remove:
            self.total_length -= self.intervals[i].end - self.intervals[i].start
        self.total_length += new_interval.end - new_interval.start


        if intervals_to_remove:
            start, end = intervals_to_remove[0], intervals_to_remove[-1]
            end_intervals = (self.intervals[end + 1:] if end + 1 < len(self.intervals) else [])
            self.intervals = (self.intervals[:start] + [new_interval] + end_intervals)
        else:
            self.intervals.append(new_interval)


    def GetTotalLength(self):
        return self.total_length


# Test cases.
i1 = Interval(1, 4)
i2 = Interval(6, 7)
i3 = Interval(2, 5)
intervals = Intervals()
intervals.Insert(i1)
intervals.Insert(i2)
print intervals.GetTotalLength()
intervals.Insert(i3)
print intervals.GetTotalLength()




'''
Solution 2:
Insert time: O(1)
getTotalLength: O(n)
'''

