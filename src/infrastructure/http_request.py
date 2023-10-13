import requests

DEFAULT_HEADERS = {
    "Accept": "text/plain, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58",
}


def get(url):
    resp = requests.get(url, headers=DEFAULT_HEADERS, timeout=2)
    return resp
