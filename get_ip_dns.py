import requests
from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest


# 阿里云API凭证
access_key_id = 'your_access_key_id'
access_key_secret = 'your_access_key_secret'
region_id = 'cn-hangzhou'  # 你的阿里云区域ID (可以不做修改)

# 域名和记录信息
domain_name = 'example.com'  # 你的域名
sub_domain = 'www'  # 子域名，例如www

# 域名和记录信息
domain_name = 'sreout.com'  # 你的域名
record_id = '844942334267784192'  # 你的记录ID
sub_domain = 'me'  # 子域名，例如www

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']

def update_dns_record(client, record_id, sub_domain, ip):
    request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    request.set_RecordId(record_id)
    request.set_RR(sub_domain)
    request.set_Type('A')
    request.set_Value(ip)
    client.do_action_with_exception(request)


def main():
    client = AcsClient(access_key_id, access_key_secret, region_id)
    current_ip = None

    while True:
        new_ip = get_public_ip()
        if new_ip != current_ip:
            update_dns_record(client, record_id, sub_domain, new_ip)
            current_ip = new_ip
            print(f'Updated DNS record to {new_ip}')

if __name__ == '__main__':
    main()
