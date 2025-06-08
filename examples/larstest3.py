from datetime import datetime, timedelta
from borsdata_client import BorsdataClient, BorsdataClientError
import os

api_key = os.getenv('BORSDATA_API_KEY')

try:
    with BorsdataClient(api_key) as client:
        instruments = client.get_instruments()
        # Get stock prices for the last 30 days
        today = datetime.now()
        last_month = today - timedelta(days=30)

        prices = client.get_stock_prices(
            instrument_id=3,  # Example: Volvo B
            from_date=last_month,
            to_date=today,
            max_count=30
        )

        for price in prices:
            print(f"Date: {price.d}, Close: {price.c}, Volume: {price.v}")

except BorsdataClientError as e:
    print(f"API request failed: {e}")
