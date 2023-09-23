import time
import logging
import requests
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest, DescribeDomainRecordsRequest, AddDomainRecordRequest
from aliyunsdkcore.acs_exception.exceptions import ServerException

# Alibaba Cloud API Credentials
access_key_id = 'your_access_key_id'
access_key_secret = 'your_access_key_secret'
region_id = 'cn-hangzhou'  # Your Alibaba Cloud region ID (No modifications needed.)

# Domain name and record information.
domain_name = 'example.com'  # your domain
sub_domain = 'www'  # subdomain，for example: www

# Set logging
logging.basicConfig(level=logging.INFO)

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # Throw HTTP error.
        ip = response.json()['ip']
        logging.info(f'Public IP retrieved: {ip}')
        return ip
    except requests.exceptions.RequestException as e:
        logging.error(f'Failed to retrieve public IP: {e}')
        return None

def get_current_dns_record(client, domain_name, sub_domain):
    request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    request.set_DomainName(domain_name)
    try:
        response = client.do_action_with_exception(request)
        records = json.loads(response)['DomainRecords']['Record']
        for record in records:
            if record['RR'] == sub_domain and record['Type'] == 'A':
                return record['RecordId'], record['Value']
        return None, None
    except ServerException as e:
        logging.error(f'Failed to get the current DNS record: {e}')
        return None, None

def update_dns_record(client, record_id, sub_domain, ip):
    request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    request.set_RecordId(record_id)
    request.set_RR(sub_domain)
    request.set_Type('A')
    request.set_Value(ip)
    try:
        client.do_action_with_exception(request)
        logging.info(f'Updated DNS record to {ip}')
    except ServerException as e:
        logging.error(f'Failed to update DNS record: {e}')

def add_dns_record(client, domain_name, sub_domain, ip):
    request = AddDomainRecordRequest.AddDomainRecordRequest()
    request.set_DomainName(domain_name)
    request.set_RR(sub_domain)
    request.set_Type('A')
    request.set_Value(ip)
    try:
        client.do_action_with_exception(request)
        logging.info(f'Added DNS record: {sub_domain}.{domain_name} -> {ip}')
    except ServerException as e:
        logging.error(f'Failed to add DNS record: {e}')

def update_dns_record_if_needed(client, domain_name, sub_domain, new_ip):
    record_id, current_ip = get_current_dns_record(client, domain_name, sub_domain)
    if record_id is None:
        logging.warning(f'No existing DNS record found for {sub_domain}.{domain_name}, adding a new record.')
        add_dns_record(client, domain_name, sub_domain, new_ip)
        return
    if current_ip != new_ip:
        update_dns_record(client, record_id, sub_domain, new_ip)

def main():
    client = AcsClient(access_key_id, access_key_secret, region_id)
    
    while True:
        new_ip = get_public_ip()
        if new_ip is not None:
            update_dns_record_if_needed(client, domain_name, sub_domain, new_ip)
        time.sleep(10)  # Wait for 10 seconds before checking again.

if __name__ == '__main__':
    main()
