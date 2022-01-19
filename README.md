## Simple Trading tool

Only summarizes trading in Binance for now

### Usage 
1. Create binance Read only API key: https://www.binance.com/en/support/faq/360002502072

2. Update docker-env.list with the keys (make sure you don't commit this anywhere)
3. Update your symbols (only USDT pairs supported for now) in `main.py` 
4. Run:

```
cd mytrades
docker build -t trades .
docker run --env-file ./docker-env.list  mytrades
```


Sample output:

```
--------------------['QIUSDT']-------------------------
Current holding QIUSDT : ...
Total spent USDT: ...
Avg price USDT: 0.2477
Current price USDT: 0.0881646
Current holding value QIUSDT : 
Profit/loss QIUSDT: ...
--------------------['ROSEUSDT']-------------------------
Current holding ROSEUSDT : ...
Total spent USDT: ...
Avg price USDT: 0.3898333333333333
Current price USDT: 0.47665246
Current holding value ROSEUSDT : ...
Profit/loss ROSEUSDT: ...
=============================================
Total Profit/loss ...
=============================================
```

### Library
https://python-binance.readthedocs.io/en/latest/