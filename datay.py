import os
import json
from bs4 import BeautifulSoup

skip = []

mcmodwebdata_path = os.path.join(os.getcwd(), 'mcmodwebdatay')
if not os.path.exists(mcmodwebdata_path):
    print('mcmodwebdatay 文件夹不存在')
    exit()

mod = []
file_list = sorted(os.listdir(mcmodwebdata_path))
for i, file in enumerate(file_list):
    if file.endswith('.html'):
        print(f'正在处理第 {i+1} 个文件: {file}')
        with open(os.path.join(mcmodwebdata_path, file), 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

            # a_target_blank = soup.find('a', {'target': '_blank', 'href': lambda x: x.startswith('/class/diff/list/')})
            a_target_blank = soup.find('a', {'target': '_blank', 'href': lambda x: x.startswith('/modpack/diff/list/')})

            if a_target_blank is None:
                print(f'{file} 为 404')
                continue

            NAME = a_target_blank['href'].split('/')[4].split('.')[0]

            data_multi_id_modid = soup.find(attrs={'data-multi-id': 'modid'})
            MODID = None if data_multi_id_modid is None else data_multi_id_modid['value']

            MCBBS = None
            for script in soup.find_all('script'):
                if script.string and '.val("https://www.mcbbs.net/thread-' in script.string:
                    MCBBS  = script.string.split('/thread-')[1].split('-')[0]
                if script.string and '.val("http://www.mcbbs.net/thread-' in script.string:
                    MCBBS = script.string.split('/thread-')[1].split('-')[0]
                if script.string and '.val("https://mcbbs.net/thread-' in script.string:
                    MCBBS  = script.string.split('/thread-')[1].split('-')[0]
                if script.string and '.val("http://mcbbs.net/thread-' in script.string:
                    MCBBS = script.string.split('/thread-')[1].split('-')[0]
                if script.string and '.val("https://www.mcbbs.net/forum.php?mod=viewthread&tid=' in script.string:
                    MCBBS  = script.string.split('/forum.php?mod=viewthread&tid=')[1].split('"')[0]
                if script.string and '.val("https://mcbbs.net/forum.php?mod=viewthread&tid=' in script.string:
                    MCBBS = script.string.split('/forum.php?mod=viewthread&tid=')[1].split('"')[0]
                if script.string and '.val("http://www.mcbbs.net/forum.php?mod=viewthread&tid=' in script.string:
                    MCBBS = script.string.split('/forum.php?mod=viewthread&tid=')[1].split('"')[0]
                if script.string and '.val("http://mcbbs.net/forum.php?mod=viewthread&tid=' in script.string:
                    MCBBS = script.string.split('/forum.php?mod=viewthread&tid=')[1].split('"')[0]
                    break

            MRID = None
            for script in soup.find_all('script'):
                if script.string and '.val("https://modrinth.com/mod/' in script.string:
                    MRID = script.string.split('/mod/')[1].split('"')[0]
                if script.string and '.val("https://www.modrinth.com/mod/' in script.string:
                    MRID = script.string.split('/mod/')[1].split('"')[0]
                if script.string and '.val("http://modrinth.com/mod/' in script.string:
                    MRID = script.string.split('/mod/')[1].split('"')[0]
                if script.string and '.val("http://www.modrinth.com/mod/' in script.string:
                    MRID = script.string.split('/mod/')[1].split('"')[0]

                if script.string and '.val("https://modrinth.com/modpack/' in script.string:
                    MRID = script.string.split('/modpack/')[1].split('"')[0]
                if script.string and '.val("https://www.modrinth.com/modpack/' in script.string:
                    MRID = script.string.split('/modpack/')[1].split('"')[0]
                if script.string and '.val("http://modrinth.com/modpack/' in script.string:
                    MRID = script.string.split('/modpack/')[1].split('"')[0]
                if script.string and '.val("http://www.modrinth.com/modpack/' in script.string:
                    MRID = script.string.split('/modpack/')[1].split('"')[0]
                    break

            data_multi_id_sname = soup.find(attrs={'data-multi-id': 'sname'})
            ADDR = None if data_multi_id_sname is None else data_multi_id_sname['value']

            data_multi_id_name = soup.find(attrs={'data-multi-id': 'name'})
            ZNAME = None if data_multi_id_name is None else data_multi_id_name['value']

            CFID = None
            for script in soup.find_all('script'):
                if script.string and '.val("https://www.curseforge.com/minecraft/mc-mods/' in script.string:
                    CFID = script.string.split('/minecraft/mc-mods/')[1].split('"')[0]
                if script.string and '.val("https://minecraft.curseforge.com/projects/' in script.string:
                    CFID = script.string.split('/projects/')[1].split('"')[0]
                if script.string and '.val("http://www.curseforge.com/minecraft/mc-mods/' in script.string:
                    CFID = script.string.split('/minecraft/mc-mods/')[1].split('"')[0]
                if script.string and '.val("http://minecraft.curseforge.com/projects/' in script.string:
                    CFID = script.string.split('/projects/')[1].split('"')[0]

                if script.string and '.val("https://www.curseforge.com/mc-mods/minecraft/' in script.string:
                    CFID = script.string.split('/mc-mods/minecraft/')[1].split('"')[0]
                if script.string and '.val("https://www.curseforge.com/legacy/mc-mods/minecraft/' in script.string:
                    CFID = script.string.split('/legacy/mc-mods/minecraft/')[1].split('"')[0]
                if script.string and '.val("https://www.curseforge.com/minecraft/projects/' in script.string:
                    CFID = script.string.split('/minecraft/projects/')[1].split('"')[0]
                if script.string and '.val("https://www.curseforge.com/projects/' in script.string:
                    CFID = script.string.split('/projects/')[1].split('"')[0]
                if script.string and '.val("https://www.curseforge.com/minecraft/modpacks/' in script.string:
                    CFID = script.string.split('/minecraft/modpacks/')[1].split('"')[0]
                if script.string and '.val("https://www.curseforge.com/projects/' in script.string:
                    CFID = script.string.split('/projects/')[1].split('"')[0]
                if script.string and '.val("https://www.curseforge.com/minecraft/customization/' in script.string:
                    CFID = script.string.split('/minecraft/customization/')[1].split('"')[0]
                if script.string and '.val("https://www.curseforge.com/minecraft/mc-addons/' in script.string:
                    CFID = script.string.split('/minecraft/mc-addons/')[1].split('"')[0]
                if script.string and '.val("https://www.curseforge.com/minecraft/customization/' in script.string:
                    CFID = script.string.split('/minecraft/customization/')[1].split('"')[0]
                if script.string and '.val("https://www.curseforge.com/minecraft/configuration/' in script.string:
                    CFID = script.string.split('/minecraft/configuration/')[1].split('"')[0]

                if script.string and '.val("http://www.curseforge.com/mc-mods/minecraft/' in script.string:
                    CFID = script.string.split('/mc-mods/minecraft/')[1].split('"')[0]
                if script.string and '.val("http://www.curseforge.com/legacy/mc-mods/minecraft/' in script.string:
                    CFID = script.string.split('/legacy/mc-mods/minecraft/')[1].split('"')[0]
                if script.string and '.val("http://www.curseforge.com/minecraft/projects/' in script.string:
                    CFID = script.string.split('/minecraft/projects/')[1].split('"')[0]
                if script.string and '.val("http://www.curseforge.com/projects/' in script.string:
                    CFID = script.string.split('/projects/')[1].split('"')[0]
                if script.string and '.val("http://www.curseforge.com/minecraft/modpacks/' in script.string:
                    CFID = script.string.split('/minecraft/modpacks/')[1].split('"')[0]
                if script.string and '.val("http://www.curseforge.com/projects/' in script.string:
                    CFID = script.string.split('/projects/')[1].split('"')[0]
                if script.string and '.val("http://www.curseforge.com/minecraft/customization/' in script.string:
                    CFID = script.string.split('/minecraft/customization/')[1].split('"')[0]
                if script.string and '.val("http://www.curseforge.com/minecraft/mc-addons/' in script.string:
                    CFID = script.string.split('/minecraft/mc-addons/')[1].split('"')[0]
                if script.string and '.val("http://www.curseforge.com/minecraft/customization/' in script.string:
                    CFID = script.string.split('/minecraft/customization/')[1].split('"')[0]
                if script.string and '.val("http://www.curseforge.com/minecraft/configuration/' in script.string:
                    CFID = script.string.split('/minecraft/configuration/')[1].split('"')[0]

                if script.string and '.val("https://curseforge.com/mc-mods/minecraft/' in script.string:
                    CFID = script.string.split('/mc-mods/minecraft/')[1].split('"')[0]
                if script.string and '.val("https://curseforge.com/legacy/mc-mods/minecraft/' in script.string:
                    CFID = script.string.split('/legacy/mc-mods/minecraft/')[1].split('"')[0]
                if script.string and '.val("https://curseforge.com/minecraft/projects/' in script.string:
                    CFID = script.string.split('/minecraft/projects/')[1].split('"')[0]
                if script.string and '.val("https://curseforge.com/projects/' in script.string:
                    CFID = script.string.split('/projects/')[1].split('"')[0]
                if script.string and '.val("https://curseforge.com/minecraft/modpacks/' in script.string:
                    CFID = script.string.split('/minecraft/modpacks/')[1].split('"')[0]
                if script.string and '.val("https://curseforge.com/projects/' in script.string:
                    CFID = script.string.split('/projects/')[1].split('"')[0]
                if script.string and '.val("https://curseforge.com/minecraft/customization/' in script.string:
                    CFID = script.string.split('/minecraft/customization/')[1].split('"')[0]
                if script.string and '.val("https://curseforge.com/minecraft/mc-addons/' in script.string:
                    CFID = script.string.split('/minecraft/mc-addons/')[1].split('"')[0]
                if script.string and '.val("https://curseforge.com/minecraft/customization/configuration/' in script.string:
                    CFID = script.string.split('/minecraft/customization/configuration/')[1].split('"')[0]

                if script.string and '.val("http://curseforge.com/mc-mods/minecraft/' in script.string:
                    CFID = script.string.split('/mc-mods/minecraft/')[1].split('"')[0]
                if script.string and '.val("http://curseforge.com/legacy/mc-mods/minecraft/' in script.string:
                    CFID = script.string.split('/legacy/mc-mods/minecraft/')[1].split('"')[0]
                if script.string and '.val("http://curseforge.com/minecraft/projects/' in script.string:
                    CFID = script.string.split('/minecraft/projects/')[1].split('"')[0]
                if script.string and '.val("http://curseforge.com/projects/' in script.string:
                    CFID = script.string.split('/projects/')[1].split('"')[0]
                if script.string and '.val("http://curseforge.com/minecraft/modpacks/' in script.string:
                    CFID = script.string.split('/minecraft/modpacks/')[1].split('"')[0]
                if script.string and '.val("http://curseforge.com/projects/' in script.string:
                    CFID = script.string.split('/projects/')[1].split('"')[0]
                if script.string and '.val("http://curseforge.com/minecraft/customization/' in script.string:
                    CFID = script.string.split('/minecraft/customization/')[1].split('"')[0]
                if script.string and '.val("http://curseforge.com/minecraft/mc-addons/' in script.string:
                    CFID = script.string.split('/minecraft/mc-addons/')[1].split('"')[0]
                if script.string and '.val("http://curseforge.com/minecraft/customization/' in script.string:
                    CFID = script.string.split('/minecraft/customization/')[1].split('"')[0]
                if script.string and '.val("http://curseforge.com/minecraft/configuration/' in script.string:
                    CFID = script.string.split('/minecraft/configuration/')[1].split('"')[0]
                    break

            data_multi_id_ename = soup.find(attrs={'data-multi-id': 'ename'})
            ENAME = None if data_multi_id_ename is None else data_multi_id_ename['value']

            if ENAME in skip:
                continue

            links_list = []
            if CFID is not None:
                if '/files' in CFID:
                    CFID = CFID[:CFID.index("/files")]
                if '?' in CFID:
                    CFID = CFID[:CFID.index("?")]
                links_list.append({
                    'type': 'curseforge',
                    'url': f'https://www.curseforge.com/minecraft/modpacks/{CFID}'
                })
            links_list.append({
                'type': 'mcmod',
                'url': f'https://www.mcmod.cn/modpack/{NAME}.html'
            })
            if MCBBS is not None:
                if '&' in MCBBS:
                    MCBBS = MCBBS[:MCBBS.index("&")]
                links_list.append({
                    'type': 'mcbbs',
                    'url': f'https://www.mcbbs.net/thread-{MCBBS}-1-1.html'
                })
            if MRID is not None:
                if '/versions' in MRID:
                    MRID = MRID[:MRID.index("/versions")]
                links_list.append({
                    'type': 'modrinth',
                    'url': f'https://www.modrinth.com/modpack/{MRID}'
                })

            mod.append({
                'name': {
                    'main': ZNAME,
                    'sub': ENAME,
                    'abbr': ADDR
                },
                'links': {
                    'list': links_list
                },
                'modid': {
                    'list': [MODID]
                }
            })

with open('datay.json', 'w', encoding='utf-8-sig') as f:
    json.dump({'mod': mod}, f, ensure_ascii=False, indent=2)

print('成功！！！')