from flask import requests 

api_key='f874cf58-4e9f-4de4-8b0f-0afca5c30f17'
email_address = 'kammarivinay26@gmail.com'

r=requests.get('https://isitarealemail.com/api/email/validate',params={'email':email_address},
headers={'Authorization':'Bearer'+api_key})

st=r.json()['status']

if st=='valid':
    print('It is Valid')
else:
    print('It is Not Valid')