import seaborn as sns
import matplotlib.pyplot as plt

def Mult_Violin_Plot(data, outcome, varlist):
    sns.set_theme(style="whitegrid")
    # Iterate over variables in a list and create scatterplots for numerical variables and violinplots for categorical 
    plt.figure(figsize=(17,20))
    for i, var in enumerate(varlist):
        plt.subplot(5, 2, i+1)
        sns.violinplot(x = outcome, y = var, data = data)
        plt.title("Violin Plot of " +  outcome + " vs. " + var)
        #legend_labels, _= ax.get_legend_handles_labels()
    
    return plt.tight_layout()