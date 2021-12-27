import apikey
import requests
import time
import pandas as pd
import matplotlib.pyplot as plt

i = 1
numOfSamples = 10

# while i < numOfSamples:
#     response = requests.get(
#         'https://api.coindesk.com/v1/bpi/currentprice.json')
#     print(str(i)+": "+str(response.json()))
#     time.sleep(5)
#     i += 1

headers = {
    'X-CMC_PRO_API_KEY': apikey.key,
    'Accepts': 'application/json'
}

params = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
qtyofcoin = 1  # số lượng đồng xu
samples = 1  # số mẫu

df = pd.DataFrame(columns=['Time', 'Price', 'volume_24h',
                  'percent_change_1h', 'percent_change_24h'])  # tạo dataFrame
while samples < 2:
    json = requests.get(url, params=params, headers=headers).json()
    print('Sample: '+str(samples)+': ')
    coins = json['data']
    for i in coins:
        if (i['name'] == "Bitcoin"):
            print(i)
            print(i['name'], 'Price: ' + str(i['quote']['USD']['price']), 'volume_24h: '+str(i['quote']['USD']['volume_24h']),
                  'percent_change_1h: ' +
                  str(i['quote']['USD']['percent_change_1h']),
                  'percent_change_24h: '+str(i['quote']['USD']['percent_change_24h']))
            df = df.append({'Time': i['quote']['USD']['last_updated'],
                            'Price': i['quote']['USD']['price'],
                           'volume_24h': i['quote']['USD']['volume_24h'],
                            'percent_change_1h': i['quote']['USD']['percent_change_1h'],
                            'percent_change_24h': i['quote']['USD']['percent_change_24h']},
                           ignore_index=True)
            qtyofcoin += 1
    # time.sleep(10)
    samples += 1
    qtyofcoin = 1
print(df)

df.to_csv('C:/Users/PC/OneDrive/Desktop/KHDL/Bitcoin.csv', index=False)
df = pd.read_csv('C:/Users/PC/OneDrive/Desktop/KHDL/Bitcoin.csv')
# print(df)

plt.plot(df['Price'])
plt.ylabel('Price(USD)')
plt.xlabel('Samples')
plt.show()
