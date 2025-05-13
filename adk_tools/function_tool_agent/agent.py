import os
from dotenv import load_dotenv
import yfinance as yf

from google.adk import Agent

load_dotenv()
model_name = os.getenv("MODEL")


def get_stock_price(symbol: str):
    """
    Retrieves the current stock price for a given symbol.

    Args:
        symbol (str): The stock symbol (e.g., "AAPL", "GOOG").

    Returns:
        float: The current stock price, or None if an error occurs.
    """
    try:
        stock = yf.Ticker(symbol)
        historical_data = stock.history(period="1d")
        if not historical_data.empty:
            current_price = historical_data["Close"].iloc[-1]
            return {"current_price": current_price}
        else:
            return {"status": "error",
                    "error_message": "could not find data"}
    except Exception as e:
        print(f"Error retrieving stock price for {symbol}: {e}")
        return {"status": "error",
                "error_message": f"Error retrieving stock price for {symbol}: {e}"}


root_agent = Agent(
    name="function_tool_agent",
    model=model_name,
    description="Agent to look up stock prices.",
    instruction="I can answer your questions about stock prices for a given ticker symbol.",
    # Add the function tool below


)