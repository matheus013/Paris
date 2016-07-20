from Constants import Constant

class Node:
    cost = 0
    parent = 0
    line = "white"
    state = 0
    SPEED = 30

    def __init__(self, cost, parent, state, line):
        self.cost = cost
        self.parent = parent
        self.state = state
        self.line = line

    def f(self, goal):
        return self.cost + Constant.cost_mtz[self.state][self.parent.state]

    def __str__(self):
        return self.state

    def __lt__(self, other):
        return self.f() < other.f()

    def __ne__(self, other):
        return self.state != other.state

    def __eq__(self, other):
        return self.state == other.state

    def finale(self, goal):
        return self.state == goal