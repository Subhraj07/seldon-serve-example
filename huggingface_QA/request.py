import requests
import json

url = "http://20.195.38.158/seldon/seldon/seldon-pipeline/api/v0.1/predictions"

# payload = {'json': json.dumps(
#     {"data": {"names": ["message"], 
#               "ndarray": ["Manas is a good boy"]
#               }}
#     )}

payload = {'json': json.dumps(
    {"data": {"ndarray": ["Hi buddy"]
              }}
    )}

r = requests.post(url, data=payload)
print(r.json())

# curl -g http://20.195.38.158/seldon/seldon/seldon-pipeline/api/v0.1/predictions --data-urlencode 'json={"data": {"names": ["message"], "ndarray": ["Manas is a good boy"]}}' | json_pp