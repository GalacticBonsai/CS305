# CS305 Park University
# Assignment #2 Starter Code
# Solving Sudoku as a CSP
# Joseph Halla
# 3/24/2024

from cspProblem import Variable, CSP, Constraint
from cspDFS import dfs_solve1    
from operator import lt,ne,eq,gt

# Attention:
# To test your code, add ?'s where you want to have the CSP solver determine
# the variable value. The search-based approach isn't very efficient, so 
# adding too many may make the solver spend a very long time searching for 
# a solution. Consider how you could make this more efficient by manipulating
# the domains in the puzzle_text_to_var function below or by using a more
# sophisticated CSP solving algorithm from the optional reading in Ch. 4.
#
# The code you have to write for this assignment is further below. 

puzzle_text1 = """ 
 5 3 4 | 6 7 8 | 9 1 2 
 6 7 2 | 1 9 5 | 3 4 8 
 1 9 8 | 3 4 2 | 5 6 7
-------+-------+------ 
 8 5 9 | 7 6 1 | 4 2 3
 4 2 ? | 8 ? 3 | ? 9 1 
 7 1 3 | 9 2 4 | 8 5 6 
-------+-------+------ 
 9 6 1 | 5 3 7 | ? ? ? 
 2 8 7 | 4 1 9 | ? ? ? 
 3 4 5 | 2 8 6 | 1 ? ?
"""


def puzzle_text_to_var_dict(txt):
  """converts a textual representation of a sudoku board to a dictionary of
  variables with (row, col) tuples as keys"""
  variables = dict()
  row, col = 1, 1
  for c in txt:
    if c >= '1' and c <= '9':
      variables[row, col] = Variable('['+str(row)+','+str(col)+']', {int(c)}, (row, col))
      col = (col % 9) + 1
      if col == 1: 
        row = (row % 9) + 1
    if c == '?':
      variables[row, col] = Variable('['+str(row)+','+str(col)+']', set(range(1,10)), (row, col))
      col = (col % 9) + 1
      if col == 1: 
        row = (row % 9) + 1
  return variables
      
      
def print_solution(sol, variables):
  """prints out variable assignments as a sudoku board for a CSP sudoku solution"""
  for r in range(1,10):
    print(" ", end="")
    for c in range(1,10):
      print(sol[variables[r,c]], end="")
      if c % 3 == 0 and c < 9:
        print(" | ", end="")
      else:
        print(" ", end="")
    if r % 3 == 0 and r < 9:
      print("\n-------+-------+------")
    else:
      print("")
  
def create_sudoku_constraints(variables): 
  constraints = []
  # Specifically: 
  #  1) Every variable in a row of the puzzle must have unique values assigned
  #     from the domain {1, 2, ... 9}
  for row in range(1, 10):
    row_vars = [variables[(row, col)] for col in range(1, 10)]
    row_constraint = Constraint(row_vars, lambda *values: len(set(values)) == len(row_vars))
    constraints.append(row_constraint)

  #  2) Every variable in a column of the puzzle must have unique values 
  #     assigned from the domain {1, 2, ... 9}
  for col in range(1, 10):
    col_vars = [variables[(row, col)] for row in range(1, 10)]
    col_constraint = Constraint(col_vars, lambda *values: len(set(values)) == len(col_vars))
    constraints.append(col_constraint)

  #  3) Every variable in a block (see segmented portion of the strings above)
  #     of the puzzle must have unique values assigned from the 
  #     domain {1, 2, ... 9}
  for block_row in range(0, 3):
    for block_col in range(0, 3):
      block_vars = []
      for i in range(1, 4):
        for j in range(1, 4):
          block_vars.append(variables[(block_row * 3 + i, block_col * 3 + j)])
      block_constraint = Constraint(block_vars, lambda *values: len(set(values)) == len(block_vars))
      constraints.append(block_constraint)

  return constraints

def main():
  puzzle_text = puzzle_text1
  variables = puzzle_text_to_var_dict(puzzle_text)
  constraints = create_sudoku_constraints(variables)
  print("Input Puzzle: ")
  print(puzzle_text)
  print("Solution: ")
  sudoku1 = CSP("sudoku", variables.values(), constraints)
  sol = dfs_solve1(sudoku1)
  print_solution(sol, variables)
  
if __name__ == '__main__':
  main()
