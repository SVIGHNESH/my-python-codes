import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("cities.csv")

main_data = df.iloc[:,:-1]
last_column = df.ioc[:,-1]

print(main_data)
print(last_column)

plt.scatter(main_data[:,0],main_data[:,1])
