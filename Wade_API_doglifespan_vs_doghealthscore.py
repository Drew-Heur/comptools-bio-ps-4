import json, csv, urllib.request

url = "https://breedhealthscore.com/api/breeds.json"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
data = json.load(urllib.request.urlopen(req))

with open("breed_health.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["breed", "median_lifespan_years", "health_score"])
    for b in data["breeds"]:                     # each b is one breed's dict
        w.writerow([b["breed"], b["median_lifespan_years"], b["health_score"]])

print(data["count"], "breeds written")

import matplotlib.pyplot as plt

breeds = data["breeds"]
x = [b["median_lifespan_years"] for b in breeds]
y = [b["health_score"] for b in breeds]

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(x, y, alpha=0.7)
ax.set_xlabel("Median lifespan (years)")
ax.set_ylabel("Breed Health Score")
ax.set_title("Lifespan vs. health score, 155 dog breeds")
