import json
import csv

# 获取 data.json 文件路径
data_path = input('请输入 datay.json 文件路径：')

# 读取 JSON 数据
with open(data_path, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

# 打开 CSV 文件
with open('datay.csv', 'w', encoding='utf-8') as f:
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

        # 筛选 curseforge_id 的内容，删除包含 "#" 的部分
        if "#" in curseforge_id:
            curseforge_id = curseforge_id[:curseforge_id.index("#")]

        # 筛选 curseforge_id 的内容，删除包含 "?" 的部分
        if "?" in curseforge_id:
            curseforge_id = curseforge_id[:curseforge_id.index("?")]

        # 筛选 mcbbs_id 的内容，删除包含 "?" 的部分
        if "&" in curseforge_id:
            mcbbs_id = mcbbs_id[:mcbbs_id.index("&")]

        # 获取模组 ID 信息
        mod_ids = ''
        # mod_ids = ','.join(mod['modid']['list'])

        # 写入 CSV 文件
        writer.writerow([curseforge_id, mcmod_id, mcbbs_id, mod_ids, chinese_name, sub_name, abbr])

# 检查并删除重复行（上述代码块会先读取 data.csv 文件的所有行，然后逐行检查是否已经出现过。如果已经出现过，就不再写入文件中，从而实现删除重复行的效果。）
lines_seen = set()  # 用于存储已经出现过的行
with open('datay.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
with open('datay.csv', 'w', encoding='utf-8') as f:
    for line in lines:
        if line not in lines_seen:  # 如果这一行没有出现过
            f.write(line)  # 写入文件
            lines_seen.add(line)  # 将这一行加入已出现的行中

print('成功！！！')