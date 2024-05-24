import heapq

class PuzzleState:
    def __init__(self, board, goal, moves=0, previous=None):
        self.board = board
        self.goal = goal
        self.moves = moves
        self.previous = previous
        self.blank_pos = self.board.index(0)

    def __lt__(self, other):
        return self.estimated_cost() < other.estimated_cost()

    def is_goal(self):
        return self.board == self.goal

    def estimated_cost(self):
        return self.moves + self.manhattan_distance()

    def manhattan_distance(self):
        distance = 0
        for i in range(1, 9):
            current_pos = self.board.index(i)
            goal_pos = self.goal.index(i)
            current_row, current_col = divmod(current_pos,3)
            goal_row, goal_col = divmod(goal_pos, 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

    def neighbors(self):
        neighbor_boards = []
        blank_row, blank_col = divmod(self.blank_pos, 3)
        for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_row, neighbor_col = blank_row + delta_row, blank_col + delta_col
            if 0 <= neighbor_row < 3 and 0 <= neighbor_col < 3:
                neighbor_pos = neighbor_row * 3 + neighbor_col
                new_board = self.board[:]
                new_board[self.blank_pos], new_board[neighbor_pos] = new_board[neighbor_pos], new_board[self.blank_pos]
                neighbor_boards.append(PuzzleState(new_board, self.goal, self.moves + 1, self))
        return neighbor_boards

def a_star_search(initial, goal):
    open_set = []
    closed_set = set()
    initial_state = PuzzleState(initial, goal)
    heapq.heappush(open_set, initial_state)

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal():
            return reconstruct_path(current_state)

        closed_set.add(tuple(current_state.board))

        for neighbor in current_state.neighbors():
            if tuple(neighbor.board) in closed_set:
                continue
            heapq.heappush(open_set, neighbor)

    return None

def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.previous
    path.reverse()
    return path

def print_path(path):
    for step in path:
        for i in range(0, len(step), 3):
            print(step[i:i+3])
        print()

# Example usage:
initial_board = [1, 2, 3, 4, 5, 6, 7, 0, 8]
goal_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]

path = a_star_search(initial_board, goal_board)
print("Solution path:")
print_path(path)


	