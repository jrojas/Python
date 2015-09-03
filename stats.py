import pandas as pd
import scipy.stats as stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines()
data = [i.split(', ') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

#creats floats
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#varibles
meanAlcohol = df['Alcohol'].mean() 
meanTobacco = df['Tobacco'].mean() 
medianTobacco =df['Tobacco'].median()
medianAlcohol =df['Alcohol'].median()
modeAlcohol =stats.mode(df['Alcohol']) 
modeTobacco =stats.mode(df['Tobacco']) 
varianceAlcohol = df['Alcohol'].var() 
varianceTobacco = df['Tobacco'].var() 
standardDeviationAlcohol= df['Alcohol'].std() 
standardDeviationTobacco= df['Tobacco'].std() 

#print values
print "The range for the Alcohol and Tobacco dataset is: %f and %f " % (rangeAlcohol, rangeTobacco)
print "The mean for the Alcohol and Tobacco dataset is: %f and %f " % (meanAlcohol, meanTobacco)
print "The median for the Alcohol and Tobacco dataset is: %f and %f " % (meanAlcohol, meanTobacco)
print "The mode for the Alcohol and Tobacco dataset is: %s and %s " % (modeAlcohol, modeTobacco)
print "The Variance for the Alcohol and Tobacco dataset is: %s and %s " % (varianceAlcohol, varianceTobacco)
print "The Standard Deviation for the Alcohol and Tobacco dataset is: %s and %s " % (standardDeviationAlcohol, standardDeviationTobacco)