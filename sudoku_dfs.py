from collections import deque
import sudoku



def dfs(puzzle):
    solutions_tried = set()
    fixed_numbers = set()
    stack = deque()


    # read the sudoku in order to assign the fixed numbers
    fixed_numbers = puzzle.read_fixed_values()
    start = puzzle.define_start()

    # wez pierwsza mozliwa cyfre do wpisania
    stack.append('1')

# sprawdz czy juz to bylo testowane tak = idz dalej, nie = wez kolejna
    while stack:
        next_try = stack.pop()
        if not next_try in solutions_tried:
            solutions_tried.append(next_try)
            counter = 0
            for i in next_try:
                x = counter % 9
                y = counter // 9
                if str(x) + str(y) in fixed_numbers:
                    counter += 1
                else:
                    puzzle[x][y] = i
                    # jezeli nie ma konfliktow
                    if sudoku.check_conflicts(puzzle.get_row_numbers(x)):

                    elif sudoku.check_conflicts(puzzle.get_column_numbers(y)):
                    # umiesc na staku kolejna liczbe
                    elif sudoku.check_conflicts(puzzle.get_block_numbers(x,y)):
                counter += 1
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