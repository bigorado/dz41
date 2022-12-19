import socket
import time
import datetime
import pprint
import json
import yaml

# set variables.
i = 1
wait = 2
srv = {'drive.google.com':'0.0.0.0', 'mail.google.com':'0.0.0.0', 'google.com':'0.0.0.0'}
init=0
fpath = "/root/dz41/"
flog  = "/root/dz41/error.log"

pprint.pprint("*"*33 + 'start script' + "*"*33)
pprint.pprint(srv)
pprint.pprint("*"*80)

while True :
  for host in srv:
    ip = socket.gethostbyname(host)
    if ip != srv[host]:
      is_error=True
      with open(flog,'a') as fl:
       print(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) +' [ERROR] ' + str(host) +' IP mistmatch: '+srv[host]+' '+ip)
      with open(fpath+host+".json",'w') as jsf:
          json_data= json.dumps({host:ip})
          jsf.write(json_data)
      with open(fpath+host+".yaml",'w') as ymf:
          yaml_data= yaml.dump([{host : ip}])
          ymf.write(yaml_data)
    if is_error:
      data = []
      for host in srv:
        data.append({host:ip})
      with open(fpath+"services_conf.json",'w') as jsf:
        json_data= json.dumps(data)
        jsf.write(json_data)
      with open(fpath+"services_conf.yaml",'w') as ymf:
        yaml_data= yaml.dump(data)
        ymf.write(yaml_data)
      srv[host]=ip
  i+=1
  if i >= 50 :
    break
  time.sleep(wait)

