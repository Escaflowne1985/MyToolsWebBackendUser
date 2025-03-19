# coding:utf-8
'''
@IDE     ：PyCharm 
@Project ：MyToolsBak-MyToolsWebBackend.py 
@File    ：_run_app.py
@Author  ：Mr数据杨
@Date    ：2025/3/19
@Desc    : 
'''

import sys

# 确保 .pyd 文件所在目录在 sys.path 中
sys.path.append(r"./")

if len(sys.argv) < 2:
    print("❌ 请提供要运行的模块名称。")
    sys.exit(1)

module_name = sys.argv[1]  # 获取命令行参数，例如 "Wav2Lip384_app" 或 "SovitsSrc_app"

try:
    module = __import__(module_name)  # 动态导入模块
    if hasattr(module, 'main'):
        module.main()  # 调用 main 方法
    else:
        print(f"❌ `{module_name}.main` 方法不存在，请检查模块")
except ModuleNotFoundError:
    print(f"❌ 模块 `{module_name}` 未找到，请检查是否正确安装或放在当前目录下")
