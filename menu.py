# version 1.0 - DAS 2022
# import all modules
import os
import random
import sys
import time
import requests
import wget
from colorama import Back, Fore
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# clean old proxy file https.txt and create new one
os.remove('https-downloaded.txt')
time.sleep(5)

(print())
print(Fore.RED + Back.BLACK + "Downloading from Proxy url")
print()

time.sleep(5)

# download proxy list from url
url = "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt"
wget.download(url, 'https-downloaded.txt')

# setting proxy file var  - https.txt is a custom - not automatic updated
#  errors may occure using the link above as proxy servers in the list are oftern down 
myproxy = 'https-downloaded.txt'


# define colors
class Bcolors:
    green = '\033[92m'
    WARNING = '\033[0;33m'
    FAIL = '\033[91m'
    enc = '\033[0m3'
    blue = '\033[94m'
    YELLOW = '\033[3;33m'
    CYAN = '\033[0;36'
    colors = ['\033[92m', '\033[91m', '\033[0;33m']
    RAND = random.choice(colors)


# logo
print(Bcolors.green + '$$$$$$$\  $$$$$$\  $$$$$$\        $$$$$$$\ $$$$$$$\  $$$$$$\  $$$$$$\  ')
print(Bcolors.green + '$$  __$$\$$  __$$\$$  __$$\       $$  __$$\$$  __$$\$$  __$$\$$  __$$\ ')
print(Bcolors.green + '$$ |  $$ $$ /  $$ $$ /  \__|      $$ |  $$ $$ |  $$ $$ /  $$ $$ /  \__|')
print(Bcolors.green + '$$ |  $$ $$$$$$$$ \$$$$$$\        $$ |  $$ $$ |  $$ $$ |  $$ \$$$$$$\  ')
print(Bcolors.green + '$$ |  $$ $$  __$$ |\____$$\       $$ |  $$ $$ |  $$ $$ |  $$ |\____$$\ ')
print(Bcolors.green + '$$ |  $$ $$ |  $$ $$\   $$ |      $$ |  $$ $$ |  $$ $$ |  $$ $$\   $$ |')
print(Bcolors.green + '$$$$$$$  $$ |  $$ \$$$$$$  |      $$$$$$$  $$$$$$$  |$$$$$$  \$$$$$$  |')
print(Bcolors.green + '\_______/\__|  \__|\______/       \_______/\_______/ \______/ \______/ ')
print()
print(Bcolors.RAND + '--- Agent being used---')

# setting up random userAgents
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
browser_options = Options()
userAgent = user_agent_rotator.get_random_user_agent()

print()
print(Bcolors.blue + userAgent)
print()

# creating random proxy primary
# storing IPs from file to list
proxy_list = []
with open(myproxy) as f:
    for line in f:
        # print(line)
        proxy_list.append(line.strip())
# storing functional IPs in a list
print(Bcolors.green + '--- WORKING PROXIES ---')
working_proxies = []
for i in proxy_list:

    try:
        proxy = ''
        ''

        response = requests.get('https://example.com', proxies=proxy)
        working_proxies.append(i)

        print(Fore.BLACK + Back.GREEN + i)

    except:
        pass

# rotating IPs from working_proxies considering we want to send 5 requests
for i in range(5):
    random_ip = random.choice(working_proxies)
    # rotating IPs from working_proxies
    proxy = random_ip

print()
print(Fore.RED + Back.BLACK + 'Please wait.. We are Testing all Proxies...')
print()

# creating random proxy 2
# storing IPs from file to list
proxy_list = []

# rotating IPs from working_proxies considering we want to send 5 requests
for i in range(5):
    random_ip2 = random.choice(working_proxies)
    # rotating IPs from working_proxies
    proxy = random_ip2

# creating random proxy 3
# storing IPs from file to list
proxy_list = []

# rotating IPs from working_proxies considering we want to send 5 requests
for i in range(5):
    random_ip3 = random.choice(working_proxies)
    # rotating IPs from working_proxies
    proxy = random_ip3

# creating random proxy 4
# storing IPs from file to list
proxy_list = []

# rotating IPs from working_proxies considering we want to send 5 requests
for i in range(5):
    random_ip4 = random.choice(working_proxies)
    # rotating IPs from working_proxies
    proxy = random_ip4



#  URLs
url = input(Fore.BLACK + Back.YELLOW + " Enter first site OPEN - include http:// >> ")
url2 = input(Fore.BLACK + Back.YELLOW + "Enter second site OPEN - include http:// >> ")
url3 = input(Fore.BLACK + Back.YELLOW + "Enter third site OPEN - include http:// >> ")
url4 = input(Fore.BLACK + Back.YELLOW + "Enter fourth site OPEN - include http:// >> ")



# browser 1 starting
s = Service('chromedriver.exe')
browser_options = Options()
browser_options.add_experimental_option("detach", True)
browser_options.add_argument('log-level=3')
PROXY = random_ip
browser_options.add_argument(f'user-agent={userAgent}')
browser_options.add_argument('--proxy-server=%s' % PROXY)
browser = webdriver.Chrome(service=s, options=browser_options)
browser.get(url)
sys.tracebacklimit = 0

# browser 2 starting
t = Service('chromedriver.exe')
browser_options = Options()
browser_options.add_experimental_option("detach", True)
browser_options.add_argument('log-level=3')
PROXY = random_ip2
browser_options.add_argument(f'user-agent={userAgent}')
browser_options.add_argument('--proxy-server=%s' % PROXY)
browser = webdriver.Chrome(service=t, options=browser_options)
browser.get(url2)
sys.tracebacklimit = 0

# browser 3 starting
z = Service('chromedriver.exe')
browser_options = Options()
browser_options.add_experimental_option("detach", True)
browser_options.add_argument('log-level=3')
PROXY = random_ip3
browser_options.add_argument(f'user-agent={userAgent}')
browser_options.add_argument('--proxy-server=%s' % PROXY)
browser = webdriver.Chrome(service=z, options=browser_options)
browser.get(url3)
sys.tracebacklimit = 0

# browser 4 starting
y = Service('chromedriver.exe')
browser_options = Options()
browser_options.add_experimental_option("detach", True)
browser_options.add_argument('log-level=3')
PROXY = random_ip4
browser_options.add_argument(f'user-agent={userAgent}')
browser_options.add_argument('--proxy-server=%s' % PROXY)
browser = webdriver.Chrome(service=y, options=browser_options)
browser.get(url4)
sys.tracebacklimit = 0
