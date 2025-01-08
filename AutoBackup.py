import shutil
import os
import time
from mega import Mega
import urllib3

urllib3.disable_warnings()

# خواندن اطلاعات کانفیگ
lines = ""
with open("/MssqlBackup/config.txt", "r+") as f:
    lines = f.read().split("\n")
    lines = [i.replace("\r", "") for i in lines]
username = lines[0]
password = lines[1]
FileAddres = lines[2]
spl1 = FileAddres.split("/")
Name = lines[3]

FileName = spl1[-1]
print(username)
print(password)
print(FileAddres)
print(Name)

mega = Mega()

def safe_login(username, password, retries=5, delay=10):
    """Login to Mega with retries."""
    for attempt in range(retries):
        try:
            return mega.login(username, password)
        except Exception as e:
            print(f"Login failed: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
    raise Exception("Failed to login to Mega after multiple attempts.")

def DeleteFile(username, password, folder):
    try:
        m = safe_login(username, password)
        getfile = m.get_files()

        if len(getfile) > 150:
            for item in getfile.items():
                if folder in str(item[1]['a']['n']):
                    files = m.find(item[1]['a']['n'])
                    if files:
                        m.destroy(files[0])
                    return
    except Exception as e:
        print(f"Error in DeleteFile: {e}")

def ReplaceFile(filename, folder, username, password):
    try:
        DeleteFile(username, password, folder + " " + time.strftime("%Y-%m", time.gmtime()))
        print("Deleted")
        m = safe_login(username, password)
        folder = folder + " " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        m.create_folder(folder)
        folder = m.find(folder)
        m.upload(filename, folder[0])
    except Exception as e:
        print(f"Error in ReplaceFile: {e}")

def upload():
    try:
        if os.path.exists('/MsSql.zip'):
            os.remove("/MsSql.zip")

        archived = shutil.make_archive('/MsSql', 'zip', FileAddres)
        print("Zip created")
        if os.path.exists('/MsSql.zip'):
            ReplaceFile('/MsSql.zip', Name, username, password)
            print("Uploaded")
        else:
            print("ZIP file not created")
    except Exception as e:
        print(f"Error in upload: {e}")

while True:
    try:
        upload()
    except Exception as e:
        print(f"Unexpected error: {e}")
    time.sleep(300)
