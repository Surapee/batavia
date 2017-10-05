
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return self.x ** self.x + self.y ** self.y


point = Point(x, y)
print('Distance is', point.distance())
