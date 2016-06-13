import sys
import datetime
import urllib
import zipfile
from cloudify import ctx

dir = "C:\Users\Administrator\Downloads\\"
log = dir + "cfy-deployment.txt"

fo = open(log, "a", 1)
fo.write("Begin POC code\n")
fo.write(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + "\n")
fo.write(ctx.deployment.id + "\n")
fo.write(" ".join(sys.argv) + "\n")

for arg in sys.argv[1:]:
    zf = dir + arg.split('/')[-1]
    fo.write("Downloading " + arg + "\n")
    urllib.urlretrieve(arg, zf)
    zip = zipfile.ZipFile(zf)
    fo.write("Unzipping " + zf + "\n")
    zip.extractall(zf.split(".zip")[0])
    zip.close()

fo.write("End POC code\n")
fo.close()
