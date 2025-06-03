import requests
import datetime
import pytz
import math


def main():
	count = 1
	counter = 1
	thresh = 50.00001
	multiplier = 0.99925
	
	sell = 162.21
	buy = 161.39
	step = 0.00005
	
	calc = (1 / math.pow(0.999, 2)) * (math.sqrt(sell / buy))
	
	fees = round(calc if round(calc / step) * step == calc else math.ceil(calc / step) * step, 5)

	coin = "SOL"
	
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
		
			if c < thresh and c_q > fees:
				period = rec()
				if count == 1:
					fill(count, diff, period, c_2, c_q)
										
				else:
					with open("difference.txt", "r") as file:
						lines = file.readlines()
					cq = float(lines[4].split(" ")[-1])
							
					if cq > c_q:
						pass
								
					else:
						fill(count, diff, period, c_2, c_q)

				count += 1
		
		except Exception as e:
			print(f"\nAn error occurred: {e}\n")
			continue
			
		counter += 1


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
	

def fill(count, diff, period, cbs, ratio):
	alert = f"Occurrences: {count}\nPrice difference: {diff}\nPeriod: {period}\nCoinbase price: {cbs}\nRatio: {ratio}"
	with open("difference.txt", "w") as file:
		file.write(alert)
	bot(alert)
		

def rec():
	current_time = datetime.datetime.now(pytz.timezone('Africa/Lagos')).strftime('%Y-%m-%d %H:%M:%S')
	return current_time
	
	
def bot(message):
	BOT_TOKEN = '7977634075:AAEXNPYr2YMdJvmNUQFBOc1c_YWNdl1NOYs'
	CHAT_ID = '1090646144'

	url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
	payload = {
		'chat_id': CHAT_ID,
		'text': f"📢 PRICE ALERT!\n\n{message}"
	}

	try:
		response = requests.post(url, data=payload)
		response.raise_for_status()
	except Exception as e:
		pass
	

if __name__ == "__main__":
	main()