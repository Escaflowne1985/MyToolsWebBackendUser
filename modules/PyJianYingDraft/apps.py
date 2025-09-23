from django.apps import AppConfig
import subprocess
import os, sys
from django.conf import settings


class PyjianyingdraftConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.PyJianYingDraft"

    def ready(self):
        # 避免 autoreload 重复启动
        if os.environ.get('RUN_MAIN') != 'true':
            return

        # Windows 下查找并杀掉占用 9001 端口的进程
        try:
            result = subprocess.run(
                ["netstat", "-ano"], capture_output=True, text=True
            )
            for line in result.stdout.splitlines():
                if "9001" in line and "LISTENING" in line:
                    pid = line.strip().split()[-1]
                    subprocess.run(["taskkill", "/F", "/PID", pid])
                    print(f"已杀掉占用 9001 端口的进程 PID={pid}")
        except Exception as e:
            print(f"清理9001端口失败: {e}")

        capcut_path = os.path.join(settings.BASE_DIR, 'plugins', 'CapCutAPI', 'main.py')
        # capcut_path = os.path.join(settings.BASE_DIR, 'plugins', 'capcut-api-dev', 'main.py')


        # 使用当前 Python 解释器启动
        subprocess.Popen([sys.executable, capcut_path])
