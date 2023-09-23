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

---



#### 检查公网IP并更新 DNS 纪录

> 此脚本将获取该服务器的公网IP，并且修改阿里云对应的DNS解析的A纪录。
>
> - 非常适用于家用网络，公网IP改变时也会同步修改至Aliyun dns解析
> - 手动误修改此DNS解析时，也会进行操作IP对比，同时进行修改 dns 解析

1、下载依赖包

```shell
pip3 install requests
pip3 install aliyun-python-sdk-core
pip3 install aliyun-python-sdk-alidns
```

2、修改配置

```ini
# 阿里云API凭证
access_key_id = 'your_access_key_id'
access_key_secret = 'your_access_key_secret'
region_id = 'cn-hangzhou'  # 你的阿里云区域ID(可以不做修改)

# 域名和记录信息
domain_name = 'example.com'  # 你的域名
sub_domain = 'www'  # 子域名，例如www
```

3、运行脚本

```shell
python3 get_ip_dns.py
```

