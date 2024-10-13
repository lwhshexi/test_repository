"""
import json
import os

# 新的数据
new_data = ['赵六', '钱七']
new_href = ['/user/profile/4', '/user/profile/5']

# 读取现有的 JSON 文件数据
if os.path.exists('data.json'):
    with open('data.json', 'r', encoding='utf-8') as f:
        json_data = json.load(f)  # 读取现有数据
else:
    json_data = []  # 如果文件不存在，则初始化为空列表

# 合并新数据
for i in range(len(new_data)):
    entry = {
        '小红书名称': new_data[i],
        '链接': new_href[i]
    }
    json_data.append(entry)

# 将更新后的字典列表写入 JSON 文件
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print("新数据已成功添加到 data.json 文件。")

"""  # 继续加入内容到json

"""
import json
json_data = []
headers = ('小红书名称', '链接')
data = ['张三', '李四', '王二麻子']
href = [1, 2, 3]
for d1 in data:
    entry = {
        headers[0]: d1,     # 创建字典
    }
    json_data.append(entry)

for d2 in href:
    entry1 = {
        headers[2]: d2,     # 创建字典
    }
    json_data.append(entry1)
# 将字典列表写入 JSON 文件
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
"""  # 写入json文件
