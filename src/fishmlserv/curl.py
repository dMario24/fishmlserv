import requests

def get(l, w, k, url="http://localhost:8000/fish"):
    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': l,
        'weight': w,
        'k': k
    }

    response = requests.get(url, params=params, headers=headers)
    j = response.json()
    r = j.get("prediction")
    return r
