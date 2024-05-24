import math

def alBe(node, depth,alpha,beta,maximizingPlayer):
    if depth == 0 or node.is_terminal():
        return node.move, node.evaluate()

    if maximizingPlayer:
        value = -math.inf
        best_move = None
        for child in node.get_children():
            _, child_value = alBe(child, depth - 1,alpha,beta ,False)
            if child_value > value:
                value = child_value
                best_move = child.move
            alpha=max(alpha,value)
            if alpha >= beta:
              break

        return best_move, value
    else:
        value = math.inf
        best_move = None
        for child in node.get_children():
            _, child_value = alBe(child, depth - 1,alpha,beta, True)
            if child_value < value:
                value = child_value
                best_move = child.move
            beta=min(beta,value)
            if alpha >= beta:
              break
        return best_move, value

class Node:
    def __init__(self, value, move=None):
        self.value = value
        self.move = move
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def is_terminal(self):
        return len(self.children) == 0

    def evaluate(self):
        return self.value

# Example usage
root = Node(None)
a = Node(5, 'a')
b = Node(4, 'b')
c = Node(8, 'c')
d = Node(6, 'd')
e = Node(2, 'e')
f = Node(3, 'f')
g = Node(1, 'g')

root.add_child(a)
root.add_child(b)
root.add_child(c)

a.add_child(d)
b.add_child(e)
c.add_child(f)
c.add_child(g)

best_move, best_value = alBe(root, 1, -math.inf, math.inf, True)
print('best move:', best_move, 'with value:', best_value)
