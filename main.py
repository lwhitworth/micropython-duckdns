import urequests
import machine
import time

domains = ['DOMAIN1', 'DOMAINx']
token = 'YOUR_DUCKDNS_TOKEN'

def update_duckdns():
    global domains, token
    duck_url = 'http://www.duckdns.org/update?domains=%s&token=%s&ip='
    domains = ','.join(domains)
    duck_url = duck_url % (domains, token)
    response = urequests.get(duck_url)
    return response.text

if __name__ == '__main__':
    print(update_duckdns())
    time.sleep(2)
    machine.deepsleep(300000) # sleep for 5 minutes