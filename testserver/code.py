
class Point:
    def __init__(self, firstPoint, secondPoint):
        self.firstPoint = firstPoint
        self.secondPoint = secondPoint

    def distance(self):
        return self.firstPoint ** self.firstPoint + self.secondPoint ** self.secondPoint


point = Point(2, 3)
print('Distance is', point.distance())
