import scipy.stats as stats
import collections
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

chi, p = stats.chisquare(freq.values())

print p
print chi