import json
from utils import Helper
helper = Helper()

if __name__ == '__main__':
    finger, cookies = helper.read_adapter_logs()
    print(cookies['Cookies'])


    def read_cookies():
        with open('cookies.txt', 'r') as file:
            content = file.read()

        return content


    # print(type(read_cookies()))
    print(type(cookies['Cookies']))
    print(type(read_cookies()))
    print(read_cookies() == cookies['Cookies'])
