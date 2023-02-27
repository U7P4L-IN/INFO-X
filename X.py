#IMPORT

import time
import signal
import os
import sys
import webbrowser
from threading import Thread
import requests
import socket
from time import sleep
try:
	import requests
except:
	os.system("pip install requests")
	
#COLOUR

GREEN ='\x1b[38;5;46m'
RED = '\x1b[38;5;196m' 
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
BLACK="\033[1;30m"

public = requests.get("https://api.ipify.org").text
banner = (f"""
{GREEN} ┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
{GREEN} ┃ {WHITE} _____ _   _ ______ ____      __   __{GREEN} ┃
{GREEN} ┃ {WHITE}|_   _| \ | |  ____/ __ \     \ \ / /{GREEN} ┃
{GREEN} ┃   {WHITE}| | |  \| | |__ | |  | |_____\ V / {GREEN} ┃
{GREEN} ┃  {RED} | | | . ` |  __|| |  | |______> <  {GREEN} ┃
{GREEN} ┃  {RED}_| |_| |\  | |   | |__| |     / . \ {GREEN} ┃
{GREEN} ┃ {YELLOW}|_____|_| \_|_|    \____/     /_/ \_\{GREEN} ┃
{GREEN} ┃                                       ┃
{GREEN} └━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
""")
main_mnu = """
\033[1;91m [01]\033[1;97m Track IP Address
\033[1;91m [02]\033[1;97m Phone Number Info
\033[1;91m [03]\033[1;97m E-Mail Info
\033[1;91m [04]\033[1;97m More Tools
\033[1;91m [05]\033[1;97m Contract Me
\033[1;91m [00]\033[1;97m Exit
"""

os.system("xdg-open https://github.com/U7P4L-IN")

