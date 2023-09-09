import shutil 
import os.path
import os
import json
import time
try:
    import  requests
except:
    os.system("pip3 install requests")
    import  requests
import urllib3
urllib3.disable_warnings()

lines = ""
with open("/MssqlBackup/config.txt","r+") as f :
    lines=f.read().split("\n")
    lines=[i.replace("\r","") for i in lines]
chid=lines[0]
Name=lines[1]
FileAddres=lines[2]
spl1=FileAddres.split("/")
token = lines[3]
t=len(spl1)-1
FileName=spl1[t]

#-------------------------------------------------------------------
def upload():
    if os.path.exists('/MsSql.zip'):
        os.remove("/MsSql.zip")
    
    archived = shutil.make_archive('/MsSql', 'zip', FileAddres)

    if os.path.exists('/MsSql.zip'):
        requests.get(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={chid}&caption=SQL Server Name : {Name}",files={'document': (FileName, open("/MsSql.zip", 'rb'))})
        print("uploaded")
    else: 
        print("ZIP file not created")
    
while True:
    try:
        upload()
    except:
        print()
    time.sleep(60)
