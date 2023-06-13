import requests
HOST= 'http://127.0.0.1:8000'
res= requests.post(HOST + '/api-token-auth/', {
    'username': 'admin',
    'password': '1234',
})

res.raise_for_status()
token= res.json()['token']
print(token)

headers= {'Authorization': 'JWT '+ token, 'Accept': 'application/json'}

# Post 
Createdata= {'title': '제목by code', 
             'text': 'API내용by code', 
             'created_date': '2022-06-07T18:34:00+09:00', 
             'published_date': '2022-06-07T18:34:00+09:00'
             }

file = {'image': open('Users/slee/intruder.jpg', 'rb')}
res= requests.post(HOST+ '/api_root/Post/', data=data, files=file, headers=headers)
print(res)
print(res.json())