def update_board(self):
    print("updating board")
    goes_alive = []
    gets_killed= []
    for row in range(len(self._grid)):
        for column in range(len(self._grid)):

            check_neighbor = self.check_neighbor(row,column)

            living_nighbor_count = []

            for neighbor_cell in check_neighbor:
                if neighbor_cell.is_alive:
                    living_nighbor_count.append(nighbor.cell)
            cell_object = self._grid[row][column]
            status_main_cell = cell_object.is_alive()


            if status_main_cell == True:
                if len(living_nighbor_count) < 2 or len(living_nighbor_count) > 3:
                    gets_killed.append(cell_object)
                if len(living_nighbor_count) ==3 or len(living_nighbor_count) == 2:
                    goes_alive(cell_object)
            else:
                if len(living_nighbor_count)==3:
                    goes_alive(cell_object)

    for cell_items in goes_alive:
        cell_items.set_alive
    for cell_item in gets_killed:
        cell_item.set_dead