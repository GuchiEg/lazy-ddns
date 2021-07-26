import requests
from secrets import API_TOKEN, API_ZONE_ID, WEBPAGE_NAME


def get_dns_records():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }
    req = requests.get(f"https://api.cloudflare.com/client/v4/zones/{API_ZONE_ID}/dns_records/", headers=headers).json()
    for result in req["result"]:
        # Find the correct DNS 
        if result["name"] == WEBPAGE_NAME:
            return result
    return None


def get_ip_addr():
    ip = requests.get('https://api.ipify.org').text
    return ip


def update_ip_addr(record, ip_addr):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }
    update_data = {
        "type": record["type"],
        "name": WEBPAGE_NAME,
        "content": ip_addr,
        "ttl": 1
    }
    print(f"Updating IP Address to {ip_addr}")
    req = requests.put(f"https://api.cloudflare.com/client/v4/zones/{API_ZONE_ID}/dns_records/{record['id']}/", 
            headers=headers, json=update_data)
    return req
