import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = 'johndungao123'
TOKEN = 'asg23sadf144fegd2'
GRAPH_ID = 'graph1'
user_params = {
    'token': 'asg23sadf144fegd2',
    'username': 'johndungao123',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'km',
    'type': 'float',
    'color': 'shibafu'
}
headers = {
    'X-USER-TOKEN': TOKEN
}
today = datetime.today()
user_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
graph_create_pixel = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '5.4'
}



response = requests.post(url=user_graph_endpoint, json=graph_create_pixel, headers=headers)
print(response.text)