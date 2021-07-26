from access_dns import get_dns_records, get_ip_addr, update_ip_addr

def main():
    ip_addr = get_ip_addr()
    record = get_dns_records()
    if record["content"] == ip_addr:
        return
    req = update_ip_addr(record, ip_addr)


if __name__ == "__main__":
    main()
