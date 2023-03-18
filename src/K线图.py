# 加载取数与绘图所需的函数包
import pandas as pd
import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import akshare as ak
import datetime 

mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


# 获取数据
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="600036", period="daily", start_date="20000101", end_date='22220907', adjust="qfq")

# 获取指定的列
df = stock_zh_a_hist_df[['日期','开盘','最高','最低','收盘']]

# 将日期作为索引，增加效率
df.set_index('日期', inplace=True)

# 计算移动平均线 MA5, MA10, MA20, MA60， 并且加入到对应的表格
df['MA5']=df['收盘'].rolling(window=5).mean()
df['MA10']=df['收盘'].rolling(window=10).mean()
df['MA20']=df['收盘'].rolling(window=20).mean()
df['MA60']=df['收盘'].rolling(window=60).mean()

# 绘制 K 线以及移动均线

# 绘制均线
plt.plot(range(len(df)), df['MA5'], color='blue', lw=1, label='MA(5)')
plt.plot(range(len(df)), df['MA10'], color='yellow', lw=1, label='MA(10)')
plt.plot(range(len(df)), df['MA20'], color='fuchsia', lw=1, label='MA(20)')
plt.plot(range(len(df)), df['MA60'], color='green', lw=1, label='MA(60)')

plt.show()


# fig = plt.figure(figsize=(12,10))
# grid = plt.   (12, 10, wspace=0.5, hspace=0.5)
 
#（1）绘制K线图
# K线数据
# ohlc = df[['日期','开盘','最高','最低','收盘']]

# ohlc.loc[:,'日期'] = range(len(ohlc))     # 重新赋值横轴数据，绘制K线图无间隔
# # 绘制K线
# ax1 = fig.(grid[0:8,0:12])   # 设置K线图的尺寸
# candlestick_ohlc(ax1, ohlc.values.tolist(), width=.7
#                  , colorup='red', colordown='green')
# # # （2）绘制均线
# ax1.plot(range(len(data_price)), data_price['MA5']
#          , color='red', lw=2, label='MA (5)')
# ax1.plot(range(len(data_price)), data_price['MA10']
#          , color='blue', lw=2, label='MA (10)')
# ax1.plot(range(len(data_price)), data_price['MA20']
#          , color='green', lw=2, label='MA (20)')
# # 设置标注
# plt.title(stock_code,fontsize = 14)       # 设置图片标题
# plt.ylabel('价 格（元）',fontsize = 14)   # 设置纵轴标题
# plt.legend(loc='best')                    # 绘制图例
# ax1.set_xticks([])                        # 日期标注在成交量中，故清空此处x轴刻度
# ax1.set_xticklabels([])                   # 日期标注在成交量中，故清空此处x轴 

# #（3）绘制成交量
# # 成交量数据
# data_volume = data_price[['Date','close_price','open_price','business_amount']]
# data_volume['color'] = data_volume.apply(lambda row: 1 if row['close_price'] >= row['open_price'] else 0, axis=1)        # 计算成交量柱状图对应的颜色，使之与K线颜色一致
# data_volume.Date = ohlc.Date
# # 绘制成交量
# ax2 = fig.add_subplot(grid[8:10,0:12])  # 设置成交量图形尺寸
# ax2.bar(data_volume.query('color==1')['Date']
#         , data_volume.query('color==1')['business_amount']
#         , color='r')                    # 绘制红色柱状图
# ax2.bar(data_volume.query('color==0')['Date']
#         , data_volume.query('color==0')['business_amount']
#         , color='g')                    # 绘制绿色柱状图
# plt.xticks(rotation=30) 
# plt.xlabel('日 期',fontsize = 14)                               # 设置横轴标题
# # 修改横轴日期标注
# date_list = ohlc.index.tolist()           # 获取日期列表
# xticks_len = round(len(date_list)/(len(ax2.get_xticks())-1))      # 获取默认横轴标注的间隔
# xticks_num = range(0,len(date_list),xticks_len)                   # 生成横轴标注位置列表
# xticks_str = list(map(lambda x:date_list[int(x)],xticks_num))     # 生成正在标注日期列表
# ax2.set_xticks(xticks_num)                                        # 设置横轴标注位置
# ax2.set_xticklabels(xticks_str)                                   # 设置横轴标注日期
# plt.show()



