# CSV2PLSDA
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: PREFIX
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that converts abundance data into data that can
be differentially analyzed by PLS-DA.

The plugin accepts as input a tab-delimited parameter file of
keyword value pairs:
normabund: Normalized abundances (input)
metadata: Samples and groups (input)
samples: PLSDA-compatible samples file (output)
categories: Category that each sample falls into (output)
observables: Values to use for differential analysis
targets: Unique groups

All output files are prefixed by the user-specified output PREFIX.
