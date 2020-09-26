import requests

url = 'https://api.bigdatahub.co.kr/v1/datahub/datasets/search.json?TDCAccessKey=a4c36cae89c772081ab678a908995a326d6339a514391d8fbbac1127643e9d34&pid=1002308'
response=requests.get(url=url).json()
#print(response.status_code)
print(response)



