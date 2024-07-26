import json

# 提取 [world-geo-json-zh](https://github.com/Surbowl/world-geo-json-zh.git) 的 properties，把没必要的外层都删剪掉
# 假设原始JSON数据存储在'input.json'文件中
input_file_path = './world.zh.json'
# 处理后的数据将被写入到'output.json'文件中
output_file_path = './output.json'

# 读取原始JSON数据
with open(input_file_path, 'r', encoding='utf-8') as file:
    raw_data = json.load(file)

# 处理数据，删除外层的properties
processed_data = [{k: v for k, v in item['properties'].items()} for item in raw_data]

# 写入处理后的数据到新文件
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(processed_data, file, ensure_ascii=False, indent=4)

print(f'Processed data has been written to {output_file_path}')