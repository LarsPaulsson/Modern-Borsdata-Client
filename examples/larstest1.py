from borsdata_client import BorsdataClient
from datetime import datetime, timedelta
import os

api_key = os.getenv('BORSDATA_API_KEY')

# Initialize the client with your API key
client = BorsdataClient(api_key)

# Get all available instruments (stocks)
instruments = client.get_instruments()

# Print the first 5 instruments
for instrument in instruments[:50]:
    print(f"ID: {instrument.ins_id}, Name: {instrument.name}, Ticker: {instrument.ticker}")

