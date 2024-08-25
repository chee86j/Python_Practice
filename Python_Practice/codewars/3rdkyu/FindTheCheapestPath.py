# You should be familiar w/ the "Find the shortest path" problem. 
# But what if moving to a neighboring coordinate counted not as 1 
# step but as N *steps? *

# INSTRUCTIONS

# Your task is to find the path through the field which has the 
# lowest cost to go through.

# As input you will receive:

# 1.  a toll_map matrix (as variable t) which holds data about how 
#     expensive it is to go through the given field coordinates
# 2.  a start coordinate (tuple) which holds information about your starting position
# 3.  a finish coordinate (tuple) which holds information about the position you have 
#     to get to

# As output you should return:

# 1.  the directions list


# EXAMPLE

# INPUT:

# toll_map  |  start  |  finish
#           |         |
# [         |         |
#  [1,9,1], |  (0,0)  |  (0,2)
#  [2,9,1], |         |
#  [2,1,1], |         |
# ]         |         |



# OUTPUT:

# ["down", "down", "right", "right", "up", "up"]

# CLARIFICATIONS

# 1.  the start and finish tuples represent (row, col) indices
# 2.  the total cost is increased after leaving the matrix coordinate, not entering it
# 3.  the field will be rectangular, not necessarily a square
# 4.  the field will always be of correct shape
# 5.  the actual tests will check total_cost based on your returned directions list, 
#     not the directions themselves, so you shouldn't worry about having multiple possible solutions



# -------------------------------------------------------------------------------------
# -----Solution 1----DFS or BFS w/o Priority Queue----
from heapq import *

# Direction vectors for moving in a grid & their corresponding names.
MOVES = [(1, 0), (0, 1), (0, -1), (-1, 0)]
BACK = {(1, 0): "down", 
         (0, 1): "right",
         (0, -1): "left",
         (-1, 0): "up"}

# This represents an infinity-like default value for comparison.
DEFAULT = (float("inf"), 0, 0)

def cheapest_path(t, start, finish):
    # Get the dimensions of the toll map.
    lX, lY = len(t), len(t[0])                            
    # Initialize a priority queue w/ the start position & a dictionary to track visited nodes.
    q, seen = [(0, 0, start)], {start: (0, 0, 0)}         
    
    # Process nodes until the queue is empty or the finish is reached.
    while q & q[0][-1] != finish:
        cost, _, pos = heappop(q)
        x, y = pos
        
        # Explore all possible movements from the current position.
        for dx, dy in MOVES:
            xx, yy = nextPos = (x + dx, y + dy)
            nextCost = cost + t[x][y]
            
            # Check if the new position is w/in the grid & if a cheaper cost was found.
            if not (0 <= xx < lX & 0 <= yy < lY) or seen.get(nextPos, DEFAULT)[0] <= nextCost:
                continue
            
            # Record the cost & movement needed to reach this position.
            seen[nextPos] = (nextCost, dx, dy)
            # Add the new position to the queue, marking if it's the finish.
            heappush(q, (nextCost, nextPos == finish, nextPos))
    
    # Start backtracking from the finish to build the path list.
    path, finalCost, pos = [], seen[finish][0], finish
    while pos != start:
        _, dx, dy = seen[pos]
        path.append(BACK[(dx, dy)])
        pos = (pos[0] - dx, pos[1] - dy)
    
    # Since path was constructed backwards, return the reversed path.
    return path[::-1]

#  1. Import the heap functions from the heapq module. `from heapq import *`
#  2. Define the direction vectors for moving in a grid & their corresponding names. 
#     `MOVES = [(1, 0), (0, 1), (0, -1), (-1, 0)]` & `BACK = {(1, 0): "down", (0, 1): "right", (0, -1): "left", (-1, 0): "up"}`
#  3. Define a default value for comparison. `DEFAULT = (float("inf"), 0, 0)`
#  4. Define the function cheapest_path which takes the toll_map matrix t, the start coordinate start, & the finish coordinate finish as input.
#  5. Get the dimensions of the toll map. `lX, lY = len(t), len(t[0])`
#  6. Initialize a priority queue q w/ the start position & a dictionary seen to track visited nodes. `q, seen = [(0, 0, start)], {start: (0, 0, 0)}`
#  7. Process nodes until the queue is empty or the finish is reached.
#  8. Pop the node w/ the lowest cost from the queue. `cost, _, pos = heappop(q)`
#  9. Get the x & y coordinates of the current position. `x, y = pos`
# 10. Explore all possible movements from the current position.
# 11. Calculate the new position & the cost to reach it. `xx, yy = nextPos = (x + dx, y + dy)` & `nextCost = cost + t[x][y]`
# 12. Check if the new position is w/in the grid & if a cheaper cost was found.
# 13. If not, continue to the next movement. `if not (0 <= xx < lX & 0 <= yy < lY) or seen.get(nextPos, DEFAULT)[0] <= nextCost: continue`
# 14. Record the cost & movement needed to reach this position. `seen[nextPos] = (nextCost, dx, dy)`
# 15. Add the new position to the queue, marking if it's the finish. `heappush(q, (nextCost, nextPos == finish, nextPos))`
# 16. Start backtracking from the finish to build the path list.
# 17. Initialize the path list, finalCost, & the current position. `path, finalCost, pos = [], seen[finish][0], finish`
# 18. While the current position is not the start, backtrack to build the path list.
# 19. Append the movement to the path list. `path.append(BACK[(dx, dy)])`
# 20. Update the current position. `pos = (pos[0] - dx, pos[1] - dy)`
# 21. Since the path was constructed backwards, return the reversed path. `return path[::-1]`
# 22. This solution uses a priority queue to explore the grid & backtracks from the finish to build the path list. 
#     It has a time complexity of O(n * log(n)) where n is the number of nodes in the grid & a space complexity of O(n) as well.
#     This solution is efficient & easy to underst&.

