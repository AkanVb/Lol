import json
import requests
#access_token": "
headers = {"Authorization": "Bearer ya29.a0AfH6SMAEToxQV7MNqdVVi0satE2NQhG4JWxAyU-NqaHU5dO-9g2BJ0TWLoEnmK5wTYB9nmIiehNe3T29h1kpg6ALIV77KEx2tJ7PhR6yjlNUVTA0YCJjYIr6iid-rzywa2r_Z3M3Mt5GYz6Uk3lvOOPQiO8X"}
para = {
    "name":"test",
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("./DCIM.zip", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)
