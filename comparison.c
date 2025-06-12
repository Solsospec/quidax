#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>
#include <sys/time.h>
#include "cJSON.h"

#define N 10

typedef struct {
	char *memory;
	size_t size;
} MemoryStruct;

static size_t WriteMemoryCallback(void *contents, size_t size, size_t nmemb, void *userp) {
	size_t realsize = size * nmemb;
	MemoryStruct *mem = (MemoryStruct *)userp;
	char *ptr = realloc(mem->memory, mem->size + realsize + 1);
	if(ptr == NULL) return 0; // out of memory
	mem->memory = ptr;
	memcpy(&(mem->memory[mem->size]), contents, realsize);
	mem->size += realsize;
	mem->memory[mem->size] = 0;
	return realsize;
}

double gettime() {
	struct timeval t;
	gettimeofday(&t, NULL);
	return t.tv_sec + t.tv_usec/1e6;
}

double get_kucoin_price() {
	CURL *curl = curl_easy_init();
	MemoryStruct chunk = {.memory = malloc(1), .size = 0};
	curl_easy_setopt(curl, CURLOPT_URL, "https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=AAVE-USDT");
	curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
	curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);
	curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10L);
	CURLcode res = curl_easy_perform(curl);
	double val = 0.0;
	if(res == CURLE_OK) {
		cJSON *json = cJSON_Parse(chunk.memory);
		if(json) {
			cJSON *data = cJSON_GetObjectItem(json, "data");
			cJSON *price = cJSON_GetObjectItem(data, "price");
			if (cJSON_IsString(price)) val = atof(price->valuestring);
			cJSON_Delete(json);
		}
	}
	curl_easy_cleanup(curl);
	free(chunk.memory);
	return val;
}

double get_coinbase_price() {
	CURL *curl = curl_easy_init();
	MemoryStruct chunk = {.memory = malloc(1), .size = 0};
	curl_easy_setopt(curl, CURLOPT_URL, "https://api.coinbase.com/v2/prices/AAVE-USDT/spot");
	curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
	curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);
	curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10L);
	CURLcode res = curl_easy_perform(curl);
	double val = 0.0;
	if(res == CURLE_OK) {
		cJSON *json = cJSON_Parse(chunk.memory);
		if(json) {
			cJSON *data = cJSON_GetObjectItem(json, "data");
			cJSON *amount = cJSON_GetObjectItem(data, "amount");
			if (cJSON_IsString(amount)) val = atof(amount->valuestring);
			cJSON_Delete(json);
		}
	}
	curl_easy_cleanup(curl);
	free(chunk.memory);
	return val;
}

double get_okx_price() {
	CURL *curl = curl_easy_init();
	MemoryStruct chunk = {.memory = malloc(1), .size = 0};
	curl_easy_setopt(curl, CURLOPT_URL, "https://www.okx.com/api/v5/market/ticker?instId=AAVE-USDT");
	curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
	curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);
	curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10L);
	CURLcode res = curl_easy_perform(curl);
	double val = 0.0;
	if(res == CURLE_OK) {
		cJSON *json = cJSON_Parse(chunk.memory);
		if(json) {
			cJSON *data = cJSON_GetObjectItem(json, "data");
			if (cJSON_IsArray(data)) {
				cJSON *item = cJSON_GetArrayItem(data, 0);
				cJSON *last = cJSON_GetObjectItem(item, "last");
				if (cJSON_IsString(last)) val = atof(last->valuestring);
			}
			cJSON_Delete(json);
		}
	}
	curl_easy_cleanup(curl);
	free(chunk.memory);
	return val;
}

double get_mexc_price() {
	CURL *curl = curl_easy_init();
	MemoryStruct chunk = {.memory = malloc(1), .size = 0};
	curl_easy_setopt(curl, CURLOPT_URL, "https://api.mexc.com/api/v3/ticker/price?symbol=AAVEUSDT");
	curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
	curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);
	curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10L);
	CURLcode res = curl_easy_perform(curl);
	double val = 0.0;
	if(res == CURLE_OK) {
		cJSON *json = cJSON_Parse(chunk.memory);
		if(json) {
			cJSON *price = cJSON_GetObjectItem(json, "price");
			if (cJSON_IsString(price)) val = atof(price->valuestring);
			cJSON_Delete(json);
		}
	}
	curl_easy_cleanup(curl);
	free(chunk.memory);
	return val;
}

double get_gate_price() {
	CURL *curl = curl_easy_init();
	MemoryStruct chunk = {.memory = malloc(1), .size = 0};
	curl_easy_setopt(curl, CURLOPT_URL, "https://api.gateio.ws/api/v4/spot/tickers?currency_pair=AAVE_USDT");
	curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
	curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);
	curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10L);
	CURLcode res = curl_easy_perform(curl);
	double val = 0.0;
	if(res == CURLE_OK) {
		cJSON *json = cJSON_Parse(chunk.memory);
		if(json && cJSON_IsArray(json)) {
			cJSON *item = cJSON_GetArrayItem(json, 0);
			cJSON *last = cJSON_GetObjectItem(item, "last");
			if (cJSON_IsString(last)) val = atof(last->valuestring);
			cJSON_Delete(json);
		}
	}
	curl_easy_cleanup(curl);
	free(chunk.memory);
	return val;
}

