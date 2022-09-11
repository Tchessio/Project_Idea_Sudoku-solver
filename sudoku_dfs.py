from collections import deque
import sudoku



def dfs(puzzle):
    solutions_tried = set()
    fixed_numbers = set()
    stack = deque()


    # read the sudoku in order to list the empty fields
    empty_fields = puzzle.read_empty_fields()
    start = puzzle.define_start()

    # wez pierwsza mozliwa cyfre do wpisania
    stack.append('1')

# sprawdz czy juz to bylo testowane tak = idz dalej, nie = wez kolejna
    while stack:
        next_try = stack.pop()
        if not next_try in solutions_tried:
            solutions_tried.append(next_try)
            for i in next_try:
                field = empty_fields[i]
                x = field[0]
                y = field[1]
                puzzle[x][y] = i
                row_conflict = Sudoku.check_conflicts(puzzle.get_row_numbers(x)):
                column_conflict = Sudoku.check_conflicts(puzzle.get_column_numbers(y)):
                box_conflict = Sudoku.check_conflicts(puzzle.get_block_numbers(x,y)):

                if not row_conflict and not column_conflict and not box_conflict:
                    if puzzle.check_solution():



            next_try = str(int(next_try) + 1)  # umiesc na staku kolejna cyfre


                    # umiesc na staku kolejna liczbe
                    # nie ma konfliktow ale sa zera to wez dziecko
                    # nie ma konfliktow i nie ma zer




        return 'brak rozwiazan'



# wpisz + dodaj do setu odwiedzonych

# sprawdz warunki jak true i jak 3x true i w sudoku nie ma zer to cel osiagniety, wydrukuj sudoku

# jak 3x true i sa zera to wez kolejne pole

    return start


s = sudoku.Sudoku(9,9)
print(dfs(s))