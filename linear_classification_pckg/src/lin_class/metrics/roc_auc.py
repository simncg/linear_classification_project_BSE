import matplotlib.pyplot as plt 
from sklearn.metrics import roc_curve, auc

def roc_auc_plot(pred_probs, y_true):
    sns.set_theme(style="whitegrid")
    fpr, tpr, _ = roc_curve(y_true, pred_probs)  #compute FPR/TPR
    auc_baseline = auc(fpr, tpr) # compute AUC
    plt.subplots(figsize=(10, 6))
    plt.plot(fpr, tpr, "b-", label="ROC Curve (AUC={:2.2f})".format(auc_baseline))
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(fontsize=15)
    plt.plot([0,1], [0,1], "r--")
    plt.title("ROC curve")

    