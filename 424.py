##!/usr/bin/env python3

import socket
import time
import datetime
import pprint

# set variables 
i = 1
wait = 2
srv = {'drive.google.com':'0.0.0.0', 'mail.google.com':'0.0.0.0', 'google.com':'0.0.0.0'}
init=0

pprint.pprint("*"*33 + 'start script' + "*"*33)
pprint.pprint(srv)
pprint.pprint("*"*80)

while True :
  for host in srv:
    ip = socket.gethostbyname(host)
    if ip != srv[host]:
      print(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) +' [ERROR] ' + str(host) +' IP mistmatch: '+srv[host]+' '+ip)
      srv[host]=ip
  i+=1
  if i >= 50 :
    break
  time.sleep(wait)