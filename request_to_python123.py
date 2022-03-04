import time

import requests
import json

# １指定ajax-post请求的url（通过抓包进行获取）
url = 'https://www.python123.io/api/v1/student/courses'



headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
    'Referer': 'https://www.python123.io/student/courses',
    'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtYWlsIjoiMTA0N------------fbG9naW4iOjE2NDYzODI5MjEyMDh9LCJpYXQiOjE2NDYzOTU0NzcsImV4cCI6MTY0NzY5MTQ3N30.SMQaYRuyCiLZHM4-QrFRoRjUfbSNBJCK0Nno2UtsKSg',
}
Cookie = "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7ImVtY-------3N30.SMQaYRuyCiLZHM4-QrFRoRjUfbSNBJCK0Nno2UtsKSg; io=voNHgr--NWDK0E"

cookies={
    i.split("=")[0]:i.split("=")[1] for i in Cookie.split(";")
}
# print(cookies)
for stu_id in range(1000,2000):
    time.sleep(0.5)
    data = {
        "code": "C989",
        "passcode": "",
        "student_id": stu_id,
        "name": "张军",
        # "email": "xx@qq.com"
    }
    response = requests.post(url=url, data=data, headers=headers,cookies=cookies)

    data = response.text
    data = json.loads(data)
    print('当前学号{}:  {}'.format(stu_id,data))
    if data['code']==201:
        print('成功！')
        break
