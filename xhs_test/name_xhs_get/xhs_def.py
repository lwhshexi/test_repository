from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def get_intro(driver):
    """

    :param driver: 网页实例
    :return: intro:简介， 返回类型字符串
    """
    # 获取简介
    try:
        # 尝试查找元素
        element = driver.find_element(By.XPATH, '//div[@class="user-desc" and @data-v-8f3e401c=""]')
        intro = element.text  # 获取元素文本
        print("简介\n:", intro)
    except NoSuchElementException:
        # 如果找不到元素，返回空值
        intro = "该用户没有编写简介"
        print("简介\n:", intro)
    return intro


def get_fan(driver):
    """

    :param driver: 网页实例
    :return: fan:粉丝，返回类型字符串
    """
    # 获取粉丝
    element_text = driver.find_elements(By.XPATH, '//span[@class="count" and @data-v-e99584b8=""]')
    fan = element_text[1].text
    print("粉丝:\n", fan)
    return fan


def get_like(driver):
    """

    :param driver: 网页实例
    :return: like:点赞，返回类型字符串
    """
    # 获取点赞
    element_text = driver.find_elements(By.XPATH, '//span[@class="count" and @data-v-e99584b8=""]')
    like = element_text[2].text
    print("点赞:\n", like)
    return like
