class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

    # def neighbors(self, state):
    #     row, col = state
    #     candidates = [
    #         ("up", (row - 1, col)),
    #         ("down", (row + 1, col)),
    #         ("left", (row, col - 1)),
    #         ("right", (row, col + 1))
    #     ]
    #
    #     result = []
    #     for action, (r, c) in candidates:
    #         if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
    #             result.append((action, (r, c)))
    #     return result
