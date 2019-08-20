import os
import time

os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
time.sleep(10)
print("before")
time.sleep(5)
exec(open("get-pip.py").read());
