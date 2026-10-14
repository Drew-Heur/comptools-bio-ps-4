import requests

API_KEY = "b0c91064-6346-43e9-8319-b7a776b31c18"  # better: load from an environment variable
BASE_URL = "https://api.ebird.org/v2"

headers = {"X-eBirdApiToken": API_KEY}

# Recent observations in Florida (region code US-FL)
url = f"{BASE_URL}/data/obs/US-FL/recent"
params = {"maxResults": 50}

response = requests.get(url, headers=headers, params=params)
response.raise_for_status()  # raises an error if the request failed

observations = response.json()  # list of dicts

for obs in observations[:10]:
    print(obs["comName"], obs["howMany"] if "howMany" in obs else "?", obs["locName"])