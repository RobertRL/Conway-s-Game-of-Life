from cell import Cell
from random import randint


class Board:
    def __init__(self,rows,columns):
        self._rows = rows
        self._columns = columns
        self._grid = [[Cell() for column_cells in range(self._columns)]for row_cells in range(self._rows)]

        self._generate_board()
    def draw_board(self):
        print('\n'*10)
        print("printing board")
        for row in self.grid:
            for column in row:
                print(column.get_print_character(),end="")
            print()
    def _generate_board(self):
        for row in self._grid:
            for column in row:
                chances_numer = randint(0, 2)
                if chances_numer == 1:
                    column.set_alive()

    def update_board(self):
        
        goes_alive = []
        gets_killed = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                
                check_neighbour = self.check_neighbour(row , column)
                
                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    #check live status for neighbour_cell:
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self._grid[row][column]
                status_main_cell = cell_object.is_alive()

                if status_main_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append(cell_object)

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)

        for cell_items in goes_alive:
            cell_items.set_alive()

        for cell_items in gets_killed:
            cell_items.set_dead()