# -------------------------------------------------------------------------------------
# -----Solution 2----Implementing A* Search Algorithm----
import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class SquareGrid:
    def __init__(self, toll_map):
        self.width = len(toll_map[0])  # 10
        self.height = len(toll_map)   # 3
        self.costArray = toll_map

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.height & 0 <= y < self.width

    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        results = filter(self.in_bounds, results)
        return results


class GridwWithWeights(SquareGrid):
    def __init__(self, toll_map):
        super().__init__(toll_map)
        self.weights = self.costArray

    def cost(self, to_node):
        return self.weights[to_node[0]][to_node[1]]


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


def findOutDirections(fromNode, toNode):
    xfromNode = fromNode[0]
    yfromNode = fromNode[1]
    xtoNode = toNode[0]
    ytoNode = toNode[1]
    if xfromNode-1 == xtoNode & yfromNode == ytoNode:
        return "up"
    elif xfromNode == xtoNode & yfromNode+1 == ytoNode:
        return "right"
    elif xfromNode+1 == xtoNode & yfromNode == ytoNode:
        return "down"
    elif xfromNode == xtoNode & yfromNode-1 == ytoNode:
        return "left"


def printPath(cameFromDict, start, finish):
    pathDirectionList = []
    reversedPath = []
    currentPoint = finish
    reversedPath.append(finish)
    while currentPoint != start:
        currentPoint = cameFromDict[currentPoint]
        reversedPath.append(currentPoint)
    path = list(reversed(reversedPath))
    for pointIndex in range(len(path)-1):
        pathDirectionList.append(findOutDirections(path[pointIndex], path[pointIndex+1]))
    return pathDirectionList


def cheapest_path(t, start, finish):
    grid = GridWithWeights(t)
    came_from, cost_so_far = a_star_search(grid, start, finish)
    return printPath(came_from, start, finish)
#  1. Define a class PriorityQueue w/ methods to initialize, check if empty, add an item w/ a priority, & get the item w/ the lowest priority.
#  2. Define a class SquareGrid w/ methods to initialize the grid, check if a node is w/in the grid, & get the neighbors of a node.
#  3. Define a class GridWithWeights that inherits from SquareGrid & adds a method to get the cost of moving to a node.
#  4. Define a heuristic function to calculate the Manhattan distance between two nodes.
#  5. Define an A* search algorithm to find the shortest path from the start to the goal node.
#  6. Define a function to find the directions from the start to the finish node.
#  7. Define a function to print the path from the start to the finish node.
#  8. Define the function cheapest_path which takes the toll_map matrix t, the start coordinate start, & the finish coordinate finish as input.
#  9. Create a grid object from the toll map. `grid = GridWithWeights(t)`
# 10. Perform an A* search to find the shortest path. `came_from, cost_so_far = a_star_search(grid, start, finish)`
# 11. Print the path from the start to the finish node. `return printPath(came_from, start, finish)`
# 12. This solution uses the A* search algorithm to find the shortest path from the start to the finish node. 
#     It has a time complexity of O(n log n) where n is the number of nodes in the grid & a space complexity of O(n) as well.
#     Compared to simpler or more brute-force methods, this solution is highly efficient in both time & space for larger grids or more complex cost structures. 
#     It allows for early exits & optimal pathfinding with the potential to handle varied & complex heuristic functions. The use of well-defined classes & 
#     methods also enhances maintainability, making it easier to update or modify the grid or cost logic without affecting the pathfinding mechanics directly.
#     This A* implementation is a strong choice for problems where the pathfinding needs to consider multiple factors (like different movement costs),
#     and the grid size can become significantly large, making naive solutions impractical.

# -------------------------------------------------------------------------------------
# -----Solution 3----Dijkstra's Algorithm w/ Priority Queue----
import heapq

