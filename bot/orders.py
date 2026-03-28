from binance.enums import *
from bot.client import get_client

client = get_client()

def place_market_order(symbol, side, quantity, logger):
    try:
        logger.info(f"Placing MARKET order: {side} {symbol} {quantity}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )

        logger.info(f"Order Response: {order}")
        return order

    except Exception as e:
        logger.error(f"Error placing MARKET order: {e}")
        raise


def place_limit_order(symbol, side, quantity, price, logger):
    try:
        logger.info(f"Placing LIMIT order: {side} {symbol} {quantity} @ {price}")

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC,
             newOrderRespType="RESULT" 
        )

        logger.info(f"Order Response: {order}")
        return order

    except Exception as e:
        logger.error(f"Error placing LIMIT order: {e}")
        raise