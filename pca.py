"""
PCA analysis of peptides taking into account physicochemical properties and binding predictions
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

df = pd.read_pickle('joint_everything.pkl')

#scale data
from sklearn.preprocessing import StandardScaler
features = ['mhcflurry %rank',
            'mixmhcpred %rank',
            'netMHC %rank',
            'mw',
            'aromaticity',
            'isoelectric', 'gravy']

#need to drop peptides that were not measured in a given donor (does not remove other donor's measurements)
dropIdx = df[df['diff'].isna()].peptide.index
df.drop(dropIdx, inplace=True)

#set depletion threshold and label peptides accordingly
def addLabel(val, threshold=150.00):
    # takes mRNA FC val and labels peptide as depleted or not depleted
    if val >= threshold:
        return "depleted"
    else:
        return "not depleted"
df['label'] = df['diff'].apply(addLabel)

# Separating out the features
x = df.loc[:, features].values
# Separating out the target
y = df.loc[:,['label']].values
# Standardizing the features
x = StandardScaler().fit_transform(x)

#pca project to 2D
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['pc1', 'pc2'])

finalDf = pd.concat([principalDf, df[['label']]], axis = 1)

#plot
data = finalDf[finalDf['label'] == 'not depleted']
sns.scatterplot(x='pc1', y='pc2', hue='label',
                data=data, alpha=0.4, edgecolor='k')
data = finalDf[finalDf['label'] == 'depleted']
sns.scatterplot(x='pc1', y='pc2', hue='label',
                data=data, alpha=1.0, edgecolor='k', palette='Set2')
plt.title('FC threshold = 150')
plt.savefig('pca_threshold150.png', dpi=300)
