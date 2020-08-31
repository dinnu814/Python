import requests
urltocall=''
params={'courseType':'aws'}
response=requests.get(url=urltocall,params=params)
data=response.json()
print(date)