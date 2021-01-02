#!/usr/bin/python

import requests

user = input("Enter The Site: ")
try:
    if user.startswith('http') or user.startswith('https'):
        pass
    else:
        user = 'http://'+ user
    response = requests.get(user)
    with open("D:/Projects/Project-NE/CurlTool/file.html", 'wb') as f:
                #Path To Store the Ouput as a file.html
        f.write(response.content)
    print(response.content)
except Exception as e:
    print(e)