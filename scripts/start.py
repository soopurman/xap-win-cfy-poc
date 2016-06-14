import subprocess
from cloudify import ctx
from cloudify.state import ctx_parameters as inputs

app_name = inputs['app_name']
space = inputs['space']
xap_master_ip = inputs['xap_master_ip']
group = inputs['group']

dir = "C:\GigaSpaces\\" + ctx.instance.id + "\\"
app_out = dir + app_name + "_out.txt"
app_err = dir + app_name + "_err.txt"
exe = dir + app_name + "\\" + app_name + ".exe"
url = "jini://*/*/" + space + "?locators=" + xap_master_ip + "&groups=" + group
opts = ["NIO", "100"]
DETACHED_PROCESS = 0x00000008

subprocess.Popen([exe, url] + opts, shell=False, cwd=dir+app_name, stdin=None, stdout=open(app_out, 'a'), stderr=open(app_err, 'a'), creationflags=DETACHED_PROCESS)
