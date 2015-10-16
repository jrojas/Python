import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
%matplotlib inline

# load clead data
loansData = pd.read_csv('loansData_clean.csv')

#Interest Rate < 12%

#loansData['IR_TF'] = np.where(loansData['Interest.Rate']<0.12,'0','1')
loansData['IR_TF'] = loansData['Interest.Rate'].map(lambda i: i < 0.12)

#intercept column
loansData['Intercept'] = 1

#independent variables
ind_vars = ['FICO.Score','Amount.Requested','Intercept']



# Define the model
logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])

# fit model
result = logit.fit()

#Get the fitted coefficients from the results
coeff = result.params

print coeff


def logistic_function(coeff,fico,amount):
   
      p = 1/(1 + np.exp(-(coeff[2] + coeff[0]*fico + coeff[1]*amount)))
      return   p

# define pred function
def pred(coeff, fico, amount):
    p = logistic_function(coeff, fico, amount)
    if p >= 0.70:
        print('Loan Approved!')
    else:
        print('Loan Declined!')

    
fico = int(raw_input('Enter a FICO score:'))

amount = int(raw_input('Enter a Loan amount:'))


# execute prediction function
pred(coeff, fico, amount)
