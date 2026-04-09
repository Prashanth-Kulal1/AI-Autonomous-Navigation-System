class Agent:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.pos = start

    def move(self, position):
        self.pos = position