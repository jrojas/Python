import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

%matplotlib inline
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

cleanInterestRate = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
loansData['Interest.Rate'] = cleanInterestRate

cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
loansData['Loan.Length']=cleanLoanLength

cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))
cleanFICORange = cleanFICORange.map(lambda x: [int(n) for n in x])
loansData['FICO.Range']=cleanFICORange
loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: [int(n) for n in x][0])


intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
#put the two columns together to create an input matrix 
x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

f.summary()
