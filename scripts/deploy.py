import sys
import datetime
import urllib
import zipfile
from cloudify import ctx

fo = open("C:\Users\Administrator\Desktop\cfy-deployment.txt", "a")
fo.write("Begin POC code\n")
fo.write(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + "\n")
fo.write(ctx.deployment.id + "\n")

for arg in sys.argv[1:]:
    zf = "C:\Users\Administrator\Downloads\\" + arg.split('/')[-1]
    fo.write("Downloading " + arg + "\n")
    urllib.urlretrieve(arg, zf)
    zip = zipfile.ZipFile(zf)
    fo.write("Unzipping " + zf + "\n")
    zip.extractall()
    zip.close()

fo.write("End POC code\n")
fo.close()
