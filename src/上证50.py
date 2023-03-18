import akshare as ak
import datetime 


# stock_zh_index_spot_df = ak.stock_zh_index_spot()
# print(stock_zh_index_spot_df)

# 历史行情数据 
# stock_zh_index_daily_df = ak.stock_zh_index_daily(symbol="sh000016")
# print(stock_zh_index_daily_df)

# stock_zh_index_daily_em_df = ak.stock_zh_index_daily_em(symbol="sh000016")
# print(stock_zh_index_daily_em_df)

#上证50成分股
# index_stock_cons_df = ak.index_stock_cons_sina(symbol="000016")
# print(index_stock_cons_df)

# 中证指数网站-成份股权重 - 按照权重来排序
# index_stock_cons_weight_csindex_df = ak.index_stock_cons_weight_csindex(symbol="000016")
# index_stock_cons_weight_csindex_df.to_excel("上证50成分股{}.xlsx".format(datetime.date.today()))
# print(index_stock_cons_weight_csindex_df.sort_values(by=['权重'], ascending=False))

# print(index_stock_cons_weight_csindex_df)
# 遍历成份股票
# index_stock_cons_weight_csindex_df = index_stock_cons_weight_csindex_df.reset_index() # make sure indexes pair with number of rows

stock_individual_info_em_df = ak.stock_individual_info_em(symbol="600036")
print(stock_individual_info_em_df)

# 获取招商银行前复权（sh600036） 2002-04-09(上市) - z
stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="600036", period="daily", start_date="20000101", end_date='22220907', adjust="qfq")
# stock_zh_a_hist_df.to_excel("招商银行600036-{}.xlsx".format(datetime.date.today()))
print(stock_zh_a_hist_df)