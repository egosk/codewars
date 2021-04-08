import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("iris.csv", delimiter='\t')


# 3. Write a Python program to create a Pie plot to get the frequency of the three species of the Iris data.

pie_plot = data['Species'].value_counts().plot.pie()
plt.show()