import requests
from requests.auth import HTTPBasicAuth

# {'password': 'ktotama', 'path': 'submissions/super/duper/secret/', 'instructions':
#     'Сделайте PUT запрос на тот же хост, но на '
#     'path указанный в этом документе c логином и паролем из этого документа.
#     Логин и пароль также передайте в заголовке Authorization.', 'login': 'galchonok'}

# req = requests.post("https://datasend.webpython.graders.eldf.ru/submissions/1/", headers={
#     "Authorization" : "Basic",}, auth=('alladin', 'opensesame'))
if __name__ == '__main__':
    req = requests.put("https://datasend.webpython.graders.eldf.ru/submissions/super/duper/secret/", headers={
        'Authorization': 'Basic'
    }, auth=('galchonok', 'ktotama'))

    print(req.text)

