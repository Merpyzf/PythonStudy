# -*- coding:utf-8 -*-
# requests网络请求库的使用
import requests


if __name__ == '__main__':
    mz_url = 'http://www.mmjpg.com/'
    # 设置请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

    }
    r = requests.get(mz_url, headers=headers, stream=True)
    # 设置获取内容的编码
    r.encoding = 'UTF-8'
    print r.text
# append# append# append# append