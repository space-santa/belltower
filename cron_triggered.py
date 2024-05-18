import requests

from src.utils import determine_rings

times, hour_times = determine_rings()
# times = 5
response = requests.get(
    "http://localhost:8456/api/ring/",
    params={"times": times, "hour_times": hour_times, "volume": 0.2},
    timeout=30,
)

print(f"{response.status_code} - {response.content}")
