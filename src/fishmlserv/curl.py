import requests

def get(l, w, url="http://localhost:8765/fish"):
    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': l,
        'weight': w,
    }

    response = requests.get(url, params=params, headers=headers)
    j = response.json()
    r = j.get("prediction")
    return r
