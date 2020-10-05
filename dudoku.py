import arcade
import random

class Dudoku():
    def __init__(self):
        self.cell_width = 60
        self.cell_height = 60
        self.cells = []	# x[y[]]
        self.cells_count = 30
        pass

    def new_game(self):
   		# create 9x9 field with values of 0
        for x in range(9):
            self.cells.append([])
            for y in range(9):
                self.cells[x].append(0)

        cells_to_create = self.cells_count
        while cells_to_create > 0:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            if (self.cells[x][y] == 0):
                new_value = random.randint(1, 9)
                if (not self.do_exist_in_row(x, new_value) and not self.do_exist_in_column(y, new_value)):
                    self.cells[x][y] = new_value
                    cells_to_create = cells_to_create - 1

    def do_exist_in_row(self, x, a):
        for cell in self.cells[x]:
            if (cell == a):
                return True
        return False

    def do_exist_in_column(self, y, a):
        for cell in self.cells:
            if (cell[y] == a):
                return True
        return False

    def draw_cells(self):
        for i in range(1, 10):
            for j in range(1, 10):
                    arcade.draw_rectangle_outline(i * self.cell_width - self.cell_width / 2 , 
                    	j * self.cell_height - self.cell_height / 2, self.cell_width, 
                    	self.cell_height, arcade.color.BRITISH_RACING_GREEN, 1)

    def draw_bigcells(self):
        w = 3 * self.cell_width
        h = 3 * self.cell_height
        for i in range(1, 4):
            for j in range(1, 4):
                arcade.draw_rectangle_outline(i * w - w / 2, j * h - h / 2, w, h, arcade.color.BRITISH_RACING_GREEN, 3)

    def draw_playground(self):
        arcade.draw_rectangle_outline(self.cell_width * 9 - (self.cell_width * 9) / 2, 
        	self.cell_height * 9 - (self.cell_height * 9) / 2, 
        	self.cell_width * 9, self.cell_height * 9, 
        	arcade.color.BRITISH_RACING_GREEN, 10)

        self.draw_cells()
        self.draw_bigcells()