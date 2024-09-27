import sys
import subprocess
import os
import psutil
from PyQt6 import QtWidgets, QtCore


class Launcher(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Django Project Launcher")

        # 创建按钮
        self.kill_button = QtWidgets.QPushButton("杀掉所有Python和ffmpeg进程", self)
        self.git_button = QtWidgets.QPushButton("更新Git仓库", self)
        self.install_button = QtWidgets.QPushButton("安装pip和数据库迁移", self)
        self.start_button = QtWidgets.QPushButton("启动Django服务", self)

        # 创建输出区域
        self.output_area = QtWidgets.QTextEdit(self)
        self.output_area.setReadOnly(True)

        # 布局设置
        layout = QtWidgets.QVBoxLayout()
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(self.kill_button)
        button_layout.addWidget(self.git_button)
        button_layout.addWidget(self.install_button)
        button_layout.addWidget(self.start_button)

        layout.addLayout(button_layout)
        layout.addWidget(self.output_area)
        self.setLayout(layout)

        # 连接按钮事件
        self.kill_button.clicked.connect(self.kill_processes)
        self.git_button.clicked.connect(self.update_git)
        self.install_button.clicked.connect(self.install_packages)
        self.start_button.clicked.connect(self.start_django)

    def append_output(self, message):
        self.output_area.append(message)

    def kill_processes(self):
        current_process = psutil.Process()  # 获取当前进程
        for proc in psutil.process_iter():
            if (proc.name() in ['python.exe', 'ffmpeg.exe']) and (proc.pid != current_process.pid):
                proc.kill()
        self.append_output("已杀掉所有Python和ffmpeg进程，除了当前进程。")

    def update_git(self):
        cmd = "git checkout . && git pull"
        process = subprocess.Popen(f'cmd.exe /c {cmd}', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # 实时输出命令结果
        for line in process.stdout:
            self.append_output(line)

        process.wait()
        if process.returncode == 0:
            self.append_output("已成功更新Git仓库。")
        else:
            self.append_output("更新失败，请查看输出。")

    def install_packages(self):
        try:
            pip_result = subprocess.run(["./dv3admin/Scripts/pip.exe", "install", "-r", "project/req_new.txt"], capture_output=True, text=True)
            self.append_output(pip_result.stdout)
            self.append_output(pip_result.stderr)

            makemigrations_result = subprocess.run(["./dv3admin/python.exe", "manage.py", "makemigrations"], capture_output=True, text=True)
            self.append_output(makemigrations_result.stdout)
            self.append_output(makemigrations_result.stderr)

            migrate_result = subprocess.run(["./dv3admin/python.exe", "manage.py", "migrate"], capture_output=True, text=True)
            self.append_output(migrate_result.stdout)
            self.append_output(migrate_result.stderr)

            if pip_result.returncode == 0 and makemigrations_result.returncode == 0 and migrate_result.returncode == 0:
                self.append_output("已成功安装pip包和数据库迁移。")
            else:
                self.append_output("安装或迁移过程中发生错误。")
        except Exception as e:
            self.append_output(f"异常: {str(e)}")

    def start_django(self):
        process = subprocess.Popen(["./dv3admin/pythonw.exe", "manage.py", "runserver", "0.0.0.0:9000"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # 实时输出命令结果
        for line in process.stdout:
            self.append_output(line)

        process.wait()
        if process.returncode == 0:
            self.append_output("Django服务已启动。")
        else:
            self.append_output("Django服务启动失败。")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    launcher = Launcher()
    launcher.show()
    sys.exit(app.exec())
