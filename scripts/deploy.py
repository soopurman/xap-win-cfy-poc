import datetime
import urllib
import zipfile
from cloudify import ctx

dir = "C:\Users\Administrator\Downloads\\"
log = dir + "cfy-deployment.txt"

fo = open(log, "a", 1)
fo.write(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + " Beginning deployment\n")

for name in ctx.node.properties['downloads_names'].split():
    zf = name + ctx.node.properties['downloads_rev-ext']
    dst = dir + zf
    src = ctx.node.properties['downloads_base'] + zf
    fo.write("Downloading " + src + "\n")
    urllib.urlretrieve(src, dst)
    zip = zipfile.ZipFile(dst)
    fo.write("Unzipping " + dst + "\n")
    zip.extractall(dir + name)
    zip.close()

fo.write(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + " Completed deployment\n")
fo.close()
