import json
from pypinyin import lazy_pinyin
# 处理 [CountryCodeAndPhoneCode](https://github.com/jjeejj/CountryCodeAndPhoneCode.git] 的数据
# 从文件读取数据
input_file = 'countries.json'
output_file = 'sorted_countries.json'

with open(input_file, 'r', encoding='utf-8') as f:
    countries = json.load(f)

# 按照中文拼音排序
countries.sort(key=lambda x: lazy_pinyin(x['chinese_name']))

# 按照拼音首字母分组
grouped_countries = {}
for country in countries:
    initial = lazy_pinyin(country['chinese_name'])[0][0].upper()
    if initial not in grouped_countries:
        grouped_countries[initial] = []
    grouped_countries[initial].append(country)

# 转换为所需的输出格式
output_data = []
for initial, countries in grouped_countries.items():
    output_data.append({'index': initial, 'countries': countries})

# 将结果写入文件
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=4)

print(f"Sorted and grouped countries have been written to {output_file}")
