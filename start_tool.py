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
        self.resize(800, 600)

        # 创建按钮
        self.kill_button = QtWidgets.QPushButton("杀掉所有Python和ffmpeg进程", self)
        self.git_button = QtWidgets.QPushButton("更新Git仓库", self)
        self.install_button = QtWidgets.QPushButton("安装pip", self)
        self.migrate_button = QtWidgets.QPushButton("数据库迁移", self)
        self.start_button = QtWidgets.QPushButton("启动Django服务", self)
        self.start_client_button = QtWidgets.QPushButton("启动客户端", self)
        self.start_client_button.setEnabled(False)  # 初始状态禁用

        # 创建输出区域
        self.output_area = QtWidgets.QPlainTextEdit(self)
        self.output_area.setReadOnly(True)
        self.output_area.ensureCursorVisible()

        # 创建按钮布局
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(self.kill_button)
        button_layout.addWidget(self.git_button)
        button_layout.addWidget(self.install_button)
        button_layout.addWidget(self.migrate_button)
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.start_client_button)

        # 主布局
        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.output_area, 1)  # 添加伸展因子确保输出区域扩展

        self.setLayout(main_layout)

        # 连接按钮事件
        self.kill_button.clicked.connect(self.kill_processes)
        self.git_button.clicked.connect(lambda:self.run_command("git checkout . && git pull"))
        self.install_button.clicked.connect(
            lambda:self.run_command(".\\dv3admin\\Scripts\\pip.exe install -r project\\req_new.txt"))
        self.migrate_button.clicked.connect(
            lambda:self.run_command(".\\dv3admin\\python.exe manage.py makemigrations && .\\dv3admin\\python.exe manage.py migrate"))
        self.start_button.clicked.connect(lambda:self.run_django_server(".\\dv3admin\\python.exe manage.py runserver 0.0.0.0:9000"))
        self.start_client_button.clicked.connect(lambda:self.run_command(".\\project\\vite-project.exe"))

    def append_output(self, message):
        self.output_area.appendPlainText(message.strip())

    def run_command(self, cmd):
        process = QtCore.QProcess(self)
        process.setProgram("cmd.exe")
        process.setArguments(["/C", cmd])
        process.readyReadStandardOutput.connect(lambda:self.append_output(str(process.readAllStandardOutput(), 'utf-8')))
        process.readyReadStandardError.connect(lambda:self.append_output(str(process.readAllStandardError(), 'utf-8')))
        process.start()

    def run_django_server(self, cmd):
        process = QtCore.QProcess(self)
        process.setProgram("cmd.exe")
        process.setArguments(["/C", cmd])
        process.readyReadStandardOutput.connect(lambda:self.check_django_startup(str(process.readAllStandardOutput(), 'utf-8')))
        process.readyReadStandardError.connect(lambda:self.append_output(str(process.readAllStandardError(), 'utf-8')))
        process.start()

    def check_django_startup(self, output):
        self.append_output(output.strip())
        if "development server at" in output:
            self.start_client_button.setEnabled(True)

    def kill_processes(self):
        current_process = psutil.Process()  # 获取当前进程
        for proc in psutil.process_iter():
            if (proc.name() in ['python.exe', 'ffmpeg.exe']) and (proc.pid != current_process.pid):
                proc.kill()
        self.append_output("已杀掉所有Python和ffmpeg进程，除了当前进程。")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    launcher = Launcher()
    launcher.show()
    sys.exit(app.exec())
