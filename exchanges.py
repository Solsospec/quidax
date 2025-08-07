import requests
import time

n = 100

# MEXC
i_j = 0
mexc_price = 0

# HTX (Huobi)
m_n = 0
htx_price = 0

for i in range(n):
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

# Compute averages
mexc_avg_price = mexc_price / n
mexc_avg_latency = i_j / n

htx_avg_price = htx_price / n
htx_avg_latency = m_n / n

# Print results
print(f"MEXC: {mexc_avg_price} -- {mexc_avg_latency}\n")
print(f"HTX: {htx_avg_price} -- {htx_avg_latency}\n")

ratio = mexc_avg_latency / htx_avg_latency
print(f"MEXC/HTX Latency Ratio: {ratio}")
print(f"\nWinner: {'HTX' if ratio > 1 else 'MEXC' }")