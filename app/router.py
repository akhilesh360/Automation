import requests

def send_to_zapier(data, webhook_url):
    response = requests.post(webhook_url, json=data)
    return response.status_code
