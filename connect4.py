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

    def move(self, position: int) -> int:
        if self.heights[position] < 0:
            return -2
        curent_height = self.heights[position]
        self.grid[curent_height][position] = self.turn
        self.heights[position] -= 1
        if self.connect_4(curent_height, position):
            return self.turn
        self.turn *= -1
        return 0

    def reset(self):
        self.grid = [[0 for _ in range(GRID_COLUMNS)] for _ in range(GRID_ROWS)]
        self.turn = 1
        self.heights = [GRID_ROWS - 1 for _ in range(GRID_COLUMNS)]
