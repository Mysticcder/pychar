import ipinfo

access_token = 'ba4ec41e72a47a'
handler = ipinfo.getHandler(access_token)

ip_address = "102.168.100.23"
details = handler.getDetails(ip_address)
print(details.all)
