from string import Template
import apikey
import requests
import time
import pandas as pd
import matplotlib.pyplot as plt
from datetime import timezone
import datetime


# format: Local time: yyyy-mm-dd hh:mm:ss
datetimeBegin = '2021-01-01 00:00:00'
datetimeEnd = datetime.datetime.now()


def getLocalTimeFromTimestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)


def getUTCTimeFromTimestamp(timestamp):
    return datetime.datetime.fromtimestamp(timestamp - 7*3600)


def getUTCTimestampFromLocalTime(localDatetime):
    try:
        localDatetime = datetime.datetime.strptime(
            localDatetime, '%Y-%m-%d %H:%M:%S')
        return int(localDatetime.replace(tzinfo=timezone.utc).timestamp())
    except:
        return int(localDatetime.replace(tzinfo=timezone.utc).timestamp())


def getBitcoinPriceHourly(datetimeBegin=datetimeBegin, datetimeEnd=datetime.datetime.now(), numOfSamples=1000):
    # Get Timestamp from UTCTime
    timestampBegin = str(getUTCTimestampFromLocalTime(datetimeBegin))
    timestampEnd = str(getUTCTimestampFromLocalTime(datetimeEnd))

    # Get URL bitcoin price hourly
    website = Template(
        'https://markets.api.bitcoin.com/ohlc/hourly?symbols=BTC&quotes=USD&tFrom=$timestampBegin&tTo=$timestampEnd&expand=true')
    url_API = website.substitute(timestampBegin=timestampBegin,
                                 timestampEnd=timestampEnd)

    # Create DataFrame to save Data
    details = ['time', 'open', 'close', 'high', 'low',
               'volumn_open', ' volumn_close', 'volumn_high', 'volumn_low']
    df = pd.DataFrame(columns=[details[0], details[1], details[2], details[3]])

    # Get Data from URL
    json = requests.get(url_API).json()['data']['BTC']['USD']['history']
    numOfCrawledData = len(json)
    sample = 0
    while sample < numOfSamples and sample < numOfCrawledData:
        df = df.append({df.columns[0]: str(json[sample][df.columns[0]]),
                        df.columns[1]: json[sample][df.columns[1]],
                        df.columns[2]: json[sample][df.columns[2]],
                        df.columns[3]: json[sample][df.columns[3]]},
                       ignore_index=True)
        sample += 1
    return df
