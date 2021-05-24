class TableCheck:
    def __init__(self):
        self._grid = [["a","b","c"],
                      ["d","e","f"],
                      ["g","h","i"],
                      ["j","k","l"]]
    def print_grid(self):
        for row in self._grid:
            print(row)
