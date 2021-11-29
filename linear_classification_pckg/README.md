# Library for Linear Classification Project
This library contains Python functions and classes for solving the linear classification project. It is distributed in different folders according to the functionality of each class/function. You will find the following functions: 

* *Mult_Violin_Plot(data, outcome, varlist)* This function is useful for generating multiple violin plots in the Exploratory Data Analysis Section.
* *plot_cf_matrix(cm, classes, normalize=False, 
                 title='Confusion matrix', cmap=plt.cm.Blues)*

  Useful function for creating Confussion Matrix Plots in order to test models accurracy. 


* *class Contengency_Table* The objective of this class is to allow user to analyze categorical variables and the relationship among them. In this class you will also find methods to make a Chi-Squared test and to plot barplots. 

* *roc_auc_plot(pred_probs, y_true)* This function allows to create ROC - AUC plots. 

* *reweight(pi,q1=0.5,r1=0.5)* This function reweights probabilities obtained from a Logistic Regression Model trained using an class-imbalanced binary model. 

* *reweight_multiclass(classes, probs, rj)* This function reweights probabilities obtained from a Logistic Regression Model trained using an class-imbalanced multiclass model. 
