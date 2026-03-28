import argparse
from bot.validators import validate_order
from bot.orders import place_market_order, place_limit_order
from bot.logging_config import setup_logger

def get_user_input():
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Enter order type (MARKET/LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))

    price = None
    if order_type == "LIMIT":
        price = float(input("Enter price: "))

    return symbol, side, order_type, quantity, price


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol")
    parser.add_argument("--side")
    parser.add_argument("--type")
    parser.add_argument("--quantity", type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()
    logger = setup_logger()

    try:
        if not all([args.symbol, args.side, args.type, args.quantity]):
            symbol, side, order_type, quantity, price = get_user_input()
        else:
            symbol = args.symbol
            side = args.side
            order_type = args.type
            quantity = args.quantity
            price = args.price

        # Validate
        validate_order(symbol, side, order_type, quantity, price)

        print(f"\nPlacing {side} {order_type} order for {symbol}")

        # Execute
        if order_type == "MARKET":
            order = place_market_order(symbol, side, quantity, logger)
        else:
            order = place_limit_order(symbol, side, quantity, price, logger)
        
        print("\nFULL RESPONSE:", order) #orders response details


        if not order:
            print("\nError : No response received from Binance")
            return

        print("\nOrder Success ")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice"))

    except Exception as e:
        logger.error(f"Error: {e}")
        print("\nError :", e)


if __name__ == "__main__":
    main()