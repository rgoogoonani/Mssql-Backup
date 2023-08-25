import os

botToken = input("Bot Token :")
while len(botToken)<46 :
    botToken = input("invalid bot token try again: ")
print(botToken)
#-------------------------------------------------------------------
chid=input("Chatid : ")
while chid=="":
    chid = input("Chatid : ")
print(chid)
#-------------------------------------------------------------------
Name=input("Server Name : ")
print(Name)
#-------------------------------------------------------------------
FileAddres=input("File Addres : ")
if FileAddres=="":
    FileAddres="/var/opt/mssql"
print(FileAddres)
with open("/MssqlBackup/config.txt","w") as f:
    f.writelines(chid+"\n"+Name+"\n"+FileAddres+"\n"+botToken)


with open("/etc/systemd/system/MssqlAutoBackup.service","w") as f:
    f.writelines("[Unit]\nDescription=Mssql Auto Backup\n\n[Service]\nExecStart=/usr/bin/python3 /MssqlBackup/AutoBackup.py\n\n[Install]\nWantedBy=multi-user.target")
#f.writelines("[Unit]\nDescription=Mssql Auto Backup\n\n[Service]\nExecStart=screen /usr/bin/python3 "+str(os.path.abspath(__file__))+"\n\n[Install]\nWantedBy=multi-user.target")

os.system("sudo systemctl daemon-reload")
os.system("sudo systemctl start MssqlAutoBackup")
os.system("sudo systemctl enable MssqlAutoBackup")