def ip():
    os.system('clear')
    print()
    time.sleep(0.5)
    print(banner)
    print()
    while True:
        ipad = input("\x1b[38;5;46m[\033[1;97m>\x1b[38;5;46m] Enter Target IP: ")

        if ipad == "":
            print()
            print(f"{RED}[!]{WHITE} No Input Detected")
            print()
            time.sleep(0.3)
        else:
            break

    ipr = requests.get("https://ipqualityscore.com/api/json/ip/pPiATkSdtLn3xgKW7a7HikZeZ4HMNa2R/" + ipad + "?strictness=0&allow_public_access_points=true&fast=true&lighter_penalties=true&mobile=true")
    print()
    time.sleep(1)
    print()
    print("\033[1;91m[~]\033[1;97m IP Details Are Given Down Below")
    print()
    print("\033[1;91m[×]\033[1;97m Target IP        : " + ipad )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m ASN              : " + str(ipr.json() ['ASN']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m ISP              : " + str(ipr.json() ['ISP']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Active TOR       : " + str(ipr.json() ['active_tor']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Active VPN       : " + str(ipr.json() ['active_vpn']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Country Code     : " + str(ipr.json() ['country_code']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Bot Status       : " + str(ipr.json() ['bot_status']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m City             : " + str(ipr.json() ['city']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Fraud Score      : " + str(ipr.json() ['fraud_score']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Host             : " + str(ipr.json() ['host']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Is Crawler       : " + str(ipr.json() ['is_crawler']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Latitude         : " + str(ipr.json() ['latitude']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Longitude        : " + str(ipr.json() ['longitude']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Message          : " + str(ipr.json() ['message']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Mobile           : " + str(ipr.json() ['mobile']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Organization     : " + str(ipr.json() ['organization']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Proxy            : " + str(ipr.json() ['proxy']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Recent Abuse     : " + str(ipr.json() ['recent_abuse']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Region           : " + str(ipr.json() ['region']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Request ID       : " + str(ipr.json() ['request_id']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Success          : " + str(ipr.json() ['success']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m TimeZone         : " + str(ipr.json() ['timezone']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m TOR              : " + str(ipr.json() ['tor']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m VPN              : " + str(ipr.json() ['vpn']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Zip Code         : " + str(ipr.json() ['zip_code']) )
    time.sleep(0.1)
    print("\033[1;91m[×]\033[1;97m Location         : https://maps.google.com/?q=" + str(ipr.json() ['latitude']) + "," + str(ipr.json() ['longitude']) )
    print()
    time.sleep(0.1)
    input(f"{GREEN}         Press ENTER To Continue")
    hack()

def mail():
	print()
	time.sleep(0.5)
	os.system("clear")
	print()
	print(banner)
	print()
	while True:
		em = input("\x1b[38;5;46m[\033[1;97m>\x1b[38;5;46m] Enter target E-mail: ")
		if em == '':
			print()
			print(f"{RED}[!]{WHITE} No input detected")
			print()
			time.sleep(0.4)
		else:
			break
	eml = requests.get("https://ipqualityscore.com/api/json/email/pPiATkSdtLn3xgKW7a7HikZeZ4HMNa2R/" + em )
	print()
	time.sleep(1)
	print()
	print("\033[1;91m[~]\033[1;97m E-mail Details are given down below")
	print()
	print("\033[1;91m[×]\033[1;97m Target E-mail       : " + em )
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Valid               : " + str(eml.json() ['valid']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Catch All           : " + str(eml.json() ['catch_all']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Common              : " + str(eml.json() ['common']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Deliverability      : " + str(eml.json() ['deliverability']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Disposable          : " + str(eml.json() ['disposable']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m DNS Valid           : " + str(eml.json() ['dns_valid']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Fraud Score         : " + str(eml.json() ['fraud_score']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Frequent Complainer : " + str(eml.json() ['frequent_complainer']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Generic             : " + str(eml.json() ['generic']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Honeypot            : " + str(eml.json() ['honeypot']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Leaked              : " + str(eml.json() ['leaked']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Message             : " + str(eml.json() ['message']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Over All Score      : " + str(eml.json() ['overall_score']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Recent Abuse        : " + str(eml.json() ['recent_abuse']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Request ID          : " + str(eml.json() ['request_id']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Sanitized E-mail    : " + str(eml.json() ['sanitized_email']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m SMTP Score          : " + str(eml.json() ['smtp_score']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Spam Trap Score     : " + str(eml.json() ['spam_trap_score']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Success             : " + str(eml.json() ['success']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Suggested Domain    : " + str(eml.json() ['suggested_domain']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Suspect             : " + str(eml.json() ['suspect']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Timed Out           : " + str(eml.json() ['timed_out']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m First Name          : " + str(eml.json() ['first_name']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Human               : " + str(eml.json() ['domain_age'] ['human']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m ISO                 : " + str(eml.json() ['domain_age'] ['iso']))
	time.sleep(0.1)
	print("\033[1;91m[×]\033[1;97m Time Stamp          : " + str(eml.json() ['domain_age'] ['timestamp']))
	time.sleep(0.1)
	print()
	input(f"{GREEN}         Press ENTER To Continue")
	hack()

def fon():
	print()
	time.sleep(0.5)
	os.system('clear')
	print(banner)
	print()
	phn = input("\x1b[38;5;46m[\033[1;97m>\x1b[38;5;46m] Enter Phone Number ( with country code ): ")
	print()
	if phn =='':
		print(f"{RED}[!]{WHITE} No input detected")
		print()
		hack()
	else:
		phe = requests.get("https://ipqualityscore.com/api/json/phone/pPiATkSdtLn3xgKW7a7HikZeZ4HMNa2R/" + phn )
		print()
		print("\033[1;91m[~]\033[1;97m Phone Number Details are given down below")
		print()
		print("\033[1;91m[×]\033[1;97m Target Number  : " + phn )
		print()
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Valid          : " + str(phe.json() ['valid']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m VOIP           : " + str(phe.json() ['VOIP']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Active         : " + str(phe.json() ['active']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Active Status  : " + str(phe.json() ['active_status']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Carrier        : " + str(phe.json() ['carrier']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m City           : " + str(phe.json() ['city']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Country        : " + str(phe.json() ['country']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Dialing Code   : " + str(phe.json() ['dialing_code']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Do Not Call    : " + str(phe.json() ['do_not_call']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Formatted      : " + str(phe.json() ['formatted']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Fraud Score    : " + str(phe.json() ['fraud_score']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Leaked         : " + str(phe.json() ['leaked']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Line Type      : " + str(phe.json() ['line_type']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Local Format   : " + str(phe.json() ['local_format']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m MCC            : " + str(phe.json() ['mcc']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Name           : " + str(phe.json() ['name']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Recent Abuse   : " + str(phe.json() ['recent_abuse']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Region         : " + str(phe.json() ['region']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Request ID     : " + str(phe.json() ['request_id']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Risky          : " + str(phe.json() ['risky']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m SMS Domain     : " + str(phe.json() ['sms_domain']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Spammer        : " + str(phe.json() ['spammer']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Success        : " + str(phe.json() ['success']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m TimeZone       : " + str(phe.json() ['timezone']))
		time.sleep(0.1)
		print("\033[1;91m[×]\033[1;97m Zip Code       : " + str(phe.json() ['zip_code']))
		time.sleep(0.1)
		print()
		input(f"{GREEN}         Press ENTER To Continue")
		time.sleep(0.1)
		print()
		hack()

def github():
	os.system("clear")
	print()
	print(banner)
	os.system("xdg-open https://github.com/U7P4L-IN")
	time.sleep(1.2)
	print()
	input(f"{GREEN}         Press ENTER To Continue")
	hack()
def fb():
	os.system("clear")
	print()
	print(banner)
	os.system("xdg-open https://github.com/U7P4L-IN")
	time.sleep(1.2)
	print()
	input(f"{GREEN}         Press ENTER To Continue")
	hack()
## Main code begin from here
def hack():
	try:
		os.system("clear")
		print(banner)
		print("\033[0;32m ░░░░░░\033[1;97m█ \033[0;32mCODING BY:",U7P4L IN,"\033[1;97m█\033[0;32m░░░░░░")
		print("\033[0;32m ░░░░░░\033[1;97m█ \033[0;32mYour IP:",public,"\033[1;97m█\033[0;32m░░░░░░")
		print(f"\t\n\t{BLACK}   ---> TOOL MEMU <--- ")
		print(main_mnu)
		mn = input(f"{GREEN} --> ")
		if mn == '':
			print()
			hack()
		elif mn == '1' or mn == '01':
			ip()
		elif mn == '2' or mn == '02':
			fon()
		elif mn == '3' or mn == '03':
			mail()
		elif mn == '4' or mn == '04':
			github()
		elif mn =='5' or mn =='05':
			fb()
		elif mn =='0' or mn =='00':
			print()
			exit()
		else:
			print()
			print("\x1b[38;5;46m[\033[1;97m>\x1b[38;5;46m] Invalid input")
			time.sleep(1)
			print()
	except:
		pass
hack()
