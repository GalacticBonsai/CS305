import a1
import math
import types
    
# Unit tests for CS305 Unit 1 homework assignment 
    
def test_1():
  assert a1.rectangle_area.__doc__, "provide a docstring comment with your function definition"
  assert a1.rectangle_area(3, 3) == 9, "did not properly determine area of square of size 3"
  assert a1.rectangle_area(4, 10) == 40, "did not properly determine area of 4x10 rectangle"
  assert a1.rectangle_area(10, 4) == 40, "did not properly determine area of 4x10 rectangle"
  assert a1.rectangle_area(3, 8) == 24, "did not properly determine area of 8x3 rectangle"
  assert a1.rectangle_area(8, 3) == 24, "did not properly determine area of 8x3 rectangle"
  assert a1.rectangle_area(3, 3) == 9, "did not properly determine area of square"
  assert a1.rectangle_area(5) == 25, "did not properly use the default value for width"
  assert a1.rectangle_area(4) == 16, "did not properly use the default value for width"
  
  
def test_2():
  assert isinstance(a1.circle_area, types.FunctionType), "circle_area does not hold a function"
  assert round(a1.circle_area(1), 5) == 3.14159, "Incorrect area for circle with radius 5"
  assert round(a1.circle_area(5), 5) == 78.53982, "Incorrect area for circle with radius 5"
  assert round(a1.circle_area(9.5), 5) == 283.52874, "Incorrect area for circle with radius 5"
    
    
def test_3_1():
  ans = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  assert isinstance(a1.perfect_squares, tuple), """perfect_squares doesn't contain a tuple"""
  assert len(a1.perfect_squares) == len(ans), "incorrect number of values in perfect_squares; was " + str(len(a1.perfect_squares)) + " but expected " + str(len(ans))
  assert list(a1.perfect_squares) == ans, "incorrect values in perfect_squares; was " + str(a1.perfect_squares) + " but expected " + str(tuple(ans))

def test_3_2():
  ans = set([1, 4, 64, 81, 100])
  assert isinstance(a1.squares_set, set), """squares_set doesn't contain a set"""
  assert len(a1.squares_set) == len(ans), "incorrect number of values in squares_set; was " + str(len(a1.squares_set)) + " but expected " + str(len(ans))
  assert a1.squares_set == ans, "incorrect values in perfect_squares; was " + str(a1.squares_set) + " but expected " + str(ans)
    
    
def test_4():
  g = a1.gen_squares(5, 10)
  assert isinstance(g, types.GeneratorType), "gen_squares is not returning a generator object"
  res_squares = [25, 36, 49, 64, 81]
  i = 0
  for s in g:
      assert i < len(res_squares), "Too many values were generated"
      assert s == res_squares[i], "The " + str(i+1) + "th value generated should be " + str(res_squares[i]) + ", instead was " + str(res_squares[i])
      i += 1
  assert i == len(res_squares), "Too few values were generated"
  
  # additional test cases
  assert list(a1.gen_squares(1, 4)) == [1, 4, 9], """Incorrect output for start=1, stop=4"""
  assert list(a1.gen_squares(10, 20)) == [100, 121, 144, 169, 196, 225, 256, 289, 324, 361], """Incorrect output for start=10, stop=20"""

if __name__ == '__main__':
    import pytest
    pytest.main()
