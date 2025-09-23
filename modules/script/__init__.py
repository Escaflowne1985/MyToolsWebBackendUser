# coding:utf-8
"""
@IDE     ：PyCharm
@Project ：MyAIToolsClient
@File    ：__init__.py
@Author  ：Mr数据杨
@Date    ：2025/9/11
@Desc    ：聚合导出 core 与 services 层的公共类与函数，统一对外可用接口
"""

# =========================
# Core 层（稳定的基础能力）
# 说明：
# - 本分区仅收敛“跨业务复用”的底层能力：常量、路径、消息格式、任务状态、异常类型与通用校验。
# - 这些模块不包含具体业务逻辑，侧重“环境/路径/消息/任务/配置键”等基础设施。
# 来源文件：
# - core_constants.py / core_path_manager.py / core_msg_manager.py
# - core_task_manager.py / core_valid_data.py / core_exceptions.py
# =========================

from modules.script.core_constants import *
from modules.script.core_constants import __all__ as core_constants_all
from modules.script.core_exceptions import *
from modules.script.core_exceptions import __all__ as core_exceptions_all
from modules.script.core_msg_manager import *
from modules.script.core_msg_manager import __all__ as core_msg_manager_all
from modules.script.core_path_manager import *
from modules.script.core_path_manager import __all__ as core_path_manager_all
from modules.script.core_task_manager import *
from modules.script.core_task_manager import __all__ as core_task_manager_all
from modules.script.core_valid_data import *
from modules.script.core_valid_data import __all__ as core_valid_data_all

# =========================
# Services 层（与业务强相关的“可组合服务”）
# 说明：
# - services_* 为可直接被业务编排调用的服务能力。
# - 按照“音频处理 / 视频处理 / 文件系统 / 可执行文件 / 配置存取 / 字幕样式 / 鉴权调用”分区导出。
# - 这里导出的名称均保持“原始文件内定义的函数名/类名”，不做改名处理。
# =========================

# ---- 鉴权与后端服务调用（HTTP 封装） ----
# 来源文件：services_auth.py
# 作用说明：统一封装后端鉴权、TTS/SEO 等 API 调用入口；对接签名、用户积分校验等。
from modules.script.services_auth import *
from modules.script.services_auth import __all__ as services_auth_all

# ---- 配置存取（持久化配置项） ----
# 来源文件：services_config_store.py
# 作用说明：以“命名配置域”为粒度保存/读取本地与远端配置；面向 UI/服务侧共享参数。
from modules.script.services_config_store import *
from modules.script.services_config_store import __all__ as services_config_store_all

# ---- 文件/目录/多媒体 I/O 管理 ----
# 来源文件：services_file_manager.py
# 作用说明：统一文件系统与多媒体元数据操作；包含目录扫描、时长/FPS 获取、批量搬运与任务目录初始化等。
from modules.script.services_file_manager import *
from modules.script.services_file_manager import __all__ as services_file_manager_all

# ---- 可执行文件定位 ----
# 来源文件：services_executable_finder.py
# 作用说明：跨平台查找 ffmpeg 等外部依赖的可执行文件绝对路径。
from modules.script.services_executable_finder import *
from modules.script.services_executable_finder import __all__ as services_executable_finder_all

# ---- 字幕样式工具（ASS 风格） ----
# 来源文件：services_subtitle.py
# 作用说明：把 SRT 转换为 ASS 并注入分辨率/字体/颜色/对齐/边距等样式；适配渲染侧字幕观感。
from modules.script.services_subtitle import *
from modules.script.services_subtitle import __all__ as services_subtitle_all

# ---- 音频侧处理（ASR/TTS 相关基础工具） ----
# 来源文件：services_audio_process.py
# 作用说明：提供时间戳格式化、文本清洗/切分、音质字符串解析等“ASR/TTS 前后处理”常用函数。
from modules.script.services_audio_process import *
from modules.script.services_audio_process import __all__ as services_audio_process_all

# ---- 视频侧处理（拼接/重排/命令执行/文本清洗等） ----
# 来源文件：services_video_process.py
# 作用说明：面向“素材级”与“片段级”的组合处理；包含随机取样、顺序合并、命令执行、CAM 字幕聚合、文本清洗等。
from modules.script.services_video_process import *
from modules.script.services_video_process import __all__ as services_video_process_all

# ---- GPT 文本洗稿（流式/整段模式统一）----
# 来源文件：chatgpt_script.py
# 作用说明：封装 GPT 调用，支持 DataFrame 批处理与逐条流式处理
from modules.script.services_chatgpt import *
from modules.script.services_chatgpt import __all__ as services_chatgpt_all

# ---- 即梦绘图封装（API模式 / 账号模式统一）----
# 来源文件：services_video_scene.py
# 作用说明：封装即梦（Jimeng）绘图调用，支持 API-Key 模式与账号模式登录，
#          并统一返回 OpenAI v1 标准格式，便于上层调用和后续维护
from modules.script.services_video_scene import *
from modules.script.services_video_scene import __all__ as services_video_scene_all

# =========================
# __all__ 对外导出名（供 IDE 补全与 from modules.script import *）
# 说明：
# - 仅导出稳定的类与函数名；严格保持与各源文件中“定义的原始名字”一致。
# - 如果未来出现“同名函数来自不同实现文件”，务必在本文件顶部以中文备注说明并采用明确命名约定再导出。
# =========================

__all__ = []

all_list = [
    core_constants_all,
    core_exceptions_all,
    core_msg_manager_all,
    core_path_manager_all,
    core_task_manager_all,
    core_valid_data_all,
    services_audio_process_all,
    services_auth_all,
    services_video_process_all,
    services_file_manager_all,
    services_config_store_all,
    services_chatgpt_all,
    services_video_scene_all,
]

for sub_all in all_list:
    __all__.extend(sub_all)
