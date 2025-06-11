import requests
import datetime
import pytz
import math
from time import time


def main():
	count = counter = 1
	multiplier = 0.99965
	
	sell = 307.4467
	buy = 306.2193
	
	step = 0.00005
	
	calc = (1 / math.pow(0.999, 2)) * (math.sqrt(sell / buy))
	
	fees = round(calc if round(calc / step) * step == calc else math.ceil(calc / step) * step, 5)

	coin = "AAVE"
	last_day = get_day_number()
	
	while True:
		state = "   YES!" if count > 1 else ""
		print(f"Running... {counter}{state}")
		
		current_day = get_day_number()
		if current_day > last_day:
			count = 1
			counter = 0
			bot()
			last_day = current_day

		try:
			c_1 = coinbase(multiplier, coin)
			q = qdx(coin)
			c_2 = coinbase(multiplier, coin)
			
			c = c_1 - c_2
			diff = c_2 - q
			c_q = c_2 / q
			thresh = c_2 * 0.0005 
			gain = c_q / fees
			
			counter += 1
		
			if c < thresh and gain > 1:
				bot(count, diff, rec(), c_2, q, gain)
				count += 1
		
		except Exception as e:
			print(f"\nAn error occurred: {e}\n")
			counter = 1 if not counter else counter


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
	
	
def bot(*args):
	BOT_TOKEN = '7553627722:AAHmqifeMpb1zdAe2tnFB7PO2YKJEk_IVJE'
	CHAT_ID = '1090646144'

	url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
	
	if args:
		count, diff, period, cbs, q, gain = args
		payload = {
			'chat_id': CHAT_ID,
			'text': f"📢 PRICE ALERT!\n\nOccurrences: {count}\nPrice difference: {diff}\nPeriod: {period}\nCoinbase price: {cbs}\nQuidax price: {q}\nGain: {gain}"
		}
		
	else:
		hyph = "-" * 30
		payload = {
			'chat_id': CHAT_ID,
			'text': f"{hyph}\n{' ' * 17}NEW DAY!!!\n{hyph}"
		}

	try:
		response = requests.post(url, data=payload)
		response.raise_for_status()
	except Exception:
		pass


def get_day_number():
	return (time() + 3600) // 86400


if __name__ == "__main__":
	main()
