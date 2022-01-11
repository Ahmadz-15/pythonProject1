import requests
import json


access_token = 'eed6fed4e780ad'

server_url = 'https://ipinfo.io/'

info_types = {
    'Geolocation': '/geo',
    'Privacy_Detection': '/privacy',
    'ASN': '/asn',
    'company_info': '/company',
    'abuse_info': '/abuse'
}

valid_ip_expected_res = {
  "ip": "161.185.160.93",
  "city": "New York City",
  "region": "New York",
  "country": "US",
  "loc": "40.7152,-73.9877",
  "org": "AS22252 The City of New York",
  "postal": "10002",
  "timezone": "America/New_York"
}

asn_expected_result = {
 "asn": "AS22252",
 "name": "The City of New York",
 "domain": "nyc.gov",
 "route": "161.185.160.0/24",
 "type": "Business"
}

privacy_off = {
    "vpn": False,
    "proxy": False,
    "tor": False,
    "relay": False,
    "hosting": False
}

privacy_on = {
    "vpn": True,
    "proxy": False,
    "tor": False,
    "relay": False,
    "hosting": False
}

valid_ip = '161.185.160.93'
invalid_ip = '161.185.160.93.'
masked_ip = '172.145.130.73'


def get_info(url, ip, token, info_type):
    print('sending a get request to {}'.format(url + ip + info_type))
    r = requests.get(url + ip + info_type, headers={'Authorization': 'Bearer {}'.format(token)})
    print(r.status_code)
    print(r.text)
    return [r.status_code, json.loads(r.text)]


# Testing a valid ip, expecting status_code 200 and json = expected_res
response = get_info(server_url, valid_ip, access_token, info_type=info_types['Geolocation'])
assert response[0] == 200 and response[1] == valid_ip_expected_res

# Testing an invalid ip, expecting status_code 404 and error message
response = get_info(server_url, invalid_ip, access_token, info_type=info_types['Geolocation'])
assert response[0] == 404 and response[1]['error']['title'] == 'Wrong ip'

# Getting ASN info for a valid ip
response = get_info(server_url, valid_ip, access_token, info_type=info_types['ASN'])
assert response[0] == 200 and response[1] == asn_expected_result

# Getting privacy info for unmasked ip, expecting json response = privacy_off
response = get_info(server_url, valid_ip, access_token, info_type=info_types['Privacy_Detection'])
assert response[0] == 200 and response[1] == privacy_off

# Getting privacy info for a masked ip, expecting json response = privacy_on
response = get_info(server_url, masked_ip, access_token, info_type=info_types['Privacy_Detection'])
assert response[0] == 200 and response[1] == privacy_on

