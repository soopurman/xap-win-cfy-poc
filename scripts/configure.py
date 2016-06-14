import datetime
import urllib
import zipfile
from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

dir = "C:\GigaSpaces\\" + ctx.instance.id + "\\"
log = dir + "cfy-deployment.txt"
license = "xap-license.txt"
lic_dir = r"C:\GigaSpaces\XAP.NET-11.0.0-x64\Runtime"

fo = open(log, "a", 1)
fo.write(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + " Beginning deployment\n")

for name in inputs['downloads_names'].split():
    zf = name + inputs['downloads_rev-ext']
    dst = dir + zf
    src = inputs['downloads_base'] + zf
    fo.write("Downloading " + src + "\n")
    urllib.urlretrieve(src, dst)
    zip = zipfile.ZipFile(dst)
    fo.write("Unzipping " + dst + "\n")
    zip.extractall(dir + name)
    zip.close()

urllib.urlretrieve(inputs['downloads_base'] + license, lic_dir + "\\" + license)

fo.write(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + " Completed deployment\n")
fo.close()
