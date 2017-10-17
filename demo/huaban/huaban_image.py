# coding:utf-8
import Queue

import requests
import json
import BeautifulSoup
import re
import json
from study_utils import convert_radix
import time

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
    r = requests.get(url_home, headers=header)

    print r.cookies
    # print r.text


def down_img(down_url):
    """
    图片下载方法
    :return:
    """
    ir = requests.get('http://img.hb.aicdn.com/' + down_url, stream=True)
    if ir.status_code == 200:
        with open(str(count) + '.jpg', 'wb') as f:
            for chunk in ir:
                f.write(chunk)
    pass


def get_page(pin_id):
    global ascii_index
    global uuid
    t = int(round(time.time() * 1000))
    uid = convert_radix.convert(t)

    print uid

    if uuid == None:
        # 设置字符
        uuid = ord(uid[-1])
    print uuid

    randomStr = uid[0:uid.__len__() - 1] + str(chr(uuid))

    print randomStr

    url = 'http://huaban.com/boards/35618451/?' + randomStr+ '&' + str(pin_id) + '&limit=20&wfl=1'
    print url
    r = requests.get(url, headers=header)
    rex_str = r'app\.page\["board"\] = ({[\s|\S]*};\n)'
    print r.text
    page_content = re.findall(rex_str, r.text)[0][:-2]
    page = json.loads(page_content)
    pins = page['pins']
    page_id = pins[-1]['pin_id']
    print '页面id-->' + str(page_id)
    # uuid += 1
    for pin in pins:
        # 获取等待下载的图片
        global count
        count += 1
        print pin['file']['key']
        # 将图片存入队列中,让下载线程对图片进行下载操作
        q_image_urls.put(pin['file']['key'] + '_fw658')
        down_img(pin['file']['key'])

    uuid += 1
    # 递归调用
    get_page(page_id)


count = 0
uuid = None

if __name__ == '__main__':
    q_image_urls = Queue.Queue()
    # 首页 <input type="hidden" name="_xsrf" value="19ca8e6e0b47700665deb31b71b4ea15">
    get_page(35618451)
