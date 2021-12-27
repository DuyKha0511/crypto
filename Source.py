import GetBitcoinPriceHourly
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from matplotlib.animation import FuncAnimation

directorCSV = 'C:/Users/PC/OneDrive/Desktop/KHDL/BitcoinPriceHourly.csv'
df = GetBitcoinPriceHourly.getBitcoinPriceHourly(numOfSamples=1000)
df.to_csv(directorCSV, index=False)


df = pd.read_csv(directorCSV)
for time in range(len(df['time'])):
    df['time'][time] = GetBitcoinPriceHourly.getLocalTimeFromTimestamp(
        df['time'][time])
print(df['time'][0])
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot('time', 'open', data=df)
ax.xaxis.set_major_formatter(mpl_dates.DateFormatter('%d %b %Y'))
ax.set_xlim(df['time'][len(df['time']) - 1], df['time'][0])
fig.autofmt_xdate()
plt.title('Bitcoin Price Hourly')
plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.show()


# x_vals = []
# y_vals = []
# n = len(df['time']) - 1
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# def animate(i):
#     x_vals.append(df['time'][n - i])
#     y_vals.append(df['open'][n - i])
#     plt.cla()
#     ax.plot(x_vals, y_vals)
#     ax.xaxis.set_major_formatter(mpl_dates.DateFormatter('%d %b %Y'))
#     fig.autofmt_xdate()
# ani = FuncAnimation(plt.gcf(), animate, interval=1)
# plt.title('Bitcoin Price Hourly')
# plt.xlabel('Time')
# plt.ylabel('Price (USD)')
# plt.show()
