import requests
import datetime
import pytz


def main():
	count = 1
	counter = 1
	thresh = 50.00001
	desire = 249.99999
	multiplier = 0.99945
	
	while True:
		state = "   YES!" if count > 1 else ""
		print(f"Running... {counter}{state}")

		try:
			c_1 = coinbase(multiplier)
			q = qdx()
			c_2 = coinbase(multiplier)
			c = c_1 - c_2
			diff = c_2 - q
		
			if c < thresh and diff > desire:
				if count == 1:
					fill(count, diff, rec())
										
				else:
					with open("difference.txt", "r") as file:
						lines = file.readlines()
					d = float(lines[1])
							
					if d > diff:
						pass
								
					else:
						period = rec()
						fill(count, diff, period)

				count += 1
		
		except Exception as e:
			print(f"\nAn error occurred: {e}\n")
			continue
			
		counter += 1


def coinbase(multiplier):
	url = "https://api.coinbase.com/v2/prices/BTC-USDC/spot"
	response = requests.get(url, timeout=0.3)
	data = response.json()["data"]["amount"]
	price = float(data) * multiplier
	return price


def qdx():
	url = "https://www.quidax.com/api/v1/markets/btcusdt/order_book"
	response = requests.get(url, timeout=0.5)
	order = response.json()["data"]["asks"][0]["price"]
	return float(order)
	

def fill(count, diff, period):
	alert = f"{count}\n{diff}\n{period}"
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
		'text': f"📢 Price Alert:\n{message}"
	}

	try:
		response = requests.post(url, data=payload)
		response.raise_for_status()
	except Exception as e:
		pass
	

if __name__ == "__main__":
	main()