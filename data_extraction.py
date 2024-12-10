import requests

target_url = "http://192.168.43.132:9200/_search"
query = {
    "size": 10,
    "query": {
        "match_all": {}
    }
}

response = requests.get(target_url, json=query)
if response.status_code == 200:
    print("Data extracted:", response.json())
else:
    print("Failed to retrieve data.")


