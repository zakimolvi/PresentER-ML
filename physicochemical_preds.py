"""
Script to combine peptide physicochemical properties with peptide HLA binding predictions

Produces joint_everything.pkl and .csv
"""
import pandas as pd
import os

# set vars
df1 = pd.read_pickle('master_aaAnnotation.pkl')
dir = 'binding_preds/'
pred_files = os.listdir(dir) #list of CSVs in dir
base = pd.DataFrame(columns=['peptide'])
base['peptide'] = df1['peptide']

#combine binding preds into one DF
for file in pred_files:
    pred = pd.read_csv(dir+file)
    method = pred.prediction_method_name[0] + ' %rank'
    pred = pred[['peptide', 'percentile_rank']]
    pred = pred.rename(columns={"percentile_rank": method})
    print(pred)
    base = base.merge(pred, on='peptide')
print(base)

# combine base with df1
base = base.merge(df1)
base.to_pickle('joint_everything.pkl')
base.to_csv('joint_everything.csv')
