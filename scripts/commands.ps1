$ctx_path=Get-ChildItem -Path $env:USERPROFILE -Filter ctx -Recurse
&$ctx_path deployment id > C:\Users\Administrator\cfy-deployment-id.txt
