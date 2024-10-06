import json
# 打开 JSON 文件并读取内容
with open('小红书数据.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 打印读取到的数据
# print("读取到的数据:", data)

# 遍历 JSON 数据
for entry in data:
    print(entry['链接'])
    break
