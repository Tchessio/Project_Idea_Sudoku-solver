
class Sudoku:

    def __init__(self, sudoku_x=9, sudoku_y=9):
        self.sudoku_x = sudoku_x
        self.sudoku_y = sudoku_y
        self.sudoku = ['250000000',
                       '000000000',
                       '000000000',
                       '000000000',
                       '000000000',
                       '000000000',
                       '000000000',
                       '000000000',
                       '000000000']

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

    def read_empty_fields(self):
        empty = []
        for x in range(0, self.sudoku_x):
            for y in range(0, self.sudoku_y):
                if self.sudoku[x][y] == "0":
                    empty.append(str(x) + str(y))
        return empty



    def sudoku_to_string(self):
        result = ''
        for x in range(0, self.sudoku_x):
                result += self.sudoku[x]
        return result


    def check_solution(self):
        solved = True
        for i in range(0,8):
            if "0" in self.sudoku[i]:
                solved = False
        return solved



#TODO: algorytm przeszukiwania pionowego
#TODO: jakis intuicyjny sposob wprowadzania danych

def check_conflicts(values):
    for i in range(int(values)):
        if values[i] != "0":
            if values.count(values[i]) > 1:
                return True
            return False




#s = Sudoku(9,9)
#print(s.read_empty_fields())
#print("0" in s.sudoku[1])