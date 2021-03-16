import requests
import json

try:
    response = requests.get('http://127.0.0.1:8080/GET_PROFILE')
    print(response.text)
    data = response.json()
    print()
    print(data['name'])
    print(data['id'])
    print(data['role'])

    # for i in range(len(data)):
    #    try:
    #        print(data[i])
    #    except KeyError:
    #        print(data[i]["id"] + " doesn't have action")
except json.JSONDecodeError:
    print('No JSON response.')
except KeyError:
    print('Bad dict access.')
