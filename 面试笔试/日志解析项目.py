__time__ = '2021/9/13'
__author__ = 'ZhiYong Sun'

import collections
import pandas as pd
from numpy import mean

with open(file=r'file_path', encoding='utf-8', mode='r') as fr:
    data = fr.readlines()

# 提取 + 保存
raw_result = collections.defaultdict(dict)
for line in data:
    if line[:10] in ['algorithm App']:
        raw_result[line[:10]][line[10:20]] = line[-10:]

for appdata in raw_result:
    df = pd.DataFrame(appdata)
    df.to_csv('sub_path_name')

# 去重 + 保存
raw_data = pd.read_csv(r'sub_path_name')
raw_data.columns = ['SeriesId', 'Time']
raw_data.drop_duplicates(subset='SeriesId', keep='first', inplace=True)

# 拼接 + 保存
old_data = pd.read_csv('old_path', encoding='utf-8')
new_data = pd.read_csv('new_path', encoding='utf-8')
merged_data = pd.merge(old_data, new_data, on=['StudyId', 'SeriesId'], sort=False)

# 求平均 + 保存
old_time_data = merged_data.iloc[:, -2]
old_avg_time = mean(old_time_data)
new_time_data = merged_data.iloc[:, -1]
new_avg_time = mean(new_time_data)
