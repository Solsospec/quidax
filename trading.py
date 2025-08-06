import threading
from time import time, sleep
import requests
import datetime
import pytz
import math


# Shared stop event
stop_event = threading.Event()


# This thread will listen for "stop" input
def listen_for_stop():
    while not stop_event.is_set():
        user_input = input("Type 'stop' to quit:\n")
        if user_input.lower() == 'stop':
            stop_event.set()


# Simulations
class Aave:
    def __init__(self):
        pass # Placeholder
        
        
    def aave_main(self):
        count = counter = 1
        	
        sell = 307.4467
        buy = 306.2193
        	
        step = 0.00005
        	
        calc = (1 / math.pow(0.999, 2)) * (math.sqrt(sell / buy))
        	
        fees = round(calc if round(calc / step) * step == calc else math.ceil(calc / step) * step, 5)
        
        coin = "AAVE"
        last_day = self.get_day_number()
        	
        while True:
        	state = "   YES!" if count > 1 else ""
        	print(f"Running... {counter}{state}")
        		
        	current_day = self.get_day_number()
        	if current_day > last_day:
        		count = 1
        		counter = 0
        		self.bot()
        		last_day = current_day
        
        	try:
        		c_1 = self.coinbase(coin)
        		q = self.qdx(coin)
        		c_2 = self.coinbase(coin)
        			
        		c = c_1 - c_2
        		diff = c_2 - q
        		c_q = c_2 / q
        		thresh = c_2 * 0.0005 
        		gain = c_q / fees
        			
        		counter += 1
        		
        		if c < thresh and gain > 1:
                    self.bot(count, diff, self.rec(), c_2, q, gain)
                    count += 1
        		
        	except Exception as e:
        		print(f"\nAn error occurred: {e}\n")
        		counter = 1 if not counter else counter
        
        if stop_event.is_set():
            break
    
    def coinbase(self, coin):
        url = f"https://api.coinbase.com/v2/prices/{coin}-USDT/spot"
        response = requests.get(url, timeout=0.3)
        data = response.json()["data"]["amount"]
        price = float(data)
        return price
        
    
    def qdx(self, coin):
        url = f"https://www.quidax.com/api/v1/markets/{coin.lower()}usdt/order_book"
        response = requests.get(url, timeout=0.5)
        order = response.json()["data"]["asks"][0]["price"]
        return float(order)
        
    
    def rec(self):
        current_time = datetime.datetime.now(pytz.timezone('Africa/Lagos')).strftime('%Y-%m-%d %H:%M:%S')
        return current_time
        	
        	
    def bot(self, *args):
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
        
        
    def get_day_number(self):
        return (time() + 3600) // 86400
    
class Btc:
    def __init__(self):
        pass
        
        
    def btc_main(self):
        count = counter = 1
        thresh = 50.00001
        	
        sell = 105768
        buy = 105694
        step = 0.00005
        	
        calc = (1 / math.pow(0.999, 2)) * (math.sqrt(sell / buy))
        	
        fees = round(calc if round(calc / step) * step == calc else math.ceil(calc / step) * step, 5)
        
        coin = "BTC"
        last_day = self.get_day_number()
        	
        while True:
        	state = "   YES!" if count > 1 else ""
        	print(f"Running... {counter}{state}")
        		
        	current_day = self.get_day_number()
        	if current_day > last_day:
        		count = 1
        		counter = 0
        		self.bot()
        		last_day = current_day
        
        	try:
        		c_1 = self.coinbase(coin)
        		q = self.qdx(coin)
        		c_2 = self.coinbase(coin)
        		c = c_1 - c_2
        		diff = c_2 - q
        		c_q = c_2 / q
        		gain = c_q / fees
        			
        		counter += 1
        		
        		if c < thresh and gain > 1:
                    self.bot(count, diff, self.rec(), c_2, q, gain)
                    count += 1
        		
        	except Exception as e:
        		print(f"\nAn error occurred: {e}\n")
        		counter = 1 if not counter else counter
        
        if stop_event.is_set():
            break
    
    def coinbase(self, coin):
        url = f"https://api.coinbase.com/v2/prices/{coin}-USDT/spot"
        response = requests.get(url, timeout=0.3)
        data = response.json()["data"]["amount"]
        price = float(data)
        return price


    def qdx(self, coin):
        url = f"https://www.quidax.com/api/v1/markets/{coin.lower()}usdt/order_book"
        response = requests.get(url, timeout=0.5)
        order = response.json()["data"]["asks"][0]["price"]
        return float(order)
        		

    def rec(self):
        current_time = datetime.datetime.now(pytz.timezone('Africa/Lagos')).strftime('%Y-%m-%d %H:%M:%S')
        return current_time
        	
	
    def bot(self, *args):
        BOT_TOKEN = '7977634075:AAEXNPYr2YMdJvmNUQFBOc1c_YWNdl1NOYs'
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
        except Exception as e:
        	pass
        

    def get_day_number(self):
        return (time() + 3600) // 86400


