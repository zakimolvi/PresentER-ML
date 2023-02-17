"""
Make quick pairplot to see if any feature is dominant
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='ticks')
df = pd.read_pickle('joint_everything.pkl')

#add label
def addLabel(val, threshold=150.00):
    # takes mRNA FC val and labels peptide as depleted or not depleted
    if val >= threshold:
        return "depleted"
    else:
        return "not depleted"
df['label'] = df['diff'].apply(addLabel)
df = df.drop('pepnum', axis=1)
sns.pairplot(df, hue='label', hue_order=['not depleted', 'depleted'], palette='pastel',
             plot_kws=dict(edgecolor="k"))
plt.savefig('pairplot.png', dpi=300)
