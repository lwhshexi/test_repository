"""
思路：
    ·利用selenium爬取网页源代码，在对源代码进行爬取
        打开网页所调用的库 > subprocess
    ·创建 WebDriver 实例连接到 Edge
    ·获取目标url，将页面滑动到最低端，在执行获取页面的html
"""
import json
import subprocess
import time
from selenium import webdriver
from lxml import etree
from xhs_def import get_fan, get_intro, get_like

xhs_name, xhs_lj = [], []


def init(url):
    """
    初始化浏览器
    :return:
    """
    target_url = url
    subprocess.Popen([
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",  # 使用原始字符串
        '--remote-debugging-port=9223',
        '--user-data-dir=D:/EdgeDev1',  # 指定一个用户数据目录
        target_url  # 直接打开目标网页
    ])  # 使用 shell=True 来避免权限问题shell=True

    # 等待一段时间，确保页面加载完成
    time.sleep(3)


def get_html():
    """
    获取关键词水果的所有html
    :return:
    """
    # 创建 WebDriver 实例连接到 Edge
    options = webdriver.EdgeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Edge(options=options)
    html = driver.page_source
    with open('水果关键词.html', 'w', encoding='utf-8') as fs:
        fs.write(html)
    print('over!')


def extract_attributes():
    # 解析 HTML 文件
    parser = etree.HTMLParser()
    tree = etree.parse('./水果关键词.html', parser)  # 解析 HTML 并返回树形结构

    # 获取所有小红书名称
    for a in range(1, 302):  # 范围1-301
        result = tree.xpath(f'//*[@id="global"]/div[2]/div[2]/div/div[3]/div[{a}]/div/a/div/div[2]/div[1]/div')  # 执行 XPath 查询
        for element in result:
            xhs_name.append(element.text)

    # 获取所有初始链接
    for a in range(1, 302):  # 范围1-301
        result = tree.xpath(f'//*[@id="global"]/div[2]/div[2]/div/div[3]/div[{a}]/div/a/@href')  # 执行 XPath 查询
        xhs_lj.append('https://www.xiaohongshu.com' + result[0])

    """
    //*[@id="global"]/div[2]/div[2]/div/div[3]/div[1]/div/a/div/div[2]/div[1]/div
    //*[@id="global"]/div[2]/div[2]/div/div[3]/div[2]/div/a/div/div[2]/div[1]/div
    """


"""
extract_attributes()
headers = ('小红书名称', '链接')
xhs_json_data = []
for i in range(len(xhs_name)):
    entry = {
        headers[0]: xhs_name[i],
        headers[1]: xhs_lj[i]
    }
    xhs_json_data.append(entry)

with open('小红书数据.json', 'w', encoding='utf_8')as f:
    json.dump(xhs_json_data, f, ensure_ascii=False, indent=4)

print('over!')
"""  # 爬取小红书博主名称和所对应的链接
# init('https://www.xiaohongshu.com/search_result?keyword=%25E6%25B0%25B4%25E6%259E%259C&source=web_search_result_notes')


def get_f():
    """
    获取小红书名称的简介，粉丝，点赞
    :return:
    """
    # 使用 Selenium 连接到 Edge 浏览器
    options = webdriver.EdgeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9223")  # 连接到远程调试地址
    driver = webdriver.Edge(options=options)

    # 使用 JavaScript 在新标签页中打开一个新的链接
    driver.get('https://www.baidu.com')
    all_tabs = driver.window_handles
    print(len(all_tabs))
    driver.switch_to.window(all_tabs[-1])  # 跳转到最新打开的标签页面

    # 打开 JSON 文件并读取内容
    with open('小红书数据.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 遍历 JSON 数据
    # 直接从索引 具体位置 开始处理（因为索引从 0 开始）
    for i in range(120, len(data)):
        entry = data[i]
        a = (entry['链接'])
        driver.get(a)
        print("当前爬取链接", a)
        # 获取简介
        intro = get_intro(driver)
        # 获取粉丝
        fan = get_fan(driver)
        # 获取点赞
        like = get_like(driver)
        # 插入新属性到第i个元素
        data[i]["简介内容"] = intro  # 新属性
        data[i]["粉丝"] = fan  # 新属性
        data[i]["点赞"] = like  # 新属性
        # 保存到文件
        with open('小红书数据.json', 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)
        print("当前索引为：" + str(i))
        print("=====================\n")

# get_f()
