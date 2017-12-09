# -*- coding:utf-8 -*-

import requests

# 测试获取用户列表


def get_user_list():
    """
    获取用户列表
    :return:
    """
    token_url = 'http://127.0.0.1:8080/get_token'
    access_token = requests.get(token_url).text
    user_list_url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token=%s' % (access_token)
    resp = requests.get(user_list_url)
    print resp.text

def main():
    get_user_list()
    pass


if __name__ == '__main__':
    main()

    pass
