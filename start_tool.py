# env manage.py/py
# -*- coding: UTF-8 -*-
'''
@Project ：manage.py 
@File    ：start_tool.py
@IDE     ：PyCharm 
@Author  ：Mr数据杨
@Date    ：2024-09-27 9:37 
'''

import sys
import subprocess
import psutil
from PyQt6 import QtWidgets


class Launcher(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Django Project Launcher")

        # 按钮
        self.kill_button = QtWidgets.QPushButton("查杀所有进程", self)
        self.git_button = QtWidgets.QPushButton("更新项目", self)
        self.install_button = QtWidgets.QPushButton("依赖安装和数据迁移", self)
        self.start_button = QtWidgets.QPushButton("启动程序服务", self)

        # 布局
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.kill_button)
        layout.addWidget(self.git_button)
        layout.addWidget(self.install_button)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

        # 连接按钮
        self.kill_button.clicked.connect(self.kill_processes)
        self.git_button.clicked.connect(self.update_git)
        self.install_button.clicked.connect(self.install_packages)
        self.start_button.clicked.connect(self.start_django)

    def kill_processes(self):
        current_process = psutil.Process()  # 获取当前进程
        for proc in psutil.process_iter():
            # 检查是否为Python或ffmpeg进程，并排除当前进程
            if (proc.name() in ['python.exe', 'ffmpeg.exe']) and (proc.pid != current_process.pid):
                proc.kill()
        QtWidgets.QMessageBox.information(self, "完成", "已经清理掉所有无关进程。")

    def update_git(self):
        # 打开一个新的命令行窗口并执行 Git 命令
        cmd = "git checkout . && git pull"
        process = subprocess.Popen(f'cmd.exe /c {cmd}', creationflags=subprocess.CREATE_NEW_CONSOLE)

        # 等待命令执行完成
        process.wait()

        if process.returncode == 0:
            QtWidgets.QMessageBox.information(self, "完成", "已成功更新Git仓库。")
        else:
            QtWidgets.QMessageBox.warning(self, "失败", "更新失败，请查看命令行窗口了解更多信息。")

    def install_packages(self):
        try:
            pip_result = subprocess.run(["./dv3admin/Scripts/pip.exe", "install", "-r", "project/req_new.txt"], capture_output=True, text=True)

            # 获取并显示命令的输出和错误信息
            output_message = f"标准输出：{pip_result.stdout}\n"
            error_message = f"标准错误：{pip_result.stderr}\n"
            result_message = f"返回代码：{pip_result.returncode}\n"

            # 显示输出
            QtWidgets.QMessageBox.information(self, "Pip安装结果", output_message + error_message + result_message)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "异常", str(e))

        makemigrations_result = subprocess.run(["./dv3admin/python.exe", "dv3admin/manage.py", "makemigrations"], capture_output=True, text=True)
        migrate_result = subprocess.run(["./dv3admin/python.exe", "manage.py", "migrate"], capture_output=True, text=True)

        if pip_result.returncode == 0 and makemigrations_result.returncode == 0 and migrate_result.returncode == 0:
            QtWidgets.QMessageBox.information(self, "完成", "已成功安装pip包和数据库迁移。")
        else:
            error_message = "安装或迁移过程中发生错误：\n"
            if pip_result.returncode != 0:
                error_message += f"Pip安装错误: {pip_result.stderr}\n"
            if makemigrations_result.returncode != 0:
                error_message += f"Makemigrations错误: {makemigrations_result.stderr}\n"
            if migrate_result.returncode != 0:
                error_message += f"Migrate错误: {migrate_result.stderr}"
            QtWidgets.QMessageBox.critical(self, "错误", error_message)

    def start_django(self):
        def start_django(self):
            runserver_result = subprocess.Popen(["dv3admin/pythonw.exe", "manage.py", "runserver", "0.0.0.0:9000"])
            runserver_result.wait()

            if runserver_result.returncode == 0:
                QtWidgets.QMessageBox.information(self, "完成", "Django服务已启动。")
            else:
                QtWidgets.QMessageBox.critical(self, "失败", "Django服务启动失败，请检查输出。")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    launcher = Launcher()
    launcher.show()
    sys.exit(app.exec())
