"""
We will annotate the protein sequences with as many physicochemical
properties as possible using biopython and combine it with the master_data.pkl
"""
import pandas as pd
from Bio.SeqUtils.ProtParam import ProteinAnalysis

#import data
df = pd.read_pickle('master_data.pkl') #original data
seqs = df['peptide'].unique().tolist()

#find all parameters
def analyzePeptide(seq):
    """
    Use biopython to calculate peptide parameters and return
    them for dframe initialization/annotation
    :param seq: 9-mer string
    :return: peptide features as a list
    """
    anlyz = ProteinAnalysis(seq)
    mw = anlyz.molecular_weight()
    aroma = anlyz.aromaticity()
    iso = anlyz.isoelectric_point()
    secstruc = anlyz.secondary_structure_fraction()
    gravy = anlyz.gravy()

    return [mw, aroma, iso, secstruc, gravy]

#analyze and assemble
chemo = df['peptide'].map(analyzePeptide)
new_df = pd.DataFrame(chemo.values.tolist(), columns = ['mw', 'aromaticity', 'isoelectric', 'secstruc', 'gravy'])
df_final = df.join(new_df)
df_final.to_csv('master_aaAnnotation.csv')
df_final.to_pickle('master_aaAnnotation.pkl')

#plot mw-FC scatter
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set()

f = sns.scatterplot(x='mw', y='diff', hue='ID', data=df_final, palette='pastel', edgecolor='k')

for donor in df_final.ID.unique().tolist():
    donor_df = df_final[df_final['ID'] == donor]
    for i in range(len(donor_df)):
        if donor_df.iloc[i]['diff'] > 100:
            txt = donor_df.iloc[i]['peptide']
            f.annotate(txt,
                        (donor_df.iloc[i]['mw']-np.random.randint(4, 20), #random jitter
                         donor_df.iloc[i]['diff']+np.random.randint(4, 20)),
                        fontsize='xx-small', annotation_clip=False,
                        horizontalalignment='right',
                        stretch='semi-condensed',
                        verticalalignment='top'
                        )
f.plot()
plt.savefig("scatter/diff-mw_scatter.png", dpi=300)
