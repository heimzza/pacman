import queue


class UCS():
    def __init__(self):
        self.place = None
        self.x = None
        self.y = None
        self.target_place = None

    def findCoordinates(self, level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]

                # Check if it is an X (Wall)
                if character == "X":
                    walls.append((x, y))

                # Check if it is a P (Player)
                if character == "P":
                    self.place = (x, y)
                    self.x = x
                    self.y = y

                # Check if it an F (Food)
                if character == "F":
                    self.target_place = (x, y)
        movements.append((self.x, self.y))
        self.findPath(self.x, self.y)
        print("Başlangıç :" + str(self.place))
        print("Hedef :" + str(self.target_place))
        print("Yol :" + str(movements))
        print("UCS Maaliyeti :" + str(len(movements)))

    def findPath(self, x, y):
        if (x, y) == self.target_place:
            movements.append((x, y))
            return len(movements)
        if (x, y + 1) not in walls and (x, y + 1) not in movements:
            queue.put(y + 1)
            queue.put(x)
            movements.append((x, y + 1))
        if (x + 1, y) not in walls and (x + 1, y) not in movements:
            queue.put(y)
            queue.put(x + 1)
            movements.append((x + 1, y))
        if (x, y - 1) not in walls and (x, y - 1) not in movements:
            queue.put(y - 1)
            queue.put(x)
            movements.append((x, y - 1))
        if (x - 1, y) not in walls and (x - 1, y) not in movements:
            queue.put(y)
            queue.put(x - 1)
            movements.append((x - 1, y))
        self.findPath(queue.get(), queue.get())


movements = []
queue = queue.LifoQueue()
walls = []