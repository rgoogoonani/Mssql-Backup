import os

username = input("Mega UserName :")
while username=="":
    username = input("Mega UserName :")
print(username)
#-------------------------------------------------------------------
password=input("Mega Password : ")
while password=="":
    password=input("Mega Password : ")
print(password)
#-------------------------------------------------------------------
FileAddres=input("Server Name : ")
if FileAddres=="":
    FileAddres="Mssql"
print(FileAddres)
#-------------------------------------------------------------------
Name=input("File Addres : ")
if Name=="":
    Name="/var/opt/mssql"
print(Name)
with open("/MssqlBackup/config.txt","w") as f:
    f.writelines(username+"\n"+password+"\n"+Name+"\n"+FileAddres)


with open("/etc/systemd/system/MssqlAutoBackup.service","w") as f:
    f.writelines("[Unit]\nDescription=Mssql Auto Backup\n\n[Service]\nExecStart=/usr/bin/python3 /MssqlBackup/AutoBackup.py\n\n[Install]\nWantedBy=multi-user.target")
#f.writelines("[Unit]\nDescription=Mssql Auto Backup\n\n[Service]\nExecStart=screen /usr/bin/python3 "+str(os.path.abspath(__file__))+"\n\n[Install]\nWantedBy=multi-user.target")

os.system("sudo systemctl daemon-reload")
os.system("sudo systemctl start MssqlAutoBackup")
os.system("sudo systemctl enable MssqlAutoBackup")
