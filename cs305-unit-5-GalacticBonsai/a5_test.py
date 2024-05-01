from a5 import K_means_learner
import math
import types   
from operator import lt,ne,eq,gt
from learnProblem import Data_set, Learner, Data_from_file
    
# Unit tests for CS305 Unit 5 homework assignment 

class Fake_learner(K_means_learner):
    def __init__(self,dataset,clusters):
        self.dataset = dataset
        self.num_classes = len(clusters)
        self.class_counts = []
        for c in clusters:
            self.class_counts.append(len(c))

        self.feature_sum = [[0]*self.num_classes
                            for feat in self.dataset.input_features]
        
        for eg in self.dataset.train:
            cl = 0
            for i in range(len(clusters)):
                if eg in clusters[i]:
                    cl = i
                    break

            for (ind,feat) in enumerate(self.dataset.input_features):
                self.feature_sum[ind][cl] += feat(eg)
                
        self.num_iterations = 0

def test_1():
  # assign two clearly matched examples to each cluster
  # to generate a positive silhouette score
  clusters = [
      [[1.1, 1, 'X'],
      [1, 1, 'X']],
      
      [[10.1, 10, 'X'],
      [10,10, 'X']]
    ]
  examples = []
  for c in clusters:
      for ex in c:
          examples.append(ex)
  data = Data_set(examples, prob_test=0, target_index=-1)
  learner = Fake_learner(data, clusters)
  print(learner.average_silhouette_score())
  assert learner.average_silhouette_score() > 0
  assert learner.average_silhouette_score() <= 1


def test_2():
  # assign two clearly mismatched examples to each cluster
  # to generate a negative silhouette score
  clusters = [
      [[10.1, 10,'X'],
      [1, 1, 'X']],
      
      [[1.1, 1, 'X'],
      [10,10, 'X']]
    ]
  examples = []
  for c in clusters:
      for ex in c:
          examples.append(ex)
  data = Data_set(examples, prob_test=0, target_index=-1)
  learner = Fake_learner(data, clusters)
  print(learner.average_silhouette_score())
  assert learner.average_silhouette_score() < 0
  assert learner.average_silhouette_score() >= -1
  

if __name__ == '__main__':
    import pytest
    pytest.main()
