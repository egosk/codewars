# ML exercises from https://www.w3resource.com/machine-learning/scikit-learn/iris/index.php

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import sparse

# 1. Write a Python program to load the iris data from a given csv file into a dataframe and print the shape of the
# data, type of the data and first 3 rows.

data = pd.read_csv("iris.csv", delimiter='\t')
print('Data shape: ', data.shape)
print('Data type: ', type(data))
print('First 3 rows:\n', data[:3]) #data.head(3)

# 2. Write a Python program using Scikit-learn to print the keys, number of rows-columns, feature names and the
# description of the Iris data.

print('Keys: ', data.keys())
print('Number rows-columns: ', len(data), '-', len(data.columns))


# 3. Write a Python program to get the number of observations, missing values and nan values.

print('Number of observations, missing values, Nan values:')
print(data.info())
# data.isnull().values.any()
# data.isnull().sum()

# 4. Write a Python program to create a 2-D array with ones on the diagonal and zeros elsewhere. Now convert the
# NumPy array to a SciPy sparse matrix in CSR format.

eye = np.eye(5)
print(eye)
new_eye = sparse.csr_matrix(eye)
print('CSR:\n', new_eye)

# 5. Write a Python program to get observations of each species (setosa, versicolor, virginica) from iris data.

print('Number of samples per specie:')
print(data['Species'].value_counts())

# 6. Write a Python program to view basic statistical details like percentile, mean, std etc. of iris data.

print('Statistical details:')
print(data.describe())


# 7. Write a Python program to access first four columns from a given Dataframe using the index and column labels.

new_df = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
print(new_df)
new_df_2 = data.iloc[:, :4]
print(new_df_2)

