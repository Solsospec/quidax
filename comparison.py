import requests
import time

n = 1000

# Kucoin
a_b = 0
i_r = 0

# Coinbase
c_d = 0
pri_ce = 0

# OKX
e_f = 0
okx_price = 0

# MEXC
i_j = 0
mexc_price = 0

# HTX (Huobi)
m_n = 0
htx_price = 0

# Binance
o_p = 0
binance_price = 0

# Bybit
q_r = 0
bybit_price = 0

for i in range(n):
    # Kucoin
    a = time.time()
    ir = "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=AAVE-USDT"
    r = requests.get(ir).json()["data"]["price"]
    ir = float(r)
    b = time.time() - a
    i_r += ir
    a_b += b

    # Coinbase
    c = time.time()
    url = "https://api.coinbase.com/v2/prices/AAVE-USDT/spot"
    response = requests.get(url)
    data = response.json()["data"]["amount"]
    price = float(data)
    d = time.time() - c
    pri_ce += price
    c_d += d

    # OKX
    e = time.time()
    okx_url = "https://www.okx.com/api/v5/market/ticker?instId=AAVE-USDT"
    okx_resp = requests.get(okx_url).json()
    okx_val = float(okx_resp["data"][0]["last"])
    f = time.time() - e
    okx_price += okx_val
    e_f += f

    # MEXC
    i1 = time.time()
    mexc_url = "https://api.mexc.com/api/v3/ticker/price?symbol=AAVEUSDT"
    mexc_resp = requests.get(mexc_url).json()
    mexc_val = float(mexc_resp["price"])
    j = time.time() - i1
    mexc_price += mexc_val
    i_j += j

    # HTX (Huobi)
    m = time.time()
    htx_url = "https://api.huobi.pro/market/detail/merged?symbol=aaveusdt"
    htx_resp = requests.get(htx_url).json()
    htx_val = float(htx_resp["tick"]["close"])
    n1 = time.time() - m
    htx_price += htx_val
    m_n += n1

    # Binance
    o = time.time()
    binance_url = "https://api.binance.com/api/v3/ticker/price?symbol=AAVEUSDT"
    binance_resp = requests.get(binance_url).json()
    binance_val = float(binance_resp["price"])
    p = time.time() - o
    binance_price += binance_val
    o_p += p

    # Bybit
    q = time.time()
    bybit_url = "https://api.bybit.com/v5/market/tickers?category=spot&symbol=NGNUSDT"
    bybit_resp = requests.get(bybit_url).json()
    bybit_val = float(bybit_resp["result"]["list"][0]["lastPrice"])
    r = time.time() - q
    bybit_price += bybit_val
    q_r += r

# Compute averages
kucoin_avg_price = i_r / n
kucoin_avg_latency = a_b / n

coinbase_avg_price = pri_ce / n
coinbase_avg_latency = c_d / n

okx_avg_price = okx_price / n
okx_avg_latency = e_f / n

mexc_avg_price = mexc_price / n
mexc_avg_latency = i_j / n

htx_avg_price = htx_price / n
htx_avg_latency = m_n / n

binance_avg_price = binance_price / n
binance_avg_latency = o_p / n

bybit_avg_price = bybit_price / n
bybit_avg_latency = q_r / n

# Print results
print(f"Kucoin: {kucoin_avg_price} -- {kucoin_avg_latency}\n")
print(f"Coinbase: {coinbase_avg_price} -- {coinbase_avg_latency}\n")
print(f"OKX: {okx_avg_price} -- {okx_avg_latency}\n")
print(f"MEXC: {mexc_avg_price} -- {mexc_avg_latency}\n")
print(f"HTX: {htx_avg_price} -- {htx_avg_latency}\n")
print(f"Binance: {binance_avg_price} -- {binance_avg_latency}\n")
print(f"Bybit: {bybit_avg_price} -- {bybit_avg_latency}\n")

print(f"\nKucoin/Coinbase Latency Ratio: {kucoin_avg_latency / coinbase_avg_latency}")
print(f"OKX/Coinbase Latency Ratio: {okx_avg_latency / coinbase_avg_latency}")
print(f"MEXC/Coinbase Latency Ratio: {mexc_avg_latency / coinbase_avg_latency}")
print(f"HTX/Coinbase Latency Ratio: {htx_avg_latency / coinbase_avg_latency}")
print(f"Binance/Coinbase Latency Ratio: {binance_avg_latency / coinbase_avg_latency}")
print(f"Bybit/Coinbase Latency Ratio: {bybit_avg_latency / coinbase_avg_latency}")