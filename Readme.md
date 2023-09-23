## Script for implementing dynamic DNS with Alibaba Cloud.


#### Check public IP addresses and update DNS records

> This script will obtain the public IP of this server and modify the A record of the corresponding DNS resolution in Alibaba Cloud.
>
> - Very suitable for home networks, the public IP will also be synchronized and updated to Aliyun DNS resolution when changed.
> - If you manually modify the DNS resolution by mistake, you will also perform IP comparison and modify the dns resolution.

1、Download dependency package.

```shell
pip3 install requests
pip3 install aliyun-python-sdk-core
pip3 install aliyun-python-sdk-alidns
```

2、Modify configuration.

```ini
# Alibaba Cloud API Credentials
access_key_id = 'your_access_key_id'
access_key_secret = 'your_access_key_secret'
region_id = 'cn-hangzhou'  # 你的阿里云区域ID(可以不做修改)

# Domain name and record information.
domain_name = 'example.com'  # your domain
sub_domain = 'www'   # Subdomain, for example：www
```

3、Run script.

```shell
python3 get_ip_dns.py
```

