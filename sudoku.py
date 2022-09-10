import math

"""
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.parent = p
        self.cost = math.inf

    def set_parent(self, p):
        self.parent = p

    def set_cost(self, c):
        self.cost = c

    def print(self):
        print(self.x, ' , ', self.y)

"""



class Sudoku:

    def __init__(self, sudoku_x=9, sudoku_y=9):
        self.sudoku_x = sudoku_x
        self.sudoku_y = sudoku_y
        self.sudoku = ['120000000',
                       '000000000',
                       '000000000',
                       '000000000',
                       '000000000',
                       '000000000',
                       '000000000',
                       '000000000',
                       '900000003']

    def get_current_point_value(self, current_point):
        return self.sudoku[current_point.x][current_point.y]

    def get_row_numbers(self, row_number):
        row_numbers = self.sudoku[row_number]
        return row_numbers

    def get_column_numbers(self, column_number):
        column_numbers = ""
        for i in range(0, self.sudoku_x):
            column_numbers += self.sudoku[i][column_number]
        return column_numbers

    def get_block_numbers(self, row_number, column_number):
        block_numbers = ""
        x = row_number // 3 * 3
        y = column_number // 3 * 3
        #return x,y
        for i in range(0, 3):
            for j in range(0, 3):
                block_numbers += self.sudoku[x+i][y+j]
        return block_numbers

    def read_fixed_values(self):
        fixed = set()

        for x in range (0, self.sudoku_x):
            for y in range (0, self.sudoku_y):
                if self.sudoku[x][y] != "0":
                    fixed.add(str(x) + str(y))

        return fixed

    def define_start(self):
        for x in range (0, self.sudoku_x):
            for y in range (0, self.sudoku_y):
                if self.sudoku[x][y] == "0":
                    start = str(x) + str(y)
                    return start

    #def enter_field:
    #    pass

    def print_sudoku(self):
        result = ''
        for x in range(0, self.sudoku_x):
            for y in range(0, self.sudoku_y):
                result += self.sudoku[x][y]
            result += '\n'
        print(result)

#TODO: algorytm przeszukiwania pionowego
#TODO: jakis intuicyjny sposob wprowadzania danych

def check_conflicts(values):
    for i in range(int(values)):
        if values[i] != "0":
            if values.count(values[i]) > 1:
                return True
            return False




#s = Sudoku(9,9)
#print(s.define_start())