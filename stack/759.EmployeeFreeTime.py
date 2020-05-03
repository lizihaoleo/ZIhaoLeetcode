"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        ans = []
        h = []
        for intervals in schedule:
            for interval in intervals:
                heapq.heappush(h,[interval.start,interval.end])
        merged = [heapq.heappop(h)]
        while h:
            cur = heapq.heappop(h)
            if cur[0] <= merged[-1][1]:
                # merge if cur.start <= last merged.end
                merged[-1][1] = max(cur[1],merged[-1][1])
            else:
                merged.append(cur)
        # print(merged)
        for i in range(1,len(merged)):
            pre = merged[i-1]
            cur = merged[i]
            ans.append(Interval(pre[1],cur[0]))
        return ans