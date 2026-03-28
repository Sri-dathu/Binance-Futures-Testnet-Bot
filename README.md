# Binance Futures Testnet Trading Bot

##  Overview

This project is a simplified trading bot built using Python that interacts with the Binance Futures Testnet (USDT-M).
It supports placing MARKET and LIMIT orders via a CLI interface with proper logging and error handling.

---

## Features

* Place MARKET and LIMIT orders
* Supports BUY and SELL
* CLI-based input using argparse
* Input validation
* Logging of API requests, responses, and errors
* Error handling for invalid inputs and API failures
* Clean modular code structure

---

## Setup Instructions

### 1. Clone the repository

bash
git clone <your-repo-link>
cd trading_bot


### 2. Install dependencies

bash
pip install -r requirements.txt


### 3. Configure API Keys

Update your API keys in:


bot/client.py


## Usage

### MARKET Order

ash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002


### LIMIT Order

bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.002 --price 50000


## Output Example

* Order summary
* Order ID
* Status
* Executed Quantity
* Average Price



##Project Structure


trading_bot/
bot/
  client.py
    orders.py
    validators.py
    logging_config.py
cli.py
requirements.txt
README.md
app.log




## Assumptions

* Only USDT-M Futures trading is supported
* Minimum order notional must be ≥ 100 USDT
* API keys are generated from Binance Futures Testnet

---

## Logs

The application logs all requests, responses, and errors in:

app.log


## Conclusion

This project demonstrates API integration, structured Python development, CLI handling, and robust error/log management for real-world trading systems.
