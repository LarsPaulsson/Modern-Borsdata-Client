from borsdata_client import BorsdataClient
from datetime import datetime, timedelta
import os
import requests

api_key = os.getenv('BORSDATA_API_KEY')
API_KEY = os.getenv('BORSDATA_API_KEY')

# beamm 2373
# canta 748
url = "https://borsdata.se/api/terminal/instruments/2373/equities"

headers = {
    "authority": "borsdata.se",
    "accept": "application/json",
    "accept-language": "sv,en;q=0.9",
    "referer": "https://borsdata.se/terminal/se/beammwave/agardata",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "cookie": "CookieConsent=false; ai_user=HzJSyClpWpDDUPy9FE6+IT|2025-03-26T10:32:03.944Z; borsdata.auth=CfDJ8LcDIbE8kM9OojHsqXH7bConydkPdzI6REFGYB6RoQS5d5xXJh30wIYIKdBQHovttiNGXtmqPI1HXhzvMRgX6NkZZrUC3ybupwn4Gt-F_ONS_WfEJdI3ckhLzPw5o7tBKu6HnP64gJHk5-ENCh5uUTb5BH_mM-riwmYJ1mpSqR_UHUy8ug38h5PbEBqDV9BHeA7zQxaMOUAnhfaiFzuHuLQibS22hEroqbWrrW4PP3SZgi2-knpQrZBl414PLCErwioC4ddK4GO6jblkDeOrjtbdxvMJlp7nz50a3T_qNt0Td9P6-XGpe2mx9T_Mznd7e57M103trWnfQgpkCormIR6eRHuqG3INNFpKmUMvXKJNUsEnuhlvkmw4TjwmS_sNUAnek9j86ig0C2nraI5R6rXKqJ3Gya_KgiVlZ1LNi3Ei4ys74yZrBtcRECBsQo6yrm8jOUD1NPEnI6yFlcPSbFjTMvd865ml3qXBRJ3Shv8GQXxPfMq5ynJt-FMg4J2akSspf5PAlpjCwg4XH6h_EY0JIrKvGTPvAU_Q34pQ5oRvjRKrKPKiab585ysjpWoKFqkwrHG3wTv_8IaSlyP-IJ8lI2kW98VkZeVJ5C9M2uOmLeMQU1Yh_tOU-wrqZvWhxNjNK6AHZDuh0cBsi7XqZ0AVm0ksPLfsf7ROJGCVnruBtAKHLgPGBx56gBft5mLMwFX_X8UA1urYUN6iIbQK3sD7t6fzRfQ3MpUSUQUA2822TYyVi4gswiCZTpKrXTS_mw; ai_session=+Dqz1aSMpw5faAviJTVYyB|1747866458243|1747866917435",
    "x-bd-language": "se",
    "sec-fetch-mode": "cors",
}

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
