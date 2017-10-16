# coding:utf-8
import requests
import json
import BeautifulSoup

# 伪造请求头
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
}


def get_login_params(url_home):
    '''
    获取模拟登陆时登陆必须的参数
    :param url_home:
    :return:
    '''
    r = requests.get(url_home,headers=header)
    
    print r.cookies
    # print r.text





if __name__ == '__main__':

    # 首页 <input type="hidden" name="_xsrf" value="19ca8e6e0b47700665deb31b71b4ea15">
    url_home = 'http://huaban.com/boards/35618451/'

    r = requests.get(url_home, headers = header)

    print r.text
