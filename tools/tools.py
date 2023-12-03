import requests
from json import dumps

chainbase_key = ""

def fetch_from_factory(chain_name, factory):
    query = "select address from " + chain_name + ".contracts where from_address like '" + factory.lower() + "'"

    try:
        resp = requests.post(
            "https://api.chainbase.online/v1/dw/query",
            headers={
                "accept": "application/json",
                "x-api-key": chainbase_key,
                "content-type": "application/json"
            },
            data=dumps({"query": query})
        )
        if resp.status_code != 200:
            return []

        resp = resp.json()
        return resp['data']['result']
    except:
        return []