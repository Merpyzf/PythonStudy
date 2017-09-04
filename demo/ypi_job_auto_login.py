# coding:utf-8
import requests
import time
from bs4 import BeautifulSoup

# 功能: python模拟浏览器进行浏览题目，领取积分，并且记录每日的题目和答案以便日后考试时寻找答案出处
# version: 1.0
# date: 2017-9-4
# Author: wangke

# 模拟浏览器的请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

}
# 用户登陆的url
url_login = 'http://ypi.91job.gov.cn/user/login?callback=login'
# 首页的url
url_index = 'http://ypi.91job.gov.cn/contest/learn'
# cookie的键
cookie_key = 'PHPSESSID2'
# 字典用来存放cookie
cookies = {}


# 获取用户的用户名和密码
def get_user_cookie(user_name, pwd):
    r = requests.request('post', url=url_login, headers=headers,
                         data={'username': user_name, 'password': pwd, 'loginsubmit': '1'})

    # ajax异步登陆获取cookie，并返回
    return requests.request('post', url=url_login, headers=headers,
                            data={'username': user_name, 'password': pwd, 'loginsubmit': '1'}) \
        .cookies.get(cookie_key)


# 将html代码转换成BeautifulSoup对象返回
def get_html_doc(url):
    response_index = requests.request('get', url, cookies=cookies).text
    soup = BeautifulSoup(response_index, 'html.parser')
    return soup


# 将题目追加写入文件
def write_question2file(content_doc, num):
    try:
        file = open('record_question.txt', 'a')
        current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # print content_doc
        if num == 1:
            file.write((current_date + ":  ").encode('utf-8'))

        # 标题的div标签
        tag_title = content_doc.find('div', {'class': 'title'})

        # 题目的标题
        title = tag_title.b.text

        # 题目选项的div标签
        tag_answer = content_doc.find('div', {'class': 'answer'})

        # 题目的选项
        answers = tag_answer.ul.text

        # 问题正确答案的div标签
        tag_right = content_doc.find('div', {'class': 'right'})

        # 正确答案
        right = tag_right.text

        str = title + answers + right

        file.write(str.encode('utf-8'))

    except AttributeError as e:
        print('html页面解析遇到了点问题,sorry啦！请手动登录 O(∩_∩)O哈哈~')


# 主方法
def main(user_name, pwd):
    try:
        cookies[cookie_key] = get_user_cookie(user_name, pwd)
        # 获取内容
        content_doc_1 = get_html_doc(url_index).find('div', {'class': 'all'})

        print '学号' + user_name
        print content_doc_1.div.contents[1].string
        # 中间存在一个换行符
        print content_doc_1.div.contents[3].string
        print '题目浏览中……'
        # 貌似无意义~~~~(>_<)~~~~ 的浏览第二个题目，因为好像只要登录就能获取积分
        get_html_doc(url_index + '?page=2')

        # 每个人的题目都是一样的，因此题目只需要记录一份
        if user_name[8::] == '01':
            # 将第一页中的题目写入文件
            write_question2file(content_doc_1, 1)
            # 将第二页中的题目写入文件
            write_question2file(get_html_doc(url_index + '?page=2').find('div', {'class': 'all'}), 2)

    except AttributeError as e:
        print('html页面解析遇到了点问题,sorry啦！请手动登录 O(∩_∩)O哈哈~')


if __name__ == '__main__':

    for n in range(1, 49):
        user_id = '15053102'
        if n < 10:
            user_id = '150531020' + str(n)
        else:
            user_id = user_id + str(n)
        # 网站没有做防爬虫处理，不需要进行休眠
        # time.sleep(1000)
        main(user_id, user_id[4::])
