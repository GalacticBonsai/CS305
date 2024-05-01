import a2
import math
import types
from cspProblem import Variable, CSP, Constraint
from cspDFS import dfs_solve1    
from operator import lt,ne,eq,gt
    
# Unit tests for CS305 Unit 2 homework assignment 
    
puzzle_text1 = """ 
 5 3 4 | 6 7 8 | 9 1 2 
 6 7 2 | 1 9 5 | 3 4 8 
 1 9 8 | 3 4 2 | 5 6 7
-------+-------+------ 
 8 5 9 | 7 6 1 | 4 2 3
 4 2 ? | 8 ? 3 | ? 9 1 
 7 1 3 | 9 2 4 | 8 5 6 
-------+-------+------ 
 9 6 1 | 5 3 7 | 2 8 4 
 2 8 7 | 4 1 9 | 6 3 5 
 3 4 5 | 2 8 6 | 1 7 9
"""
variables = a2.puzzle_text_to_var_dict(puzzle_text1)
empty_puzzle = """  
 ? ? ? | ? ? ? | ? ? ? 
 ? ? ? | ? ? ? | ? ? ? 
 ? ? ? | ? ? ? | ? ? ?
-------+-------+------ 
 ? ? ? | ? ? ? | ? ? ? 
 ? ? ? | ? ? ? | ? ? ? 
 ? ? ? | ? ? ? | ? ? ? 
-------+-------+------ 
 ? ? ? | ? ? ? | ? ? ? 
 ? ? ? | ? ? ? | ? ? ? 
 ? ? ? | ? ? ? | ? ? ?
"""
empty_vars = a2.puzzle_text_to_var_dict(empty_puzzle)
    
def test_1():
  """determine that the constraint builder is creating actual constraints"""
  constraints = a2.create_sudoku_constraints(variables)
  for c in constraints:
    assert type(c) == Constraint, "create_sudoku_constraints must only return a list of Constraint objects"
    
if __name__ == '__main__':
    import pytest
    pytest.main()
