import json
import pandas as pd

with open('xhs_bj1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # 读取现有数据

# 将 JSON 数据转换为 DataFrame
df = pd.DataFrame(data)

# 将 DataFrame 导出到 Excel 文件
excel_file = '小红书笔记数据.xlsx'
df.to_excel(excel_file, index=False, engine='openpyxl')

print(f"数据已成功导出到 {excel_file}")
