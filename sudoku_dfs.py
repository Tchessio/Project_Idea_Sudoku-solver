import os
from collections import deque
import sudoku


def dfs(puzzle):
    solutions_tried = set()
    stack = deque()
    empty_list = []
    empty_fields = {}
    current_state = puzzle
    fields_entered = []

    # read the sudoku in order to list the empty fields and possible values
    def define_possible_values():
        for i in current_state.read_empty_fields():
            empty_fields[i] = current_state.read_possible_values(int(i[0]),int(i[1]))
        return empty_fields

   # check for easy numbers to be filled
    def find_sole_number():
        sole_number = []
        for i in possible_values:
            if len(possible_values[i]) == 1:
                sole_number.append(str(i) + str(possible_values[i]))
        return sole_number

    def update_sole_number():
        update = current_state.sudoku_to_string()
        for i in sole_numbers:
            x = int(i[0])
            y = int(i[1])
            value = str(i[2])
            place = x * 9 + y
            update = update[0:place] + value + update[place+1:]
            fields_entered.append(i)
            del(possible_values[(str(x)+str(y))])
        return update

    possible_values = define_possible_values()
    sole_numbers = find_sole_number()

    while sole_numbers:
        current_state = sudoku.Sudoku(current_state.string_to_sudoku(update_sole_number()))
        possible_values = define_possible_values()
        sole_numbers = find_sole_number()


    #print(possible_values)
    for key in possible_values.keys():
        empty_list.append(key)

    for value in possible_values[empty_list[0]]:
        stack.append(value)

    attempt = 0

# sprawdz czy juz to bylo testowane tak = idz dalej, nie = wez kolejna
    while stack:
        attempt +=1

        next_try = stack.pop()

        if not next_try in solutions_tried:

            solutions_tried.add(next_try)
            current_state = sudoku.Sudoku(puzzle.update_field(empty_list, next_try))

            field = empty_list[len(next_try)-1]
            x = int(field[0])
            y = int(field[1])

            row_conflict = sudoku.check_conflicts(current_state.get_row_numbers(x))
            column_conflict = sudoku.check_conflicts(current_state.get_column_numbers(y))
            box_conflict = sudoku.check_conflicts(current_state.get_block_numbers(x,y))

            is_conflict = row_conflict or column_conflict or box_conflict

            if not is_conflict: # nie ma konfliktu - wrzuc na stack kolejne pole
                if current_state.check_solution():
                    print('solution: ' + os.linesep + str(current_state.print_sudoku()))
                    print('attempts: ' + str(attempt))
                    exit()

                for value in possible_values[empty_list[len(next_try)]]:
                    stack.append(next_try + value)


    print("no solutions")



table = ['084000013',
        '200030600',
        '600509002',
        '002000469',
        '700000000',
        '000280000',
        '020700000',
        '008005906',
        '500020307']
s = sudoku.Sudoku(table)
print(dfs(s))

