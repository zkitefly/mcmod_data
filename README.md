# mcmod_data

## 介绍

该仓库是爬取 mcmod 上的 中文名称 次要名称 curseforge mcmod mcbbs modrinth 数据的仓库

并将收集到的数据整理成 data.csv 供 HMCL 使用

**本仓库的脚本并不是开箱即用的，可能需要你自己去改一些东西，才能正常食用！**

## 使用方法

#### 0.配置环境

首先将 Python 安装好

然后输入命令：`pip install selenium` 安装 selenium

然后确保你的电脑装有 Chrome 浏览器

#### 1.获取 MCMOD 网站页面

输入：`python3 mcmoddata.py`

然后按照脚本提示输入相应数据

输入完后，你会发现脚本会自动打开 Chrome 浏览器并执行相应操作

注意：

- 请一定要确保你的设备网络通畅！

- 请不要运行多个 mcmoddata.py ，否则 MCMOD 可能会将你的 IP 列入黑名单！

#### 2.整理数据

输入`python3 data.py`

然后就可以自动整理数据至 data.json 文件中

#### 3.数据转换为 data.csv

输入：`python3 parse_mcmod_data.py`

然后就可以自动整理数据至 data.csv 文件中

## 版权

所有爬取出来的数据均归 mcmod.cn 版权所有©