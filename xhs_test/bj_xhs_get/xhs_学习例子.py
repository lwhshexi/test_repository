import threading
import time
from DrissionPage import ChromiumOptions, Chromium
from DrissionPage import ChromiumPage

from get_lasturl import get_part1

# co = ChromiumOptions().set_paths(browser_path=r"C:\Users\shexi\AppData\Local\Google\Chrome\Application\chrome.exe")
# page = ChromiumPage(co)
# # 第一个标签页访问网址
# page.new_tab('https://gitee.com/explore/ai')
# # 获取第一个标签页对象
# tab1 = page.get_tab()
# # 新建一个标签页并访问另一个网址
# tab2 = page.new_tab('https://gitee.com/explore/machine-learning')
# # 获取第二个标签页对象
# tab2 = page.get_tab(tab2)
# print(tab1.tab_id)
# print(tab2.tab_id)
# time.sleep(2)
# tab1.close()

# co1 = ChromiumOptions().set_local_port(9222).set_user_data_path('data1')
# page = Chromium(9222)
a = 0


def control():
    global a
    while True:
        b = input('输入你想查看的线程')
        b = int(b)
        a = b


def open_url():
    while True:
        # print(a)
        time.sleep(0.5)
        if a == 1:
            # tab1 = page.new_tab('https://www.baidu.com')
            print(f'我是线程1：')
        if a == 2:
            # tab1 = page.new_tab('https://www.baidu.com')
            print(f'我是线程2：')
        if a == 3:
            # tab1 = page.new_tab('https://www.baidu.com')
            print(f'我是线程3：')


def pd(i):
    if i == 0:
        control()
    if i == 1:
        open_url()

def  xc_while(page, lines, t_url):
    """
    :param page: 网页实例
    :param lines: 爬取的url数据
    :param t_url: 线程索引
    :return:
    """
    page = page.new_tab(lines[t_url].strip())
    print(f'线程{t_url}正在爬取url为：{lines[t_url].strip()}')
    # 读取整个文件并输出前三行
    get_part1(page, t_url, lines[t_url].strip(), t_url)
    for i1 in range(1, 2):
        page.get(lines[i1].strip())
        print(f'线程{t_url}正在爬取url为：{lines[i1].strip()}')
        get_part1(page, i1, lines[i1].strip(), t_url)
    page.close()

def main(t_url):
    """
    :param t_url: 线程的url的索引
    :return:
    """
    with open('last_url.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()  # 读取所有行
        page = Chromium(9222)
    if t_url == 0:  # 代表的是第一个线程 url范围：[0, 39]
        xc_while(page, lines, t_url)


# main()
if __name__ == '__main__':
    for i in range(5):
        t1 = threading.Thread(target=main, args=(i,))
        t1.start()
