import shutil 
import os.path
import os
import json
import time
import os
try:
    import mega
except:
    os.system("pip3 install mega.py")
    from mega import Mega
import urllib3
urllib3.disable_warnings()

lines = ""
with open("/MssqlBackup/config.txt","r+") as f :
    lines=f.read().split("\n")
    lines=[i.replace("\r","") for i in lines]
username=lines[0]
password = lines[1]

FileAddres=lines[2]
spl1=FileAddres.split("/")

Name=lines[3]

t=len(spl1)-1
FileName=spl1[t]
print(username)
print(password)
print(FileAddres)
print(Name)

mega = mega.Mega()
def ReplaceFile(filename,folder,username, password):
    
    m = mega.login(username, password)
    if len(m.get_files())>50:
        files = m.find(folder)
        if files:
            m.delete(files[0])
    m.create_folder(folder)
    folder = m.find(folder)

    m.upload(filename, folder[0])
#-------------------------------------------------------------------
def upload():
    
    if os.path.exists('/MsSql.zip'):
        os.remove("/MsSql.zip")
    
    archived = shutil.make_archive('/MsSql', 'zip', FileAddres)

    if os.path.exists('/MsSql.zip'):
        ReplaceFile('/MsSql.zip',Name+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),username, password)
        #requests.get(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={chid}&caption=SQL Server Name : {Name}",files={'document': (FileName, open("/MsSql.zip", 'rb'))})
        print("uploaded")
    else: 
        print("ZIP file not created")

while True:
    try:
        upload()
    except:
        print()
    time.sleep(300)
