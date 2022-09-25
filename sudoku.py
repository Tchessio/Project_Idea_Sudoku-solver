import os


class Sudoku:

    def __init__(self, table):
        self.sudoku_x = 9
        self.sudoku_y = 9
        self.sudoku = table

    def get_current_point_value(self, field):
        return self.sudoku[int(field[0])][int(field[1])]

    def update_field(self, empty_list, values):

        for i in range(len(empty_list)):
            x = int(empty_list[i][0])
            y = int(empty_list[i][1])

            if i < len(values):
                value = values[i]
            else:
                value = 0

            row = self.sudoku[x]
            new_row = row[0:y] + str(value) + row[y+1:]
            self.sudoku[x] = new_row
        return self.sudoku

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

    def read_possible_values(self, row, column):
        possible_values = ""
        for number in range(1, 10):
            possible_values += str(number)

        cannotuse = self.get_row_numbers(row) + self.get_column_numbers(column) + self.get_block_numbers(row,column)
        for number in cannotuse:
            if number != "0":
                possible_values = possible_values.replace(str(number), "")

        return possible_values

    def sudoku_to_string(self):
        result = ''
        for x in range(0, self.sudoku_x):
                result += self.sudoku[x]
        return result


    def print_sudoku(self):
        result = '_______________' + os.linesep

        for x in range(0, self.sudoku_x):
            row = self.sudoku[x]
            print_row = "||"
            for i in range(0, 3):
                for j in range(0,3):
                    print_row += row[i * 3 + j]
                print_row += '|'


            result += print_row + '|' + os.linesep

        result += '_______________'
        return str(result)

    def string_to_sudoku(self, string):
        for i in range(0,9):
            row = ""
            for j in range(0,9):
                row += str(string[i*9+j])
            self.sudoku[i] = row
        return self.sudoku

    def check_solution(self):
        solved = True
        for i in range(0,9):
            if "0" in self.sudoku[i]:
                solved = False
        return solved



#TODO: algorytm przeszukiwania pionowego
#TODO: jakis intuicyjny sposob wprowadzania danych

def check_conflicts(values):
    for i in range(len(values)):
        if values[i] != "0":
            #print('co ' + values[i])
            #print('ile ' + str(values.count(values[i])))
            if values.count(values[i]) > 1:
                return True
    return False

"""
table = ['084000013',
        '200030600',
        '600509002',
        '002000469',
        '700000000',
        '000280000',
        '020700000',
        '008005906',
        '500020307']

list = ['00', '02', '03', '04', '05', '06', '07', '08', '10', '12', '14']
values = ['1', '1', '1']
s = Sudoku(table)
print(s.print_sudoku())



"""
print(check_conflicts('561928387'))