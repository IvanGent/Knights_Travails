from tree import Node

class KnightPathFinder:
    def __init__ (self, coordinates):
        self._coordinates = coordinates
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

        filtered = [z for z in set(valid_moves) if z[0] >= 0 and z[1] >= 0]


        return set(filtered)
    
    def new_move_positions(self, pos):
        move_positions = self.get_valid_moves(pos) - self._considered_positions
        return move_positions
        

finder = KnightPathFinder((0, 0))
print(finder.new_move_positions((0, 0)))
