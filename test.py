import os
try:
    import mega
except:
    os.system("pip3 install mega.py")
    from mega import Mega

mega = Mega()
m = mega.login("reza.g.g.ir@gmail.com", "kH8C8Ypt.tgskyq")
