"""
Append master DF with binding predictions from predictors:
 -NetMHC4
 -MixMHCpred
 -MHCflurry
"""
import pandas as pd
import os
from mhctools import MHCflurry, NetMHC4, MixMHCpred

#import data
df = pd.read_pickle('master_data.pkl')

seqs = df['peptide'].unique().tolist()
predList = [MHCflurry, NetMHC4, MixMHCpred]

def initAndPredict(predictor):
    # initialize predictor and return DF of predicted sequences
    predictor = predictor(alleles='A*02:01')
    preds = predictor.predict_peptides(seqs)
    return preds

for program in predList:
    f = initAndPredict(program)
    f.to_csv('binding_preds/'+str(program)+'_results.csv')
