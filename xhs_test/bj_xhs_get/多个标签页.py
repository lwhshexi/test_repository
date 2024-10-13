import threading
import time
from DrissionPage import Chromium, ChromiumOptions
from get_lasturl import get_part1


def init():
    co1 = ChromiumOptions().set_local_port(9223).set_user_data_path('data2')
    page = Chromium(co1)

# init()


def xc_while(page, lines, t_url):
    """
        线程循环体函数
    :param page: 网页实例
    :param lines: 爬取的url数据后面跟索引
    :param t_url: 线程索引
    :return:
    """
    page = page.new_tab(lines[t_url * 40].strip())
    # print(f'线程{t_url}正在爬取url为：{lines[t_url].strip()}')
    # 读取整个文件并输出前三行
    get_part1(page, t_url * 40, lines[t_url * 40].strip(), t_url)
    for i1 in range(t_url * 40 + 1, 200):  # 39 + t_url * 40
        # page.get(lines[i1].strip())
        # print(f'线程{t_url}正在爬取url为：{lines[i1].strip()}')
        get_part1(page, i1, lines[i1].strip(), t_url)
    page.close()


def main(t_url):
    """
    :param t_url: 线程的url的索引
    :return:
    """
    with open('last_url.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()  # 读取所有行
        page = Chromium(9223)

    if t_url == 0:  # 代表的是第一个线程 url范围：[0, 39]
        xc_while(page, lines, t_url)

    if t_url == 1:  # 代表的是第一个线程 url范围：[40, 79]
        xc_while(page, lines, t_url)

    if t_url == 2:  # 代表的是第一个线程 url范围：[80, 119]
        xc_while(page, lines, t_url)

    # if t_url == 3:  # 代表的是第一个线程 url范围：[120, 159]
    #     xc_while(page, lines, t_url)
    #
    # if t_url == 4:  # 代表的是第一个线程 url范围：[160, 199]
    #     xc_while(page, lines, t_url)


# main()
if __name__ == '__main__':
    for i in range(1):
        t1 = threading.Thread(target=main, args=(i,))
        t1.start()
