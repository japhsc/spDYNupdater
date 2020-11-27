import json
import requests
from requests.auth import HTTPBasicAuth
import socket

update_addrs = 'YOUR_NIC.spdns.org'
update_token = 'YOUR-UPDATE-TOKEN'
update_spurl = 'https://update.spdyn.de/nic/update?hostname=%s&myip=%s'

lookup_dns = '2001:4860:4860::8844'
#lookup_dns = '8.8.8.8'
lookup_url = 'http://meineipv6.de/mro.php?format=json'

def pipecmd(cmd):
    import subprocess
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = ''
    while process.returncode is None:
        for line in process.stdout:
            result += line.decode('utf-8')
        # set returncode if the process has exited
        process.poll()
    return result

def getIP_DNS(addr, dns):
    #hostIP = socket.getaddrinfo(update_addrs, None, socket.AI_CANONNAME)
    ret = pipecmd('nslookup %s %s'%(addr, dns))
    lines = ret.split('\n')
    ip = lines[-3].replace('Address: ','')
    return ip.strip()
    
def getIP_URL(url):
    ip = ''
    r = requests.get(url)
    if (r.status_code == 200):
        data = r.json()
        ip = str(data['ipaddress'])
    else:
        print('Received Error Code')
    return ip

def updateIP(newip):
    updater = update_spurl%(update_addrs, newip)
    r = requests.get(updater, auth=HTTPBasicAuth(update_addrs, update_token))
    return r.text

def main():
    
    newip = getIP_URL(lookup_url)
    oldip = getIP_DNS(update_addrs, lookup_dns)
    
    #print(getIP_DNS('ipv4.google.com', lookup_dns))
    #print(getIP_DNS('ipv6.google.com', lookup_dns))
    
    print('dyndns  ip: ', oldip)
    print('current ip: ', newip)

    if newip == oldip:
        print('No update needed!')
    else:
        print('Update...')
        print(updateIP(newip))
        
if __name__ == '__main__':
    main()

