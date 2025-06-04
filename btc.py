import requests
import datetime
import pytz
import math


def main():
	count = 1
	counter = 1
	thresh = 50.00001
	multiplier = 0.99925
	
	sell = 105768
	buy = 105694
	step = 0.00005
	
	calc = (1 / math.pow(0.999, 2)) * (math.sqrt(sell / buy))
	
	fees = round(calc if round(calc / step) * step == calc else math.ceil(calc / step) * step, 5)

	coin = "BTC"
	
	while True:
		state = "   YES!" if count > 1 else ""
		print(f"Running... {counter}{state}")

		try:
			c_1 = coinbase(multiplier, coin)
			q = qdx(coin)
			c_2 = coinbase(multiplier, coin)
			c = c_1 - c_2
			diff = c_2 - q
			c_q = c_2 / q
			
			counter += 1
		
			if c < thresh and c_q > fees:
				bot(count, diff, rec(), c_2, c_q)
				count += 1
		
		except Exception as e:
			print(f"\nAn error occurred: {e}\n")


def coinbase(multiplier, coin):
	url = f"https://api.coinbase.com/v2/prices/{coin}-USDC/spot"
	response = requests.get(url, timeout=0.3)
	data = response.json()["data"]["amount"]
	price = float(data) * multiplier
	return price


def qdx(coin):
	url = f"https://www.quidax.com/api/v1/markets/{coin.lower()}usdt/order_book"
	response = requests.get(url, timeout=0.5)
	order = response.json()["data"]["asks"][0]["price"]
	return float(order)
		

def rec():
	current_time = datetime.datetime.now(pytz.timezone('Africa/Lagos')).strftime('%Y-%m-%d %H:%M:%S')
	return current_time
	
	
def bot(count, diff, period, cbs, ratio):
	BOT_TOKEN = '7977634075:AAEXNPYr2YMdJvmNUQFBOc1c_YWNdl1NOYs'
	CHAT_ID = '1090646144'

	url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
	payload = {
		'chat_id': CHAT_ID,
		'text': f"📢 PRICE ALERT!\n\nOccurrences: {count}\nPrice difference: {diff}\nPeriod: {period}\nCoinbase price: {cbs}\nRatio: {ratio}"
	}

	try:
		response = requests.post(url, data=payload)
		response.raise_for_status()
	except Exception as e:
		pass
	

if __name__ == "__main__":
	main()
