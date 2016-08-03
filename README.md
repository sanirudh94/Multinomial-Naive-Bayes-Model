# Multinomial-Naive-Bayes-Model
##Hotel Reviews Classifier##
The aim of the project is to program a Naive Bayes Classifier as a 4-class single classification problem to identify the hotel reviews as either **truthful** or **deceptive** and either **positive** or **negative**. The word tokens are used as features for classification. **Laplace smoothing** is applied for smoothing of data and handling the unknown vocabulary in the test data. The solution uses add-one smoothing on the transition probabilities and no smoothing on the emmission probabilities; for unknown tokens in the test data it will ignore the emmission probabilities and use the transition probabilities alone.

#Pre-requisites
* Python 3.0 or above(recommended)
* Latest version of PyCharm installed

#Data description
```
$ A top level directory with two sub-directories, one for positive and another for negative reviews
$ Each of the subdirectories contain two-subdirectories , one with truthful reviews and one with deceptive reviews
$ Each of these sub-directories contain 4 sub-directories called "folds"
$ Each of the folds contains 80 text files with English text(one review per file)
```
#Files description
* **nblearn.py** :- The program will learn a Naive Bayes Model and write the model parameters to the file called nbmodel.txt
* **nbclassify.py** :- The program will read the parameters of a Naive Bayes model from nbmodel.txt, classify each file in the test data and write the results to a text file called nboutput.txt in the format **label_a label_b path** where label_a is either **"truthful or deceptive"**, label_b is either **"positive or negative"**

#Evaluation
The model is trained on all the folds and then tested on a new set of data and F1 score is calculated


