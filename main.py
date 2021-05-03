import socket
from access_dns import get_dns_records

# ip = get('https://api.ipify.org').text
# print('My public IP address is: {}'.format(ip))

print(get_dns_records())