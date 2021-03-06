    #!/usr/bin/env python

"""
Naive bayes implementation in Python
Classifier Algorithm
"""

from datasets import load_loan_defaulters
from feature import ContinuousFeature
from feature import DiscreteFeature
from naive_bayes import NaiveBayes


def main():
    dataset = load_loan_defaulters()
    design_matrix = [row[:-1] for row in dataset]
    target_values = [row[-1] for row in dataset]
    clf = NaiveBayes(extract_features)
    clf.fit(design_matrix, target_values)
    prediction = clf.predict_record([1, 1, 50700])
    negation_word = " not " if prediction == 0.0 else ""
    print("testing negative sentiment" + negation_word + "of the tweet")


def extract_features(feature_vector):
    """Maps a feature vector to whether each feature is continuous or discrete."""
    return [
        DiscreteFeature(feature_vector[0]),
        DiscreteFeature(feature_vector[1]),
        ContinuousFeature(feature_vector[2])
    ]


if __name__ == '__main__':
    main()

        
   
        
    
        
        
        
