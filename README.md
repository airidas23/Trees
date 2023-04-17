## Decision Tree and Random Forest Models Comparison for Loan Category Prediction
In this report, we compare the performance of decision tree and random forest models for predicting loan categories based on the dataset found at https://www.kaggle.com/datasets/laotse/credit-risk-dataset. The report covers the model construction, testing, comparison results, and conclusions.

The main activities and tasks involved are:

#### Dataset Preparation

Select dataset for the decision tree model.
Derive decision tree output based on the predicted attribute (categorical variable with cardinality between 4 and 10).
Split dataset into training and testing subsets.
Divide data into input and output features.
Decision Tree and Random Forest Model Creation

#### Construct a decision tree using the training dataset.

Visually represent the resulting decision tree.
Test the constructed decision tree using testing data and calculate prediction accuracy/error.
Experimentally measure accuracy by changing the maximum tree depth.
Form a random forest with 5 trees using the same training and testing data distribution.
Determine the best results by changing the number of trees in the forest [3-9].
Model Comparison and Result Analysis

#### Compare the results of the initial decision tree and random forest.

Provide a confusion matrix.
Describe the results of the models and draw conclusions about each model's performance and their differences.
Calculate error metrics (e.g., MAE, MSE, etc.).
Present experimental results in the report, such as graphical representations, tables with results, and decision tree fragments to better understand and evaluate the models.
Provide recommendations based on the obtained results for model selection and its practical application.

# Conclusions
In this work, decision tree and random forest models were compared by applying them to a dataset. Based on the conducted study, it can be concluded that the random forest achieved slightly lower accuracy in predicting the loan category compared to the decision tree.

The visually represented decision tree helped to understand how the model makes decisions based on the dataset. It was also determined that constructing the decision tree model by changing the maximum tree depth can help achieve even better results.

It can be concluded that the random forest is a more effective model in this dataset compared to the decision tree, as it achieved higher accuracy and lower errors.

It is important to note that the model results may differ depending on the data distribution, as well as the choice of model parameters. This model can be improved by conducting additional experiments with other data variables to verify the effectiveness of these models in different situations.
