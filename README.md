# PresentER-ML
Prediction of TCR off-target peptides from [PresentER](https://pubmed.ncbi.nlm.nih.gov/32184297/) screen data.

## Requirements
- Python libraries: `pandas`, `biopython`, `seaborn`, `numpy`, `mhctools`
- Locally installed NetMHC4, MixMHCpred 

## Manifest
`assemble_df.py`: Reformats data from an investigator performing a PresentER screen in donor TCR-transduced T cells

`physicochemical_annotation.py`: Annotates each peptide with physicochemical properties (e.g. hydrophobicity, molecular weight, isoelectric point).
Produces example plot of PresentER depletion score (diff) vs. molecular weight (mw).
<p align="center">
<img src="diff-mw.png" height=50% width=50%>
</p>
