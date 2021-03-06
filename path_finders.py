from tree import Node


class KnightPathFinder:
    def __init__(self, coordinates):
        # self._coordinates = coordinates
        self._root = Node(coordinates)
        self._considered_positions = {coordinates}

    def get_valid_moves(self, pos):
        valid_moves = {
            (pos[0] - 1, pos[1] + 2),
            (pos[0] + 1, pos[1] + 2),
            (pos[0] + 2, pos[1] - 1),
            (pos[0] + 2, pos[1] + 1),
            (pos[0] - 1, pos[1] - 2),
            (pos[0] + 1, pos[1] - 2),
            (pos[0] - 2, pos[1] - 1),
            (pos[0] - 2, pos[1] + 1)
        }

        filtered = [z for z in set(valid_moves) if
                    z[0] >= 0 and z[1] >= 0 and z[0] < 8 and z[1] < 8]

        return set(filtered)

    def new_move_positions(self, pos):
        move_positions = self.get_valid_moves(pos) - self._considered_positions
        return move_positions

    def build_move_tree(self):
        queue = []
        queue.append(self._root)
        currNode = None
        while queue:
            currNode = queue.pop(0)
            self._considered_positions.add(currNode.value)
            newMoves = self.new_move_positions(currNode.value)
            for move in newMoves:
                currNode.add_child(Node(move))
            for child in currNode.children:
                queue.append(child)

    def find_path(self, end_position):
        node = self._root.breadth_search(end_position)
        return self.trace_to_root(node)

    def trace_to_root(self, end_node):
        path = []
        currNode = end_node
        while currNode is not self._root:
            path.append(currNode.value)
            currNode = currNode.parent
        path.append(currNode.value)
        return sorted(path)


finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((4, 4)))
finder.build_move_tree()
# print(finder._root.children)
print(finder.find_path((2,1)))
print(finder.find_path((3,3)))
print(finder.find_path((6,2)))
print(finder.find_path((7,6)))
