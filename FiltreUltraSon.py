import collections

class FiltreUltrason:
    def __init__(self, distance):
        self.runningData = collections.deque([distance, distance, distance, distance, distance])
        self.dataAmount = 5

    def RunningAverage(self, distance):
        self.runningData.appendleft(distance)
        self.runningData.pop()
        runingAverage = 0
        for x in self.runningData:
            runingAverage += x
        runingAverage /= self.dataAmount
        return runingAverage
