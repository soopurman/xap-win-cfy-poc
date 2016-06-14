import os
import datetime
import urllib
import zipfile
from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

dir = os.path.normcase("C:/GigaSpaces/" + ctx.instance.id)
log = os.path.normcase(dir + "/cfy-deployment.txt")
license = "xap-license.txt"
lic_dir = os.path.normcase("C:/GigaSpaces/XAP.NET-11.0.0-x64/Runtime")

try:
    os.makedirs(dir)
except os.error:
    pass

fo = open(log, "a", 1)
fo.write(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + " Beginning deployment\n")

for name in inputs['downloads_names'].split():
    zf = name + inputs['downloads_rev-ext']
    dst = os.path.normcase(dir + "/" + zf)
    src = inputs['downloads_base'] + zf
    fo.write("Downloading " + src + "\n")
    urllib.urlretrieve(src, dst)
    zip = zipfile.ZipFile(dst)
    fo.write("Unzipping " + dst + "\n")
    zip.extractall(os.path.normcase(dir + "/" + name))
    zip.close()

urllib.urlretrieve(inputs['downloads_base'] + license, os.path.normcase(lic_dir + "/" + license))

fo.write(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + " Completed deployment\n")
fo.close()
