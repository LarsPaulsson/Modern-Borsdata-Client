# from borsdata_client import BorsdataClient
from borsdata_client import BorsdataClient, Instrument, StockPrice
from datetime import datetime, timedelta
import os
import requests
from typing import Dict, List, Tuple
import pandas as pd

api_key = os.getenv('BORSDATA_API_KEY')
API_KEY = os.getenv('BORSDATA_API_KEY')

# Define a sample portfolio (ticker: number of shares)
PORTFOLIO = {
    "BEAMMW B":500000,
    "CANTA":0,
    "ERIC B": 100,  # Ericsson
    "QCORE":54000,
    "SEB A": 75,    # SEB
    "VOLV B": 50,   # Volvo
}

def get_instrument_by_ticker(client: BorsdataClient, ticker: str) -> Instrument:
    """Find an instrument by its ticker symbol."""
    instruments = client.get_instruments()
    for instrument in instruments:
        if instrument.ticker == ticker:
            return instrument
    raise ValueError(f"Instrument with ticker {ticker} not found")

# beamm 2373
# canta 748
url = "https://borsdata.se/api/terminal/instruments/2373/equities"

headers = {
    "authority": "borsdata.se",
    "accept": "application/json",
    "accept-language": "sv,en;q=0.9",
    "referer": "https://borsdata.se/terminal/se/beammwave/agardata",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
#    "cookie": "CookieConsent=false; ai_user=HzJSyClpWpDDUPy9FE6+IT|2025-03-26T10:32:03.944Z; borsdata.auth=CfDJ8LcDIbE8kM9OojHsqXH7bConydkPdzI6REFGYB6RoQS5d5xXJh30wIYIKdBQHovttiNGXtmqPI1HXhzvMRgX6NkZZrUC3ybupwn4Gt-F_ONS_WfEJdI3ckhLzPw5o7tBKu6HnP64gJHk5-ENCh5uUTb5BH_mM-riwmYJ1mpSqR_UHUy8ug38h5PbEBqDV9BHeA7zQxaMOUAnhfaiFzuHuLQibS22hEroqbWrrW4PP3SZgi2-knpQrZBl414PLCErwioC4ddK4GO6jblkDeOrjtbdxvMJlp7nz50a3T_qNt0Td9P6-XGpe2mx9T_Mznd7e57M103trWnfQgpkCormIR6eRHuqG3INNFpKmUMvXKJNUsEnuhlvkmw4TjwmS_sNUAnek9j86ig0C2nraI5R6rXKqJ3Gya_KgiVlZ1LNi3Ei4ys74yZrBtcRECBsQo6yrm8jOUD1NPEnI6yFlcPSbFjTMvd865ml3qXBRJ3Shv8GQXxPfMq5ynJt-FMg4J2akSspf5PAlpjCwg4XH6h_EY0JIrKvGTPvAU_Q34pQ5oRvjRKrKPKiab585ysjpWoKFqkwrHG3wTv_8IaSlyP-IJ8lI2kW98VkZeVJ5C9M2uOmLeMQU1Yh_tOU-wrqZvWhxNjNK6AHZDuh0cBsi7XqZ0AVm0ksPLfsf7ROJGCVnruBtAKHLgPGBx56gBft5mLMwFX_X8UA1urYUN6iIbQK3sD7t6fzRfQ3MpUSUQUA2822TYyVi4gswiCZTpKrXTS_mw; ai_session=+Dqz1aSMpw5faAviJTVYyB|1747866458243|1747866917435",
    "cookie": "CookieConsent=false; ai_user=HzJSyClpWpDDUPy9FE6+IT|2025-03-26T10:32:03.944Z; borsdata.auth=CfDJ8PwJFyuz_NtBiAXErgVPg4zYt6kFHawihaX5JSeGA3sFfUwwsHYR_Il365gnNLEu5yZlquatHkq8ShbJ172wP1UKN4iXXTTAPPxqknWskr3H1HfwkVbB6htMrZGjaeaFBX_jNkrN0WDB7GlwLWH8ZdZAGdTM4TcXhKclRebqw37hgYP-9KMTidbx0MGN34lrsSWAs69OPR9tsqAmCvsU5XYkoFZf5Qcp0raLvL5tEQVWrUNmMP-bm-KAIN99cuSFyCwNexxcgYN7mNgm5Jd9msiT-IVuJgNUeSPcnbKDOTqq8DnAYvIPn7QP4cyK6xm6McHr858eQaD11nokopWUMsyxzzQU50QYxpUVdfqhetzqn4jWOgQkNBf6I1P9lNhsk3gOh3ds4BUjC3yZGxdggcfaInkpl_66AKpTth3n4oz87gDFPDewUrYgd15Gcxj77Pg-LzaHEtc3b_bPoCRXszLd3NXqiKmHRSJHuykjR2Y-Hi1e0NSgUOwc6q9LeffetcXh-nHMgQDpwEQQBF2nXgpUT7dDnbQVsj0VHSY44DkMNNxQA-mSifhq4QGxGbGFmujdsp5ecG21lSTttuVoukqtEOMaXOHOtGMr_Gud9HfGUXYO7ltRk681TWr2dNnBtWA5dRmTz2bqtIaDpC-9gZp9u36LM2Jn1BVtACg_CN-5DvClpTnJcDDPJhTIwhpqB4LF2Drb5lSGL92ZQ5sb1ZQtUQ6JrISD_3hgPCJTfTFzg2_JmVICsr7BjANcyQsmNQ; ai_session=60QkCq1GhUEIovSqnEezFI|1749397439295|1749397439295",

    "x-bd-language": "se",
    "sec-fetch-mode": "cors",
}

