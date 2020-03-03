import requests as rq

response = rq.get('https://api.github.com')

if response.status_code == 220:
    print('Success')
elif response.status_code == 404:
    print('Not Found')