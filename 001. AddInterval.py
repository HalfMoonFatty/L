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
