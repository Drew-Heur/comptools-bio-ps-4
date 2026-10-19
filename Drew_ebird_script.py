import requests
from collections import Counter
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

API_KEY = "b0c91064-6346-43e9-8319-b7a776b31c18"
BASE_URL = "https://api.ebird.org/v2"
headers = {"X-eBirdApiToken": API_KEY}

species = {"turvul": "Turkey Vulture", "blkvul": "Black Vulture"}

# Fetch each species separately and count observations per day
counts_by_species = {}
for code in species:
    url = f"{BASE_URL}/data/obs/US-FL/recent/{code}"
    params = {"back": 30, "maxResults": 10000}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    obs_list = response.json()
    print(f"{species[code]}: {len(obs_list)} observations")

    days = [datetime.strptime(o["obsDt"][:10], "%Y-%m-%d").date() for o in obs_list]
    counts_by_species[code] = Counter(days)

# Build a full 30-day axis so days with zero observations still show up
today = datetime.now().date()
all_dates = [today - timedelta(days=i) for i in range(29, -1, -1)]

fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

for ax, (code, name) in zip(axes, species.items()):
    counts = counts_by_species[code]
    ax.bar(all_dates, [counts.get(d, 0) for d in all_dates])
    ax.set_title(f"{name} observations in Florida (last 30 days)")
    ax.set_ylabel("Number of observations")

axes[-1].set_xlabel("Date")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()