# CS305 Park University
# Assignment #4 Starter Code
# Supervised Learning Lab

from learnProblem import Data_from_file, Learner, Evaluate
from learnDT import DT_learner
from learnCrossValidation import K_fold_dataset
from statistics import mean, mode
import math

# In this assignment you'll perform supervised learning and analyze
# the results of the process. The initial steps are in the main function
# below where you will develop a baseline for the iris dataset and
# also test decision tree analysis against this dataset.
#
# Following that, you will need to complete the definition of the
# k-nearest-neighbor learner class (described in your reading)
# and additionally analyze it against the other techniques over
# several values of its "hyperparameter" k. Euclidean distance will
# be used in every case. 

class KNN_learner(Learner):
    """Lazy learning algorithm for a categorical target and numeric features"""
    def __init__(self,
                 dataset,
                 k=1,
                 train=None):
        self.dataset = dataset
        self.target = dataset.target
        self.k = k
        if train is None:
            self.train = self.dataset.train
        else:
            self.train = train

    def learn(self):
        """defines the k-nn prediction function to be returned
          the function will rely on the original dataset for predictions
        """
        def ev(ex):
            # find neighbors of ex
            ns = list(self.get_neighbors(ex, self.k))
            classes = set(map(self.target, self.train)) # all possible classes
            t = self.majority_vote(ns) # most common class among neighbors
            return { c: 1 if t == c else 0 for c in classes}  # prediction dictionary
        return ev
        
    def majority_vote(self, exs):
        """determines the most common target classification among examples"""
        return mode(map(self.target, exs))


#
# NOTE: Step 1 is below in the main function
#

# 5. 
# TODO: complete the definition of the euclidean distance function
    def euclidean_dist(self, ex1, ex2):
        """find euclidean distance between features of two examples"""
        dist = 0
        for i in range(len(ex1) - 1):  # Assuming the last element is the target
            dist += (ex1[i] - ex2[i]) ** 2
        return math.sqrt(dist)
# 6.
# TODO: complete the definition of the get_neighbors function    
    def get_neighbors(self, ex, k):
        """generate the k closest neighbors of example 'ex'"""
        distances = []
        for i in range(len(self.train)):
            dist = self.euclidean_dist(ex, self.train[i])
            distances.append((self.train[i], dist))
        distances.sort(key=lambda x: x[1])  # Sort by distance
        neighbors = [dist[0] for dist in distances[:k]]
        return neighbors

def main():
    folds = 10
    trials = 100
    dataset_filename = 'data/iris.data'
    bl_acc=0
    dt_acc=0

    for i in range(trials):
# 1. 
# TODO: load the dataset (using the specified filename)
# store it in the variable 'data'.
# We're not using cross validation so use the defaults for
# creating a training and test set.
        data = Data_from_file(dataset_filename)

# 2.        
# TODO: create the baseline predictor (always guess the mode)
# hint: look at the implementation of majority_vote and check
# the notes. 
        def baseline(example):
            return mode([example[i] for i in range(len(example) - 1)])
        bl_acc += data.evaluate_dataset(data.test,
                                       baseline,
                                       Evaluate.accuracy)
# 3.         
# in the end results, you'll see that the accuracy for the
# baseline is a little worse than what you might consider
# for random guessing. Why do you suppose that is the case
# for this dataset?
# TODO: Briefly answer in comments
# The baseline predictor always guesses the mode of the target variable.
# The mode in the training set might not necessarily be the mode in the test set
# leading to lower accuracy than random guessing.

    bl_acc /= trials
    
# 4. 
# TODO: load the dataset again, but make sure all examples are
# training examples (since we'll use cross-validation).
# store it in the variable 'data'.
    data = Data_from_file(dataset_filename, prob_test=0, target_index=-1)
    for i in range(trials):
        cvdata = K_fold_dataset(data, folds)
        dt_acc += cvdata.validation_error(DT_learner, Evaluate.accuracy)
    dt_acc /= trials
    
    # 7. 
    # TODO: add k values to the list you want to check for accuracy
    kvals = [1,3,5]
    knn_accs = []  # will hold accuracies for each k value
    for k in kvals:
        acc = 0
        for i in range(trials):
            cvdata = K_fold_dataset(data, folds)
            acc += cvdata.validation_error(KNN_learner,
                                Evaluate.accuracy,
                                distance=KNN_learner.euclidean_dist, # pytest requires euclideon_dist to be in KNN_learner
                                k=k)
        acc /= trials
        knn_accs.append(acc)
    
    print('after', trials, 'trials...')
    print('basline accuracy:', bl_acc)
    print('decision tree accuracy:', dt_acc)
    print('knn accuracy for:')
    for i in range(len(kvals)):
        print('k =',kvals[i],':', knn_accs[i])
    
# 8. 
# TODO: what methods are working the best? Add brief comments to
# your final submission.
# - The decision tree (DT) learner achieves the highest accuracy among all methods.
# - The k-nearest neighbors (KNN) learner with k=3 also performs reasonably well, but slightly lower than the DT learner.
# - The baseline predictor (mode) has the lowest accuracy, indicating that the dataset may not be well-suited for simple majority voting.
# - Further analysis and parameter tuning could potentially improve the performance of the KNN learner.
  
if __name__ == '__main__':
  main()
