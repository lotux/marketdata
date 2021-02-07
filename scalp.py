import yfinance as yf
data = yf.download("NIO", period = "1d",interval = "1m",prepost = True)
print(data)
# data.get
for col in data.columns:
    print(col)
for index, row in data.iterrows():
    print(row['Volume'], row['Open'])