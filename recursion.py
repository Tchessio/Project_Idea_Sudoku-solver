import sudoku



def solve(s):

    i = s.find('0')
    row = i//9
    column = i%9

    possible_values = ""
    for number in range(1, 10):
        possible_values += str(number)

    cannotuse = sudoku.get_row_numbers(row) + sudoku.get_column_numbers(column) + sudoku.get_block_numbers(row, column)

    for number in cannotuse:
        if number != "0":
            possible_values = possible_values.replace(str(number),"")

    for v in possible_values:
        s = s[0:i] + v + s[i+1: ]
        solve(s)
        if val.find('0') == -1:
            return(s)


sudoku = sudoku.Sudoku()
To_be_solved = sudoku.sudoku_to_string()
print(solve(To_be_solved))