from a4 import KNN_learner
import math
import types   
from operator import lt,ne,eq,gt
from learnProblem import Data_set
# Unit tests for CS305 Unit 4 homework assignment 
    
def test_1():
  """template"""
  examples = [
        [1, 1, 'a'],
        [1, 2, 'a'],
        [2, 1, 'a'],
        [2, 2, 'a'],
        [1.9, 1.9, 'b'],
        [8, 8, 'b'],
        [8, 7, 'b'],
        [7, 8, 'b']
      ]
  data = Data_set(examples, prob_test=0, target_index=-1)
  knn1 = KNN_learner(data, 1)
  knn1pred = knn1.learn()
  
  # within the upper-left cluster, 'a' will mostly be the answer
  assert knn1pred([1,1])['a'] == 1.0
  assert knn1pred([1.1,1.1])['a'] == 1.0
  assert knn1pred([1.4,1.4])['a'] == 1.0
  # too close to the outlier will flip the answer
  assert knn1pred([1.7,1.7])['b'] == 1.0
  assert knn1pred([2.1,2.1])['a'] == 1.0
  # in the bottom-right cluster, it will be the other answer
  assert knn1pred([7.7,7.8])['b'] == 1.0
  
  knn3 = KNN_learner(data, 3)
  knn3pred = knn3.learn()
  
  assert knn3pred([1,1])['a'] == 1.0
  assert knn3pred([1.1,1.1])['a'] == 1.0
  assert knn3pred([1.4,1.4])['a'] == 1.0
  # the outlier is smoothed over by the other two neighbors when k=3
  assert knn3pred([1.7,1.7])['a'] == 1.0
  assert knn3pred([2.1,2.1])['a'] == 1.0
  assert knn3pred([7.7,7.8])['b'] == 1.0

if __name__ == '__main__':
    import pytest
    pytest.main()