#encoding:utf8

import requests
import json


# 保存参数
params = {}

# 建立一个请求会话
session = requests.session()
# 先授权
result = session.post('http://www.testingedu.com.cn/inter/HTTP/auth',data={})

# print(result.text)
# 解析json
jsonres = json.loads(result.text)
# 断言，判断相等
if jsonres['status']==200:
    print('授权：PASS!')
else:
    print('授权：FAIL')
    print(result.text)
#保存token
params['token'] = jsonres['token']
# 添加token到请求头
session.headers['token'] = params['token']
print(session.headers)

# 请求登录
d = {'username':'will101','password':'123456'}
result = session.post('http://www.testingedu.com.cn/inter/HTTP/login',data=d)
print(result.text)
# 解析json
jsonres = json.loads(result.text)
# 断言，判断相等
if jsonres['status']==200:
    print('登录：PASS!')
    params['id'] = jsonres['userid']
else:
    print('登录：FAIL')
    print(result.text)

# 请求用户信息
d = {'id':params['id']}
result = session.post('http://www.testingedu.com.cn/inter/HTTP/getUserInfo',data=d)
print(result.text)
# 解析json
jsonres = json.loads(result.text)
# 断言，判断相等
if jsonres['status']==200:
    print('登录：PASS!')
else:
    print('登录：FAIL')
    print(result.text)

# 注销
result = session.post('http://www.testingedu.com.cn/inter/HTTP/logout',data={})
# print(result.text)
# 解析json
jsonres = json.loads(result.text)
# 断言，判断相等
if jsonres['status']==200:
    print('注销：PASS!')
else:
    print('注销：FAIL')
    print(result.text)



