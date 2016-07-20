from Node import Node
from Constants import Constant
import copy

priority = []


def color(a, b):
    for i in Constant.lines:
        if a + 1 in Constant.lines[i] and b + 1 in Constant.lines[i]:
            return i
    return "white"


def start_color(a):
    for i in Constant.lines:
        if a in Constant.lines[i]:
            return i
    return "white"


def expand(actual, line):
    for i in range(0, 14):
        if Constant.adj_mtz[actual.state][i] == 1:
            aux = Node((actual.cost + Constant.cost_mtz[actual.state][i]), copy.deepcopy(actual), i, color(i,
                                                                                                           actual.state))
            if aux.line != line:
                aux.cost += 4
            priority.append(aux)
            priority.sort()
            # print str(i) + " -> " + str(aux.state) + " " + str(aux.cost)


def star(start, end):
    priority.append(start)
    while priority.__len__() > 0:
        next_node = priority.pop(0)
        if next_node.finale(end):
            return next_node
        expand(next_node, next_node.line)


if __name__ == '__main__':
    rote = []
    a = int(raw_input("MATCH: "))
    b = int(raw_input("GOAL: "))
    result = star(Node(0, Node, a - 1, start_color(a)), b - 1)
    print "TOTAL COST: " + str(result.cost)

    while result.state != 0:
        rote.append(result.state + 1)
        result = result.parent
    if a == 1:
        rote.append(1)
    rote.reverse()
    print rote
    for i in rote:
        print i
