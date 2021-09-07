import requests

url = 'http://192.168.1.81'
res = requests.get(url)

time_elapsed = res.elapsed.total_seconds()
print('time_elapsed:', time_elapsed)
