"""
dict = {'00': '5679', '02': '579', '03': '1235678'}
list = ['00', '02', '03']

conflict = False

#if not row_conflict and not column_conflict and not box_conflict:
#    if not puzzle.check_solution():

current_field = 0
current_number = 0

next_try=dict[list[current_field]][current_number]

if not conflict:
    current_field += 1
    current_number = 0
    next_try += dict[list[current_field]][current_number] # wez pierwsza cyfre z kolejnego pola
    print(next_try)
else:
    print("solved")
    print(next_try)

print(dict[list[current_field]][-1])

"""



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

   # check for easu numbers to be filled
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
    #print(empty_list)


    for i in range(0,len(empty_list)):
        for j in range(0,len(empty_list[i])):
            field = empty_list[i]
            value = possible_values[empty_list[i]][j]
            current_state = sudoku.Sudoku(current_state.update_field(field, value))

            x = int(field[0])
            y = int(field[1])

            row_conflict = sudoku.check_conflicts(current_state.get_row_numbers(x))
            column_conflict = sudoku.check_conflicts(current_state.get_column_numbers(y))
            box_conflict = sudoku.check_conflicts(current_state.get_block_numbers(x,y))

            #print(row_conflict, column_conflict, box_conflict)
            if not row_conflict and not column_conflict and not box_conflict:
                if not puzzle.check_solution():
                    #current_field += 1
                    #current_number = 0
                    #next_try += str(possible_values[empty_list[current_field]][current_number]) # wez pierwsza cyfre z kolejnego pola
                    #stack.append(next_try)
                else:
                    print("solved")
                    print(next_try)
            elif not current_number == possible_values[empty_list[current_field]][-1]: # czy to juz ostatnia cyfra w polu
                # jezeli nie jest:
                current_number +=1

            else:
                current_field -=1
        print("no solutions")



table = ['040000000',
         '020904000',
         '183000942',
         '206080000',
         '830000560',
         '000061038',
         '400002180',
         '068090407',
         '000040050']
s = sudoku.Sudoku(table)
print(dfs(s))