double get_htx_price() {
	CURL *curl = curl_easy_init();
	MemoryStruct chunk = {.memory = malloc(1), .size = 0};
	curl_easy_setopt(curl, CURLOPT_URL, "https://api.huobi.pro/market/detail/merged?symbol=aaveusdt");
	curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
	curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);
	curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10L);
	CURLcode res = curl_easy_perform(curl);
	double val = 0.0;
	if(res == CURLE_OK) {
		cJSON *json = cJSON_Parse(chunk.memory);
		if(json) {
			cJSON *tick = cJSON_GetObjectItem(json, "tick");
			if (tick) {
				cJSON *close = cJSON_GetObjectItem(tick, "close");
				if (cJSON_IsNumber(close)) val = close->valuedouble;
			}
			cJSON_Delete(json);
		}
	}
	curl_easy_cleanup(curl);
	free(chunk.memory);
	return val;
}

double get_binance_price() {
	CURL *curl = curl_easy_init();
	MemoryStruct chunk = {.memory = malloc(1), .size = 0};
	curl_easy_setopt(curl, CURLOPT_URL, "https://api.binance.com/api/v3/ticker/price?symbol=AAVEUSDT");
	curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
	curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);
	curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10L);
	CURLcode res = curl_easy_perform(curl);
	double val = 0.0;
	if(res == CURLE_OK) {
		cJSON *json = cJSON_Parse(chunk.memory);
		if(json) {
			cJSON *price = cJSON_GetObjectItem(json, "price");
			if (cJSON_IsString(price)) val = atof(price->valuestring);
			cJSON_Delete(json);
		}
	}
	curl_easy_cleanup(curl);
	free(chunk.memory);
	return val;
}

double get_bybit_price() {
	CURL *curl = curl_easy_init();
	MemoryStruct chunk = {.memory = malloc(1), .size = 0};
	curl_easy_setopt(curl, CURLOPT_URL, "https://api.bybit.com/v5/market/tickers?category=spot&symbol=AAVEUSDT");
	curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
	curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);
	curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10L);
	CURLcode res = curl_easy_perform(curl);
	double val = 0.0;
	if(res == CURLE_OK) {
		cJSON *json = cJSON_Parse(chunk.memory);
		if(json) {
			cJSON *result = cJSON_GetObjectItem(json, "result");
			if (result) {
				cJSON *list = cJSON_GetObjectItem(result, "list");
				if (list && cJSON_IsArray(list)) {
					cJSON *item = cJSON_GetArrayItem(list, 0);
					cJSON *lastPrice = cJSON_GetObjectItem(item, "lastPrice");
					if (cJSON_IsString(lastPrice)) val = atof(lastPrice->valuestring);
				}
			}
			cJSON_Delete(json);
		}
	}
	curl_easy_cleanup(curl);
	free(chunk.memory);
	return val;
}

int main() {
	double a_b=0, i_r=0, c_d=0, pri_ce=0, e_f=0, okx_price=0, i_j=0, mexc_price=0, k_l=0, gate_price=0;
	double m_n=0, htx_price=0, o_p=0, binance_price=0, q_r=0, bybit_price=0;

	curl_global_init(CURL_GLOBAL_DEFAULT);

	for (int i=0; i<N; i++) {
		// Kucoin
		double a = gettime();
		double kucoin = get_kucoin_price();
		double b = gettime() - a;
		i_r += kucoin;
		a_b += b;

		// Coinbase
		double c = gettime();
		double coinbase = get_coinbase_price();
		double d = gettime() - c;
		pri_ce += coinbase;
		c_d += d;

		// OKX
		double e = gettime();
		double okx = get_okx_price();
		double f = gettime() - e;
		okx_price += okx;
		e_f += f;

		// MEXC
		double i1 = gettime();
		double mexc = get_mexc_price();
		double j = gettime() - i1;
		mexc_price += mexc;
		i_j += j;

		// Gate.io
		double k = gettime();
		double gate = get_gate_price();
		double l = gettime() - k;
		gate_price += gate;
		k_l += l;

		// HTX (Huobi)
		double m = gettime();
		double htx = get_htx_price();
		double n1 = gettime() - m;
		htx_price += htx;
		m_n += n1;

		// Binance
		double o = gettime();
		double binance = get_binance_price();
		double p = gettime() - o;
		binance_price += binance;
		o_p += p;

		// Bybit
		double q = gettime();
		double bybit = get_bybit_price();
		double r = gettime() - q;
		bybit_price += bybit;
		q_r += r;
	}

	printf("Kucoin:   %f -- %f\n", i_r/N, a_b/N);
	printf("Coinbase: %f -- %f\n", pri_ce/N, c_d/N);
	printf("OKX:	  %f -- %f\n", okx_price/N, e_f/N);
	printf("MEXC:	 %f -- %f\n", mexc_price/N, i_j/N);
	printf("Gate.io:  %f -- %f\n", gate_price/N, k_l/N);
	printf("HTX:	  %f -- %f\n", htx_price/N, m_n/N);
	printf("Binance:  %f -- %f\n", binance_price/N, o_p/N);
	printf("Bybit:	%f -- %f\n", bybit_price/N, q_r/N);

	printf("\nKucoin/Coinbase Latency Ratio:   %f\n", (a_b/N)/(c_d/N));
	printf("OKX/Coinbase Latency Ratio:	  %f\n", (e_f/N)/(c_d/N));
	printf("MEXC/Coinbase Latency Ratio:	 %f\n", (i_j/N)/(c_d/N));
	printf("Gate.io/Coinbase Latency Ratio:  %f\n", (k_l/N)/(c_d/N));
	printf("HTX/Coinbase Latency Ratio:	  %f\n", (m_n/N)/(c_d/N));
	printf("Binance/Coinbase Latency Ratio:  %f\n", (o_p/N)/(c_d/N));
	printf("Bybit/Coinbase Latency Ratio:	%f\n", (q_r/N)/(c_d/N));

	curl_global_cleanup();
	return 0;
}