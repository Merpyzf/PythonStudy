# -*- coding:utf-8 -*-
# 添加一个菜单
import requests


def create_menu():
    """
    自定义menu
    :return:
    """
    access_token_url = 'http://127.0.0.1:8080/get_token'
    resp = requests.get(access_token_url)

    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % resp.text
    print url

    post_json = """ 
{
    "button": [
        {
            "type": "click",
            "name": "今日歌曲",
            "key": "V1001_TODAY_MUSIC"
        },
        {
            "name": "菜单",
            "sub_button": [
                {
                    "type": "view",
                    "name": "搜索",
                    "url": "http://www.soso.com/"
                },
                {
                    "type": "click",
                    "name": "赞一下我们",
                    "key": "V1001_GOOD"
                }
            ]
        }
    ]
}
 
"""

    result = requests.post(url, data=post_json)
    print result.text


if __name__ == '__main__':
    create_menu()
