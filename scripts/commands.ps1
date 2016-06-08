echo Begin POC code > C:\Users\Administrator\cfy-deployment.txt


$ctx_path=Get-ChildItem -Path $env:USERPROFILE -Filter ctx -Recurse

&$ctx_path deployment id >> C:\Users\Administrator\cfy-deployment.txt


echo End POC code >> C:\Users\Administrator\cfy-deployment.txt
