#!/bin/env python
import requests
API_key = input('Paste Your CloudFlare API Key here:')
zone_identifier = input('Paste Your CloudFlare Zone ID here:')

def get_dns_records(API_key, zone_identifier):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records?per_page=1000"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {API_key}"
    }
    resp = requests.get(url, headers=headers)
    nums = len(resp.json()['result'])
    print(f"have {nums} record(s)")
    i = 0
    id_list = []
    for i in range(nums):
        id_list.append(resp.json()['result'][i]['id'])
    return id_list

def delete_dns_records(API_key, zone_identifier, id_list):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {API_key}"
    }
    for i in range(len(id_list)):
        print(f'deleting {i+1} records')
        url = f'https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records/{id_list[i]}'
        requests.delete(url, headers=headers)
    print('finished')

id_list = get_dns_records(API_key, zone_identifier)
delete_dns_records(API_key, zone_identifier, id_list)