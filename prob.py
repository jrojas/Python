#discuss with mentor
import collections
import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt
%matplotlib inline


datainlesson =  [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(datainlesson)

print c

# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

#boxplot of data in lesson

print "Boxplot:"
plt.boxplot(datainlesson)
plt.show()

#histogram of data in lesson
plt.hist(x, histtype='bar')
plt.show()

# QQ-plot for the data in this lesson
plt.figure()
print "The normal data:"
normal_data = np.random.normal(datainlesson)   
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show() #this will generate the first graph
plt.figure()
print "The uniform data:"
uniform_data = np.random.uniform(datainlesson)   
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show() #this will generate the second graph
