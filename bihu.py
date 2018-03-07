# coding=utf8
import copy
import json

import requests

post_token = {"accessToken": None, "userId":None}

baseUrl = "https://be02.bihu.com/bihube-pc/api"

headers_base = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Host': 'be02.bihu.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Referer': 'https://bihu.com/login',
        'origin': 'https://bihu.com'
    }

session = requests.session()


def login(phone, password):
    post_data = {
            'password': password,
            'phone': phone,
    }

    #登录的URL
    url = baseUrl + "/user/loginViaPassword"
    #requests 的session登录，以post方式，参数分别为url、headers、data
    content = session.post(url, headers=headers_base, data=post_data, verify=False)

    print content.text
    d = json.loads(content.text)
    post_token['accessToken'] = d['data']["accessToken"]
    post_token['userId'] = d['data']["userId"]
    print post_token
    #再次使用session以get去访问首页，一定要设置verify = False，否则会访问失败
    #s = session.get("https://bihu.com/", verify = False)
    #print s.text.encode('utf-8')
    #把爬下来的首页写到文本中
    #f = open('mycomments.txt', 'w')
    #f.write(s.text.encode('utf-8'))


def hot_art_list():
    post_data = copy.copy(post_token)
    url = baseUrl + "/content/show/hotArtList"
    content = session.post(url, headers=headers_base, data=post_data, verify=False)
    print content.text


def up_vote(art_id):
    post_data = copy.copy(post_token)
    post_data['artId'] = art_id
    url = baseUrl + "/content/upVote"
    content = session.post(url, headers=headers_base, data=post_data, verify=False)
    print content.text


def create_comment(art_id, content):
    post_data = copy.copy(post_token)
    post_data['artId'] = art_id
    post_data['content'] = content
    post_data['rootCmtId'] = None
    post_data['commentId'] = None
    url = baseUrl + "/content/createComment"
    content = session.post(url, headers=headers_base, data=post_data, verify=False)
    print content.text


#查看文章是否存在，若不存在，返回None, 否则返回用户article
def get_article(art_id):
    post_data = copy.copy(post_token)
    post_data['artId'] = art_id
    url = baseUrl + "/content/show/getArticle"
    content = session.post(url, headers=headers_base, data=post_data, verify=False)
    print content.text
    return json.loads(content.text)


def get_unlogin_article(art_id):
    post_data = {"accessToken": None, "userId": None, "artId": art_id}
    url = baseUrl + "/content/show/getArticle"
    content = requests.post(url, headers=headers_base, data=post_data, verify=False)
    print content.text
    return json.loads(content.text)


#进行登录，将星号替换成你的登录邮箱和密码即可
#密码发到币乎之前会被加密，浏览器post的时候看postbody里面的password填入这儿，注意这里使用密码登陆而不是验证码
login("yourphone","02eba44686463071dc1d4b209c90c35501579059326647bae9c0c17de8f8173x")

