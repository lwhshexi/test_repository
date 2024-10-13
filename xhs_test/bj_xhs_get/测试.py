import random
import time
from DrissionPage import ChromiumPage, ChromiumOptions
from DrissionPage.common import Actions
from get_lasturl import get_last_url

random_number = random.randint(0, 10)
url = 'https://www.xiaohongshu.com/search_result?keyword=%25E6%25B0%25B4%25E6%259E%259C%25E5%25AD%25A3%25E8%258A%2582&source=web_search_result_notes&type=51'

co = ChromiumOptions().set_paths(browser_path=r"C:\Users\shexi\AppData\Local\Google\Chrome\Application\chrome.exe")
page = ChromiumPage(co)
ac = Actions(page)
page.get(url)  # 访问网址，这行产生的数据包不监听
page.listen.start('web/v1/search/notes')  # 开始监听，指定获取包含该文本的数据包(部分url)
page('@class=search-icon').click()
res = page.listen.wait()  # 等待并获取一个数据包
count = 1
print(f'第{count}个notes: ', res.url)
get_last_url(page, res.response.body, count)
while True:
    # 检查循环条件
    if count == 11:     # 测试1，需求11
        break  # 如果条件满足，退出循环

    # 执行循环体
    page.listen.start('web/v1/search/notes')  # 开始监听，指定获取包含该文本的数据包(部分url)
    ac.scroll(delta_y=1500+random_number)
    res = page.listen.wait(timeout=2)  # 等待并获取一个数据包
    if res!=False:
        count += 1
        print(f'第{count}个notes: ', res.url)
        a = get_last_url(page, res.response.body, count)
        print(a)
