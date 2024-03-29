from scipy.stats import chi2_contingency, ttest_ind
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class Contengency_Table:
    def __init__(self, df, outcome, var):
        self.cont_table = pd.crosstab(df[var], df[outcome], margins=True)
        self._var = var
        self._outcome = outcome
    def chi_squared_test(self):
        chi2, p, dof, ex = chi2_contingency(self.cont_table)
        print(self._var,': p-value of chisquare test =', p)
    def barplot(self):
        sns.set_theme(style="whitegrid")
        k=pd.melt(self.cont_table.drop("All", axis=0).reset_index().drop("All", axis = 1), id_vars = [self._var])
        k[self._var] = k[self._var].astype("category")
        return sns.barplot(x=self._var, y = "value", hue=self._outcome, data=k)   