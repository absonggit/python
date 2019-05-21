from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

url = Request("https://baidu.com")
try:
    response = urlopen(url)
except HTTPError as e:
    print('Error code: ', e.code)
except URLError as e:
    print('Reason: ', e.reason)
else:
    print(response.read().decode("utf8"))