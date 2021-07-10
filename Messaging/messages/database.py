import time
import requests
import json
import string
import random

def tokengen():
    url = 'https://cheetah-api.builderall.com/api/login'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:78.0) Gecko/20100101 Firefox/78.0'}
    r = requests.post(url, json={'email': 'hadjiamar.mani@gmail.com' , 'password': 'eyJpdiI6Imx4ZzlPZ0tDalpnUnE5alhcL2VoaUpBPT0iLCJ2YWx1ZSI6ImZyQjU5aWFYUkEyZkVBK3BMYnJMYlJHQTJwdXRWSTZCK3ZNdjFPZzE1K0k9IiwibWFjIjoiMGZmODVlMGNkZDFjYzNjOTM2MmI5YjRjOTZmNzRlMTM2NzI1ODcxZGFmOTY2NDI0ZjdmMDE3ZTk1MzA1OTQ3MiJ9'}, headers=headers)
    response = json.loads(r.text)
    print('Retrieving Account Info')
    token = response['token']
    return token

def deamoncon():
    url = 'https://cheetah-api.builderall.com/api/domain/connect'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:78.0) Gecko/20100101 Firefox/78.0', 'Authorization': 'Bearer %s'%token}
    r = requests.post(url, json={'name': '%s.%s'%(name, domainname) , 'region': '101', 'encrypted_id': '%s'%encid}, headers=headers)
    response = json.loads(r.text)
    print(response)
    print('Connected to %s.%s'%(name, domainname))

def newsub():
    alphanumiric = string.ascii_lowercase + string.digits
    name = ''.join(random.choice(alphanumiric) for i in range(4))
    print('using %s.%s as a subdomain name'%(name, domainname))
    return name

def deamondis():
    url = 'https://cheetah-api.builderall.com/api/domain/disconnect'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:78.0) Gecko/20100101 Firefox/78.0', 'Authorization': 'Bearer %s'%token}
    r = requests.post(url, json={'name': '' , 'region': '101', 'encrypted_id': '%s'%encid}, headers=headers)
    response = json.loads(r.text)
    print(response)
    print('\nDomain Disconnected Succesfully')

domainname = 'dollreview.net'
token = tokengen()

with open ('websites.txt', 'r') as enc_file:
    for encid in enc_file:
        print('disconnecting domain')
        deamondis()
        time.sleep(10)
        name = newsub()
        time.sleep(1)
        deamoncon()
        outd = open('subdomains.txt', 'a')
        subdomain = '%s.%s\n'%(name, domainname)
        outd.write(subdomain)
        time.sleep(1)
        print('\nMoving to the next subdomain\n')
        outd.close()
print('Added 10 new subdomains')