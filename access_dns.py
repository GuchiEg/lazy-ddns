import requests
from secrets import *


def get_dns_records():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }
    req = requests.get(f"https://api.cloudflare.com/client/v4/zones/{API_ZONE_ID}/dns_records/", headers=headers).json()
    return req