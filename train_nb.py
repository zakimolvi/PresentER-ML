"""
Train naive bayes classifier on depleted peptide data.
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#import data / global vars
df = pd.read_csv('input.txt', sep='\t')

# feature extraction: peptide -> vector
vectorizer = CountVectorizer(analyzer='char_wb', ngram_range=(2,3))
corpus = df['peptide']
X = vectorizer.fit_transform(corpus)

clf = MultinomialNB().fit(X, norm)

new_peptides = ['SLLMWITQC', 'RMFPNAPYL', 'RQASPLVHR', 'SLMMMMLLL']
X_predict = vectorizer.transform(new_peptides)
y_new = clf.predict(X_predict)

#ngram vals
xaxis = list(vectorizer.vocabulary_.keys())
yaxis = list(vectorizer.vocabulary_.values())
