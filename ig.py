import requests, json
from datetime import datetime

def login(_username, _password):
    link = 'https://www.instagram.com/accounts/login/'
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    
    time = int(datetime.now().timestamp())
    response = requests.get(link)
    csrf = response.cookies['csrftoken']

    payload = {
        'username': _username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{_password}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    }

    login_response = requests.post(login_url, data=payload, headers=login_header)
    json_data = json.loads(login_response.text)

    if json_data["authenticated"]:
        print("login successful")
        cookies = login_response.cookies
        cookie_jar = cookies.get_dict()
        print(f"Cookie : {cookie_jar}")
    else:
        print("login failed ", login_response.text)


if __name__=='__main__':
    input_username = input('Input Username : ')
    input_password = input('Input Password : ')
    login(input_username, input_password)
