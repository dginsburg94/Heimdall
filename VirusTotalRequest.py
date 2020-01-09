#!/usr/bin/env python3
import requests
import json
from special import key

def virusTotal(domain):
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': key, 'resource':domain}
    response = requests.get(url, params=params)
    parsed = json.loads(response.text)
    if parsed['verbose_msg'] == 'Resource does not exist in the dataset':
        return None
    if parsed['positives'] != 0:
        return True
    else:
        return False