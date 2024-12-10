import requests

url = "http://192.168.43.132:9200/my_index/_doc"
data = {
    "username": "attacker",
    "action": "injection test"
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print("Data injection successful")
else:
    print(f"Failed to inject data. Status code: {response.status_code}")