class Btc_ngn:
    def __init__(self):
        pass
        
        
    def btc_ngn_main(self):
        count = counter = 1
        while True:
        		try:
        			converter = self.conversion()
        			break
        		except Exception as e:
        			print(f"Error: {e}\nRetrying the USDT/NGN converter...\n\n")
        			sleep(0.5)
        	
        sell = 173222
        	buy = 172530
        	step = 0.00005
        	
        	calc = (1 / math.pow(0.999, 2)) * (math.sqrt(sell / buy))
        	
        	fees = round(calc if round(calc / step) * step == calc else math.ceil(calc / step) * step, 5)
        
        	coin = "BTC"
        	last_day = self.get_day_number()
        	
        	while True:
        		state = "   YES!" if count > 1 else ""
        		print(f"Running... {counter}{state}")
        		
        		current_day = self.get_day_number()
        		if current_day > last_day:
        			count = 1
        			counter = 0
        			self.bot()
        			last_day = current_day
        
        		try:
        			converter = self.conversion() if counter % 600 == 0 else converter
        
        			c_1 = self.coinbase(coin, converter)
        			q = self.qdx(coin)
        			c_2 = self.coinbase(coin, converter)
        			
        			c = c_1 - c_2
        			diff = c_2 - q
        			c_q = c_2 / q
        			thresh = c_2 * 0.0005 
        			gain = c_q / fees
        			
        			counter += 1
        		
        			if c < thresh and gain > 1:
        				self.bot(count, diff, self.rec(), c_2, q, gain)
        				count += 1
        		
        		except Exception as e:
        			print(f"\nAn error occurred: {e}\n")
        			counter = 1 if not counter else counter
        
        if stop_event.is_set():
            break

    def coinbase(self, coin, converter):
        url = f"https://api.coinbase.com/v2/prices/{coin}-USDT/spot"
        response = requests.get(url, timeout=0.3)
        data = response.json()["data"]["amount"]
        price = float(data) * converter
        return price
        

    def quidax(self, coin="usdt"):
        url = f"https://www.quidax.com/api/v1/markets/{coin.lower()}ngn/order_book"
        response = requests.get(url, timeout=0.5)
        order_book = response.json()["data"]
        return order_book
    

    def qdx(self, coin):
        return float(self.quidax(coin)["asks"][0]["price"])
	

    def conversion(self):
        data = self.quidax()
        ask = float(data["asks"][0]["price"])
        bids = data["bids"]
        bid = float(bids[0]["price"])
        bid = float(bids[1]["price"]) if bid == 1600 else bid
        return math.sqrt(ask * bid)
        

    def rec(self):
        current_time = datetime.datetime.now(pytz.timezone('Africa/Lagos')).strftime('%Y-%m-%d %H:%M:%S')
        return current_time
        	
	
    def bot(self, *args):
        BOT_TOKEN = '8003135578:AAHufA9EPBwRgR9xEHlB2vyq4dhx8MxYoL8'
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
        	except Exception as e:
        		pass
        

    def get_day_number(self):
        	return (time() + 3600) // 86400


class Sol:
    def __init__(self):
        pass
        
        
    def sol_main(self):
        count = counter = 1
        thresh = 50.00001
        	
        	sell = 162.21
        	buy = 161.39
        	step = 0.00005
        	
        	calc = (1 / math.pow(0.999, 2)) * (math.sqrt(sell / buy))
        	
        	fees = round(calc if round(calc / step) * step == calc else math.ceil(calc / step) * step, 5)
        
        	coin = "SOL"
        	last_day = self.get_day_number()
        	
        	while True:
        		state = "   YES!" if count > 1 else ""
        		print(f"Running... {counter}{state}")
        		
        		current_day = self.get_day_number()
        		if current_day > last_day:
        			count = 1
        			counter = 0
        			self.bot()
        			last_day = current_day
        
        		try:
        			c_1 = self.coinbase(coin)
        			q = self.qdx(coin)
        			c_2 = self.coinbase(coin)
        			c = c_1 - c_2
        			diff = c_2 - q
        			c_q = c_2 / q
        			gain = c_q / fees
        			
        			counter += 1
        		
        			if c < thresh and gain > 1:
        				self.bot(count, diff, self.rec(), c_2, q, gain)
        				count += 1
        		
        		except Exception as e:
        			print(f"\nAn error occurred: {e}\n")
        			counter = 1 if not counter else counter
        
        if stop_event.is_set():
            break
    
    def coinbase(self, coin):
        url = f"https://api.coinbase.com/v2/prices/{coin}-USDT/spot"
        response = requests.get(url, timeout=0.3)
        data = response.json()["data"]["amount"]
        price = float(data)
        return price
        

    def qdx(self, coin):
        url = f"https://www.quidax.com/api/v1/markets/{coin.lower()}usdt/order_book"
        	response = requests.get(url, timeout=0.5)
        	order = response.json()["data"]["asks"][0]["price"]
        	return float(order)
        		
        
    def rec(self):
        current_time = datetime.datetime.now(pytz.timezone('Africa/Lagos')).strftime('%Y-%m-%d %H:%M:%S')
        return current_time
        	
	
    def bot(self, *args):
        BOT_TOKEN = '7743900681:AAFtpcFEtng9sbAUuxh2JimmajuxTLou08g'
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
        		
    
    def get_day_number(self):
        return (time() + 3600) // 86400


# Main controller
def main_loop():
    while not stop_event.is_set():
        Aave().aave_main()
        Btc().btc_main()
        Btc_ngn().btc_ngn_main()
        Sol().sol_main()
        
        print("Loop cycle complete. Restarting...\n")
        sleep(1)


if __name__ == "__main__":
    # Start the stop-listener thread
    stop_thread = threading.Thread(target=listen_for_stop, daemon=True)
    stop_thread.start()

    # Run the main app loop
    main_loop()

    print("Shutdown complete.")