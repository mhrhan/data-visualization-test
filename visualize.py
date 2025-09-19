import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

plt.plot(data["Year"], data["Value"])
plt.xlabel("Year")
plt.ylabel("Value")
plt.title("Example Line Chart")
plt.show()
