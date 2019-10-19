from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heappush(self.small, -heappushpop(self.large, num))
        if len(self.small)>len(self.large):
            heappush(self.large, -heappop(self.small))
        # if len(self.small)==len(self.large):
        #     heappush(self.large, -heappushpop(self.small, -num))
        # else:
        #     heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            return (-self.small[0] +self.large[0] )/2
        else:
            return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
