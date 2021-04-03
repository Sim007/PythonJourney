# from https://www.w3schools.com/python/python_ml_getting_started.asp
# Machine Learning is making the computer learn from studying data and statistics.
# Machine Learning is a step into the direction of artificial intelligence (AI).
# Machine Learning is a program that analyses data and learns to predict the outcome.

# We can split the data types into three main categories:
#  Numerical
#  Categorical
#  Ordinal

# Mean Median Mode



import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Mean: average
x = numpy.mean(speed)
print("Mean   : ")
print(x)

# Median: value middle after sort
x = numpy.median(speed)
print("Median : ")
print(x)

# Mode: value with most counts
from scipy import stats
x = stats.mode(speed)
print("Mode  : ")
print(x)