def check_portfolio(
    client: BorsdataClient,
    portfolio: Dict[str, int]
) -> Tuple[float, Dict[str, float], pd.DataFrame]:
    """Calculate the current value of a portfolio and its performance."""
    total_value = 0.0
    stock_values = {}
    price_history = {}
    
    # Get all instruments
    instruments = client.get_instruments()

    # Get all branches
    branches = client.get_branches()
    branch_map = {b.id: b.name for b in branches}

    # Create a DataFrame with instrument details
    instrument_df = pd.DataFrame([{
        "ID": i.ins_id,
        "Name": i.name,
        "Ticker": i.ticker,
        "Branch ID": i.branch_id,
        "Branch": branch_map.get(i.branch_id, "Unknown") if i.branch_id else "Unknown"
    } for i in instruments])

    # Get last stock prices, Call API 20:00 UTC to get today latest data. (Or you will get yesterday data)
    # Man kan bara hämta stängningspris, inte löpande under dagen.
    # Det finns också API för att hämta alla slutkurser för en lista av instrument, men man kan lika gärna hämta alla
    # då det blir enklare att lägga till och dra ifrån, samt avslöjar inte för Börsdata vilka man följer.
    last_prices = client.get_last_stock_prices()

    # Create a DataFrame with price details
    price_df = pd.DataFrame([{
        "ID": p.i,
        "Date": datetime.strptime(p.d, "%Y-%m-%d"),
        "Close": p.c,
        "Volume": p.v
    } for p in last_prices])

    # Merge the DataFrames
    combined_df = pd.merge(instrument_df, price_df, on="ID", how="left")

    # Get data for each stock in the portfolio
    for ticker, shares in portfolio.items():
        try:
            # Filtrera för den valda tickern
            stock_info = combined_df[combined_df["Ticker"] == ticker]

            # Visa resultat
            if not stock_info.empty:
                row = stock_info.iloc[0]
                latest_price=row['Close']
                print(f"Senaste kurs för {row['Ticker']} ({row['Name']}): {row['Close']} SEK den {row['Date'].date()}")
            else:
                latest_price=0
                print("Ticker hittades inte.")

          
            stock_value = latest_price * shares
            # Store the results
            total_value += stock_value
            stock_values[ticker] = stock_value
                        
            print(f"{ticker}: {shares} shares at {latest_price:.2f} = {stock_value:.2f}")
            
        except ValueError as e:
            print(f"Error processing {ticker}: {e}")
        
    return total_value, stock_values


def check_owner():
    response = requests.get(url, headers=headers)

    if response.ok:
        print("OKOKOK")
        data = response.json()
        # print(data)
        # for item in data.get('items', []):
        #    print(f"{item['owner']} äger {item['shares']} aktier ({item['ownershipPct']}%)")
        for owner in data['topOwners']:
            print(f"Namn: {owner['name']}")
            print(f"  Kapitalandel: {owner['capital']['fValue']}")
            print(f"  Röstandel: {owner['votes']['fValue']}")
            print(f"  Förändring i kapital: {owner['capitalDelta']['fValue']}")
            print(f"  Marknadsvärde: {owner['mcap']['fValue']}")
            print(f"  Verifierad: {owner['verified']['fValue']}")
            print(f"  Förändring i antal aktier: {owner['deltaShares']['fValue']}")
            print("  Aktier:")
            for stock in owner['stocks']:
                print(f"    {stock['symbol']}: {stock['fValue']}")
            print("-" * 40)
    else:
        print("Fel:", response.status_code, response.text)

def check_owners():
    # for each stock in the portfolio
    for ticker, shares in portfolio.items():
        try:
            # Filtrera för den valda tickern
            stock_info = combined_df[combined_df["Ticker"] == ticker]

            # Visa resultat
            if not stock_info.empty:
                row = stock_info.iloc[0]
                latest_price=row['Close']
                print(f"Senaste kurs för {row['Ticker']} ({row['Name']}): {row['Close']} SEK den {row['Date'].date()}")
            else:
                latest_price=0
                print("Ticker hittades inte.")

          
            stock_value = latest_price * shares
            # Store the results
            total_value += stock_value
            stock_values[ticker] = stock_value
                        
            print(f"{ticker}: {shares} shares at {latest_price:.2f} = {stock_value:.2f}")
            
        except ValueError as e:
            print(f"Error processing {ticker}: {e}")

def main():
    """Run the portfolio analysis example."""
    with BorsdataClient(api_key) as client:
        print("Analyzing portfolio...")
        total_value, stock_values = check_portfolio(client, PORTFOLIO)
        
        print("\nPortfolio Summary:")
        print(f"Total Value: {total_value:.2f}")
    check_owner()
        

if __name__ == "__main__":
    main()
    # print(api_key)
    
