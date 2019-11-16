import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('power.csv', parse_dates=['Date'])  # parse_dates=['Date'] to recognize dates
# print(data)
data = data.set_index('Date')
print(plt.style.available)
plt.style.use('fivethirtyeight')
graph, ax = plt.subplots()
data.loc['2017', 'Consumption'].plot() # consumption against 2017
ax.set_xlabel("period")
ax.set_ylabel("Consumption in GWh")
plt.show()

graph, ax = plt.subplots()
data.loc['2017', ['Consumption','Solar']].plot() # consumption versus solar
ax.set_xlabel("period")
ax.set_ylabel("Consumption in GWh")
plt.show()

graph, ax = plt.subplots()
data.loc['2017-12', ['Consumption','Solar']].plot() # consumption against 2017 december
ax.set_xlabel("period")
ax.set_ylabel("Consumption in GWh")
plt.show()

graph, ax = plt.subplots()
data.loc['2015-01-01':'2017-10-01', ['Consumption','Solar']].plot()  # consumption from 2015 jan to 2017 october
ax.set_xlabel("period")
ax.set_ylabel("Consumption in GWh")

plt.show()
graph.savefig('power.png') #  saving the graph

# install skilearn
# anaconda