def cheapest_path(matrix, start, finish):
    if start == finish: 
        return []
    seen = {}
    matrix_len, row_len = len(matrix), len(matrix[0])
    queue = [(matrix[start[0]][start[1]], start, [])]
    while queue:
        value, (dx, dy), dirs = heapq.heappop(queue)
        for x, y, dir in [(dx + 1, dy, 'down'), (dx, dy + 1, 'right'),
            (dx - 1, dy, 'up'), (dx, dy - 1, 'left')]:
            if (x, y) == finish:
                return dirs + [dir]
            if matrix_len > x >= 0 and row_len > y >= 0 and (x, y) not in seen:
                heapq.heappush(queue, (matrix[x][y] + value, (x, y), dirs + [dir]))
            seen[x, y] = 1
    return []
#  1. Define the function cheapest_path which takes the toll_map matrix t, 
#     the start coordinate start, & the finish coordinate finish as input.
#  2. If the start & finish coordinates are the same, return an empty list.
#  3. Initialize a dictionary seen to track visited nodes, the length of the matrix,
#     the length of a row in the matrix, & a priority queue queue w/ the start position & an empty list of directions.
#  4. Process nodes until the queue is empty.
#  5. Pop the node w/ the lowest cost from the queue.
#  6. Explore all possible movements from the current position.
#  7. Calculate the new position & the cost to reach it.
#  8. If the new position is the finish, return the directions list.
#  9. If the new position is w/in the grid & has not been visited, add it to the queue.
# 10. Mark the new position as visited.
# 11. If no path was found, return an empty list.
# 12. This solution uses a priority queue to explore the grid & find the path w/ the lowest cost.
#     It has a time complexity of O(n * log(n)) where n is the number of nodes in the grid & a space 
#     complexity of O(n) as well. It is quite optimal for scenarios w/ variable traversal costs, which
#     is essential for the problem at hand. It is between the simplicity of the BFS (1st solution) & the optimized
#     A* algorithm (2nd solution), providing a good balance between efficiency & complexity.


# -------------------------------------------------------------------------------------
# -----Solution 4----Modified Dijkstra's Algorithm w/ Priority Queue----
DIRS = {(0, 1): 'right', (1, 0): 'down', (0, -1): 'left', (-1, 0): 'up'}

def cheapest_path(grid, start, finish):
    h, w = len(grid), len(grid[0])
    prev, bag = {start: None}, {start: 0}
    while bag:
        x, y = pos = min(bag, key=bag.get)
        if pos == finish: break
        cost = bag.pop(pos) + grid[x][y]
        for u, v in DIRS:
            new_pos = m, n = x + u, y + v
            if not (0 <= m < h and 0 <= n < w): continue
            if new_pos in prev and new_pos not in bag: continue
            if cost < bag.get(new_pos, float('inf')):
                bag[new_pos], prev[new_pos] = cost, pos
    path = []
    while pos != start:
        (x1, y1), (x0, y0) = pos, prev[pos]
        path.append(DIRS[x1 - x0, y1 - y0])
        pos = prev[pos]
    return path[::-1]
#  1. Define the direction vectors for moving in a grid & their corresponding names. 
#     `DIRS = {(0, 1): 'right', (1, 0): 'down', (0, -1): 'left', (-1, 0): 'up'}`
#  2. Define the function cheapest_path which takes the toll_map matrix t, the start 
#     coordinate start, & the finish coordinate finish as input.
#  3. Get the dimensions of the toll map. `h, w = len(grid), len(grid[0])`
#  4. Initialize a dictionary prev to track the previous node & a dictionary bag to 
#     track the cost to reach a node.
#  5. Process nodes until the bag is empty.
#  6. Get the position w/ the lowest cost from the bag.
#  7. If the position is the finish, break the loop.
#  8. Calculate the cost to reach the current position.
#  9. Explore all possible movements from the current position.
# 10. Calculate the new position & the cost to reach it.
# 11. If the new position is not w/in the grid, continue to the next movement.
# 12. If the new position is already visited & not in the bag, continue to the next movement.
# 13. If the cost to reach the new position is less than the current cost, update the cost in the bag.
# 14. Backtrack from the finish to build the path list.
# 15. Append the movement to the path list.
# 16. Update the current position.
# 17. Return the reversed path.
# 18. This solution uses a priority queue to explore the grid & backtracks from the finish to build the path list.
#     It has a time complexity of O(n * log(n)) where n is the number of nodes in the grid & a space complexity of O(n) as well.
#     It is a modified version of Dijkstra's algorithm that uses a priority queue to find the path w/ the lowest cost. Its manual 
#     priority queue management using a dictionary is less efficient than the heapq-based priority queue in the 3rd solution, 
#     but it is still a viable approach for this problem. For larger grids or more complex scenarios, the manual approach might 
#     lead to slower performance due to less efficient priority queue operations. Using heapq or implementing a more standard 
#     priority queue might enhance both performance & readability.