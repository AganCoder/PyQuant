import matplotlib.pyplot as plt
import akshare as ak
import datetime

index_stock_cons_df = ak.index_stock_cons_sina(symbol="000016")

today = datetime.datetime.today()

# 60个工作日最少需要三个月，一个月有效时间只有22-23天，节假日时间更长
delta = datetime.timedelta(days=100)
end = today.strftime("%Y%m%d")
start = (today - delta).strftime("%Y%m%d")

for index, row in index_stock_cons_df.iterrows():
    name, code = row['name'], row['code']
    df = ak.stock_zh_a_hist(symbol=code, period="daily", start_date=start, end_date=end, adjust="qfq")
    # 计算移动平均线 MA5, MA10, MA20, MA60， 并且加入到对应的表格
    df['MA5']=df['收盘'].rolling(window=5).mean()
    df['MA10']=df['收盘'].rolling(window=10).mean()
    df['MA20']=df['收盘'].rolling(window=20).mean()
    df['MA60']=df['收盘'].rolling(window=60).mean()
    # df.to_excel("{}-{}.xlsx".format(name, code))

    todayData = df.loc[len(df)-1]
    if( todayData['收盘'] > todayData['MA60'] ):
        # round 并不精准，但是对我们来说已经够了
        print("{}-{} 收盘价({}) > MA60({}) - http://quote.eastmoney.com/sh{}.html#fullScreenChart".format(name, code, todayData['收盘'], round(todayData['MA60'], 2), code))
    



