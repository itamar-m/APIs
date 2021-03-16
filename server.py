import requests
import json

try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
    response = requests.get('http://127.0.0.1:8080/GET_PROFILE')
    print(response.text)
    # response = requests.request('GET', 'https://api.github.com/events')
    data = response.json()
    print()
    print(data['name'])
    print(data['id'])
    print(data['role'])
    #print(len(data))

    # for i in range(len(data)):
    #    try:
    #        print(data[i])
    #    except KeyError:
    #        print(data[i]["id"] + " doesn't have action")
except json.JSONDecodeError:
    print('No JSON response')
