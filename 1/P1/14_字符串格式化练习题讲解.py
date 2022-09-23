
name = "传智播客"
stock_price = 19.99
stock_code = "003032"

#股票 价格 每日 增长 因子
stock_price_daily_growth_factor = 1.2
growth_days = 7

finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
print(f"公司: {name}, 股票代码: {stock_code},当前股价: {stock_price}")
print("每日增长系数: %.1f， 经过%d天的增长后，股价达到了: %.2f" % (stock_price_daily_growth_factor, growth_days, finally_stock_price))

# 公司: 传智播客, 股票代码: 003032,当前股价: 19.99
# 每日增长系数: 1.2， 经过7天的增长后，股价达到了: 71.63

