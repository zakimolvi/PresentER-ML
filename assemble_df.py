"""
Prepre long-form document of PresentER screen data. For each donor, take the difference between .TCR and .UNTD and assemble in longform doc, save to directory.

input.txt is a wide-form tsv with the following columns: peptide	psuedo.1G4.don1	psuedo.UNTD.don1	psu.frac.TCR.don1	psu.frac.UNTD.don1	psuedo.1G4.don2	psuedo.UNTD.don2	psu.frac.TCR.don2	psu.frac.UNTD.don2	psuedo.1G4.don3	psuedo.UNTD.don3	psu.frac.TCR.don3	psu.frac.UNTD.don3	P.value	FC.don1	FC.don2	FC.don3	Log2FC.don1	Log2FC.don2	Log2FC.don3	avg.log2FC	neg.log10.pval
"""

import pandas as pd

#import data
df = pd.read_csv('input.txt', sep='\t') 
prefix = 'psu.frac'
group = ['.TCR', '.UNTD']
donors = ['.don1', '.don2', '.don3']

return_df = pd.DataFrame()
for don in donors:
    tcr = df[prefix+group[0]+don]
    untd = df[prefix+group[1]+don]
    diff = untd/tcr
    joint = pd.DataFrame()
    joint['peptide'] = df['peptide']
    joint['ID'] = don[1:]
    joint['diff'] = diff
    return_df = return_df.append(joint)
return_df['pepnum'] = return_df.index
return_df = return_df.reset_index(drop=True)

return_df.to_pickle('master_data.pkl')
return_df.to_csv('master_data.csv')
