from urllib.request import Request, urlopen
from urllib.parse import urlencode


url = 'http://passport2.chaoxing.com/fanyalogin'
args = {
    'uname': '15120001810',
    'password': '123456',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
}

f_data = urlencode(args)
print(f_data)

request = Request(url, headers=headers, data=f_data.encode())
response = urlopen(request)
print(response.read().decode())
