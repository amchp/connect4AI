from typing import Union


GRID_ROWS = 6
GRID_COLUMNS = 7
CONNECT_TILES = 4

class Connect4:
    def __init__(self) -> None:
        self.reset()

    def inside_grid(self, i: int, j: int) -> bool:
        return (
            i >= 0 and 
            i < len(self.grid) and 
            j >= 0 and 
            j < len(self.grid[i])
        )

    def check_direction(
        self,
        i: int,
        j: int,
        cur_dir_i: int,
        cur_dir_j: int
    ) -> int:
        assert self.inside_grid(i, j)
        turn = self.grid[i][j]
        assert turn != 0
        for connections in range(CONNECT_TILES - 1):
            i += cur_dir_i
            j += cur_dir_j
            if (
                (not self.inside_grid(i, j)) or 
                self.grid[i][j] != turn
            ):
                return connections
        return CONNECT_TILES - 1

    def connect_4(self, i: int, j: int) -> bool:
        dir_i = [-1, -1, -1, 0]
        dir_j = [-1, 0, 1, -1]
        for k in range(4):
            cur_dir_i = dir_i[k]
            cur_dir_j = dir_j[k]
            if (
                (
                    self.check_direction(i, j, cur_dir_i, cur_dir_j) + 
                    self.check_direction(i, j, -cur_dir_i, -cur_dir_j)
                ) >= CONNECT_TILES - 1
            ):
                return True
        return False
    
    def make_state(self) -> list[int]:
        state = [
            self.grid[i][j]
            for i in range(len(self.grid))
            for j in range(len(self.grid[i]))
        ]
        return state

    def move(self, position: int) -> Union[list[int], int, int]:
        if self.heights[position] < 0:
            return (self.make_state(), +1000, 0)
        curent_height = self.heights[position]
        self.grid[curent_height][position] = self.turn
        self.heights[position] -= 1
        self.num_move += 1
        if self.connect_4(curent_height, position):
            return (self.make_state(), -self.num_move, self.turn)
        if sum(self.heights) == -7:
            return (self.make_state(), -self.num_move, 2)
        self.turn *= -1
        return (self.make_state(), -self.num_move, 0)

    def reset(self) -> list[int]:
        self.grid = [[0 for _ in range(GRID_COLUMNS)] for _ in range(GRID_ROWS)]
        self.turn = 1
        self.heights = [GRID_ROWS - 1 for _ in range(GRID_COLUMNS)]
        self.num_move = 1
        return self.make_state()
