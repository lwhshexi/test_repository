import json
import re

from DrissionPage.errors import ElementNotFoundError

json_data = []


def get_part(page, i, a1, a2):
    """

    :param page:
    :param i: 这里可以忽略
    :param a1:
    :param a2:
    :return:
    """
    last_url = 'https://www.xiaohongshu.com/explore/' + a1 + '?xsec_token=' + a2 + '&xsec_source=pc_search'
    print(f'第{i}个数据：', last_url)
    page.get(last_url)
    a = page.ele('xpath://span[@class="username" and @data-v-1c93c041=""]').text  # 作者
    b = page.ele('xpath://div[@id="detail-title" and @class="title"]').text  # 笔记标题
    c = page.ele('xpath://span[@class="note-text" and @data-v-cd6ca71e=""]').text  # 笔记内容
    d = page.eles('xpath://span[@class="count" and @data-v-e5195060=""]')
    d = d[len(d) - 1].text  # 点赞数
    e = page.ele('xpath://span[@class="count" and @data-v-502c7b76=""]').text  # 收藏数
    f = page.ele('xpath://span[@class="count" and @data-v-3eeaf146=""]').text  # 评论数

    headers = ('作者', '笔记标题', '笔记内容', '点赞数', '收藏数', '评论数', '笔记链接')
    print(f'目前爬取第: {i}组数据')
    entry = {
        headers[0]: a,  # 作者
        headers[1]: b,  # 笔记标题
        headers[2]: c,  # 笔记内容
        headers[3]: d,  # 点赞数
        headers[4]: e,  # 收藏数
        headers[5]: f,  # 评论数
        headers[6]: last_url  # 笔记链接
    }
    json_data.append(entry)
    with open('xhs_bj.json1', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    print(f'第{i}组数据爬取成功！')


def get_last_url(page, res_response_body, count):
    """
    :param count: 记录爬取第几个notes
    :param page: 打开网页的实例
    :param res_response_body: 抓包的body内容
    :return:
    """
    a, b, c, d, e = '', '', '', '', ''  # a.作者 b.笔记标题 c.笔记内容 d.点赞 e.收藏 f.评论
    data = res_response_body
    a = []
    print('data总共长度为：', len(data['data']['items']))
    for i in range(len(data['data']['items'])):
        a1, a2 = data['data']['items'][i]['id'], data['data']['items'][i]['xsec_token']
        if re.match(r'^[a-zA-Z0-9]+$', a1):  # 判断id是否为数字加字母组合
            last_url = 'https://www.xiaohongshu.com/explore/' + a1 + '?xsec_token=' + a2 + '&xsec_source=pc_search'
            print(last_url)
            with open('last_url.txt', 'a', encoding='utf-8') as f:
                f.write(last_url + '\n')
            # get_part(page, i, a1, a2)
        else:
            a.append(f'第{i}组数据有问题。notes为{count}')
    return a


def get_part1(page, i, url, t_url):
    """

    :param t_url: 为了表示线程的索引
    :param url: 获取文件里的url
    :param page:
    :param i: 爬取数据的索引 t_url*40
    :return:
    """
    last_url = url
    page.get(last_url)
    a = page.ele('xpath://span[@class="username" and @data-v-1c93c041=""]').text  # 作者
    try:
        # 尝试查找元素
        b = page.ele('xpath://div[@id="detail-title" and @class="title"]', timeout=2).text  # 笔记标题
    except ElementNotFoundError:
        b = "该用户没有编写标题"
    c = page.ele('xpath://span[@class="note-text" and @data-v-cd6ca71e=""]').text  # 笔记内容
    d = page.eles('xpath://span[@class="count" and @data-v-e5195060=""]')
    d = d[len(d) - 1].text  # 点赞数
    e = page.ele('xpath://span[@class="count" and @data-v-502c7b76=""]').text  # 收藏数
    f = page.ele('xpath://span[@class="count" and @data-v-3eeaf146=""]').text  # 评论数

    headers = ('作者', '笔记标题', '笔记内容', '点赞数', '收藏数', '评论数', '笔记链接')
    entry = {
        headers[0]: a,  # 作者
        headers[1]: b,  # 笔记标题
        headers[2]: c,  # 笔记内容
        headers[3]: d,  # 点赞数
        headers[4]: e,  # 收藏数
        headers[5]: f,  # 评论数
        headers[6]: last_url  # 笔记链接
    }
    json_data.append(entry)
    with open('xhs_bj1.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
    print(f'线程{t_url}第{i}组数据爬取成功！：{last_url}')
