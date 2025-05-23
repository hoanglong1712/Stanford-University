#!/usr/bin/python
import math
import random
from typing import Callable, Dict, List, Tuple, TypeVar

from util import *

FeatureVector = Dict[str, int]
WeightVector = Dict[str, float]
Example = Tuple[FeatureVector, int]


############################################################
# Problem 3: binary classification
############################################################

############################################################
# Problem 3a: feature extraction

def extractWordFeatures(x: str) -> FeatureVector:
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x:
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    # raise Exception("Not implemented yet")
    words = x.split(' ')
    word_features = {}
    for word in words:
        word_features[word] = word_features.get(word, 0) + 1
        pass
    return word_features
    # END_YOUR_CODE


############################################################
# Problem 3b: stochastic gradient descent

T = TypeVar('T')


def learnPredictor(trainExamples: List[Tuple[T, int]],
                   validationExamples: List[Tuple[T, int]],
                   featureExtractor: Callable[[T], FeatureVector],
                   numEpochs: int, eta: float) -> WeightVector:
    '''
    Given |trainExamples| and |validationExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of epochs to
    train |numEpochs|, the step size |eta|, return the weight vector (sparse
    feature vector) learned.

    You should implement stochastic gradient descent.

    Notes:
    - Only use the trainExamples for training!
    - You should call evaluatePredictor() on both trainExamples and
      validationExamples to see how you're doing as you learn after each epoch.
    - The predictor should output +1 if the score is precisely 0.
    '''
    weights = {}  # feature => weight

    # BEGIN_YOUR_CODE (our solution is 13 lines of code, but don't worry if you deviate from this)
    # raise Exception("Not implemented yet")
    def hinge_loss(featuresVector: {}, y: float, w: {}):
        margin = y * dotProduct(featuresVector, w)
        return max(0, 1 - margin)

    for epoch in range(numEpochs):
        for x, y in trainExamples:
            features = featureExtractor(x)
            loss = hinge_loss(features, y, weights)
            if loss > 0:
                # weight update
                increment(weights, (-1) * y * eta, features)
                pass
            pass
        pass

    def predictor(x):
        # Compute the score
        score = sum(weights.get(feature, 0) * value for feature, value in featureExtractor(x).items())
        # Predict +1 for score >= 0, otherwise -1
        return 1 if score >= 0 else -1

    # print(evaluatePredictor(trainExamples, predictor))
    # END_YOUR_CODE
    return weights


############################################################
# Problem 3c: generate test case


def generateDataset(numExamples: int, weights: WeightVector) -> List[Example]:
    '''
    Return a set of examples (phi(x), y) randomly which are classified
      correctly by |weights|.
    '''
    random.seed(42)

    # Return a single example (phi(x), y).
    # phi(x) should be a dict whose keys are a subset of the keys in weights
    # and values can be anything (randomize!) with a score for the given weight vector.
    # note that there is intentionally flexibility in how you define phi.
    # y should be 1 or -1 as classified by the weight vector.
    # IMPORTANT: In the case that the score is 0, y should be set to 1.

    # Note that the weight vector can be arbitrary during testing.
    def generateExample() -> Tuple[Dict[str, int], int]:
        # BEGIN_YOUR_CODE (our solution is 3 lines of code, but don't worry if you deviate from this)
        # raise Exception("Not implemented yet")
        phi = {feature: random.randint(0, 10) for feature in weights.keys()}
        score = dotProduct(phi, weights)
        y = 1 if score <= 0 else -1
        # END_YOUR_CODE
        return phi, y

    return [generateExample() for _ in range(numExamples)]


############################################################
# Problem 3d: character features


def extractCharacterFeatures(n: int) -> Callable[[str], FeatureVector]:
    '''
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces mapped to their n-gram counts.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that 1 <= n <= len(x).
    '''

    def extract(x: str) -> Dict[str, int]:
        # BEGIN_YOUR_CODE (our solution is 6 lines of code, but don't worry if you deviate from this)
        # raise Exception("Not implemented yet")
        text = x.replace(" ", "").replace("\t", "")
        i = 0
        features = {}
        while i + n < len(text):
            ngram = text[i:i + n]
            features[ngram] = features.get(ngram, 0) + 1
            i += 1
            pass
        return features
        # END_YOUR_CODE

    return extract


############################################################
# Problem 3e:




############################################################
# Problem 5: k-means
############################################################


def kmeans(examples: List[Dict[str, float]], K: int,
           maxEpochs: int) -> Tuple[List, List, float]:
    '''
    Perform K-means clustering on |examples|, where each example is a sparse feature vector.

    examples: list of examples, each example is a string-to-float dict
    representing a sparse vector.
    K: number of desired clusters. Assume that 0 < K <= |examples|.
    maxEpochs: maximum number of epochs to run
    (you should terminate early if the algorithm converges).
    Return: (length K list of cluster centroids,
            list of assignments (i.e. if examples[i] belongs to centers[j],
            then assignments[i] = j),
            final reconstruction loss)
    '''
    # BEGIN_YOUR_CODE (our solution is 28 lines of code, but don't worry if you deviate from this)
    # raise Exception("Not implemented yet")
    centers = []
    assignments = []
    totalCost = 0

    centers = [examples[random.randint(0, len(examples) - 1)]
               for k in range(K)]

    def dist(x, center):
        return math.sqrt(sum([(x[key] - center[key]) ** 2 for key in x.keys()]))

    for epoch in range(maxEpochs):
        totalCost = 0
        assignments = []
        for example in examples:
            chosen_center = 0
            best_dist = None
            j = 0
            for center in centers:
                curr_dist = dist(example, center)
                if best_dist is None or curr_dist < best_dist:
                    chosen_center = j
                    best_dist = curr_dist
                    totalCost += best_dist
                    pass
                j += 1
                pass
            assignments.append(chosen_center)
            pass

        old_center = [item for item in centers]
        centers = []
        for i in range(K):
            arr = []
            for j in range(len(assignments)):
                if assignments[j] == i:
                    arr.append(examples[j])
                    pass
                pass
            center = {}
            for key in arr[0].keys():
                center[key] = sum([item.get(key) for item in arr]) / len(arr)
                pass
            centers.append(center)
            pass
        if all([dist(centers[i], old_center[i]) < 1e-6 for i in range(K)]):
            break
        pass

    return centers, assignments, totalCost
    # END_YOUR_CODE

x1 = {'good':0, 'bad':0}
x2 = {'good':0, 'bad':1}
x3 = {'good':0, 'bad':2}
x4 = {'good':0, 'bad':3}
x5 = {'good':0, 'bad':4}
x6 = {'good':0, 'bad':5}
examples = [x1, x2, x3, x4, x5, x6]
centers, assignments, totalCost = kmeans(examples, 2, maxEpochs=10)

print(centers, assignments, totalCost)