import json
import csv

# 获取 data.json 文件路径
data_path = input('请输入 data.json 文件路径：')

# 读取 JSON 数据
with open(data_path, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

# 打开 CSV 文件
with open('data.csv', 'w', encoding='utf-8') as f:
    # 创建 CSV 写入器
    writer = csv.writer(f, delimiter=';')

    # 遍历 JSON 数据中的 mod 列表
    for mod in data['mod']:
        # 获取模组名称信息
        chinese_name = mod['name']['main']
        sub_name = mod['name']['sub']
        abbr = mod['name']['abbr']

        # 获取模组链接信息
        curseforge_id = ''
        mcmod_id = ''
        mcbbs_id = ''
        for link in mod['links']['list']:
            if link['type'] == 'curseforge':
                curseforge_id = link['url'].split('/')[-1]
            elif link['type'] == 'mcmod':
                mcmod_id = link['url'].split('/')[-1].split('.')[0]
            elif link['type'] == 'mcbbs':
                mcbbs_id = link['url'].split('/')[-1].split('-')[1]

        # 获取模组 ID 信息
        mod_ids = ','.join(mod['modid']['list'])

        # 写入 CSV 文件
        writer.writerow([curseforge_id, mcmod_id, mcbbs_id, mod_ids, chinese_name, sub_name, abbr])

print('成功！！！')