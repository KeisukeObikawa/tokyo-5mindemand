import pandas as pd
import datetime as dt
import time

def job():
    url = 'https://www.tepco.co.jp/forecast/html/images/juyo-d-j.csv'
    df = pd.read_csv(url,encoding='shift-jis',skiprows=53)
    df['太陽光発電の割合（％）'] = round(df['太陽光発電実績(５分間隔値)(万kW)']/df['当日実績(５分間隔値)(万kW)']*100,1)
    now = dt.datetime.now()
    time = now.strftime('%Y%m%d-%H%M%S')
    df.to_csv('/Users/sejin/Documents/python-cron/output_{}.csv'.format(time), index=False, encoding='utf_8_sig')