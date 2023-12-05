import collections

class FiltreUltrason:
    def __init__(self):
        self.runningData = collections.deque([100, 100, 100, 100, 100, 100, 100, 100])
        self.dataAmount = 8
        self.offset = 2

    def RunningAverage(self, distance):
        self.runningData.appendleft(distance)
        self.runningData.pop()
        runingAverage = 0
        for x in self.runningData:
            runingAverage += x
        runingAverage /= self.dataAmount
        return runingAverage + self.offset
