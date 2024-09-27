import sys
import subprocess
import os
import psutil
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QRegion, QPainterPath
from PyQt6.QtCore import Qt, QRectF
import qdarktheme
import re


def remove_ansi_escape_sequences(text):
    ansi_escape_pattern = re.compile(r'''
        \x1B  # ESC
        (?:   # 7-bit C1 Fe (except CSI)
            [@-Z\\-_]
        |     # or [ for CSI, followed by a control sequence
            \[
            [0-?]*  # Parameter bytes
            [ -/]*  # Intermediate bytes
            [@-~]   # Final byte
        )
    ''', re.VERBOSE)
    return ansi_escape_pattern.sub('', text)


class Launcher(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.old_pos = None
        self.click_event()

    def init_ui(self):
        self.setWindowTitle("AI工具箱启动器")
        self.resize(1000, 300)
        self.set_round_corners()

        # 创建最小化和关闭按钮
        self.minimize_button = QtWidgets.QPushButton("-", self)
        self.close_button = QtWidgets.QPushButton("x", self)
        self.minimize_button.clicked.connect(self.showMinimized)
        self.close_button.clicked.connect(self.close)

        # 创建功能按钮
        self.kill_button = QtWidgets.QPushButton("杀掉所有Python和ffmpeg进程", self)
        self.git_button = QtWidgets.QPushButton("更新Git仓库", self)
        self.install_button = QtWidgets.QPushButton("安装pip", self)
        self.migrate_button = QtWidgets.QPushButton("数据库迁移", self)
        self.start_button = QtWidgets.QPushButton("启动Django服务", self)
        self.start_client_button = QtWidgets.QPushButton("启动客户端", self)
        self.start_client_button.setEnabled(False)

        # 创建按钮布局
        button_layout = QtWidgets.QVBoxLayout()
        button_layout.addWidget(self.kill_button)
        button_layout.addWidget(self.git_button)
        button_layout.addWidget(self.install_button)
        button_layout.addWidget(self.migrate_button)
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.start_client_button)

        # 描述标签和控制按钮的组合布局
        top_layout = QtWidgets.QHBoxLayout()
        description_label = QtWidgets.QLabel("AI工具箱启动器，获取最新程序加入QQ群：670870515", self)
        description_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)  # 文字左对齐
        top_layout.addWidget(description_label, 1)
        top_layout.addWidget(self.minimize_button)
        top_layout.addWidget(self.close_button)

        # 创建输出区域
        self.output_area = QtWidgets.QPlainTextEdit(self)
        self.output_area.setReadOnly(True)
        self.output_area.ensureCursorVisible()

        # 创建消息输出布局
        message_layout = QtWidgets.QVBoxLayout()
        message_layout.addWidget(self.output_area)

        # 下层水平布局
        content_layout = QtWidgets.QHBoxLayout()
        content_layout.addLayout(button_layout)
        content_layout.addLayout(message_layout, 1)

        # 创建主布局
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(top_layout)
        main_layout.addLayout(content_layout)

        self.setLayout(main_layout)

    def click_event(self):
        # 连接按钮事件
        self.kill_button.clicked.connect(self.process_kill_processes)
        self.git_button.clicked.connect(self.process_update_git)
        self.install_button.clicked.connect(self.process_install_pip)
        self.migrate_button.clicked.connect(self.process_database_migration)
        self.start_button.clicked.connect(self.process_start_django)
        self.start_client_button.clicked.connect(self.process_start_client)

    def set_round_corners(self):
        radius = 10  # 圆角半径
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), radius, radius)
        self.setMask(QRegion(path.toFillPolygon().toPolygon()))

    def mousePressEvent(self, event):
        self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.old_pos:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.old_pos = None

    def append_output(self, message, color='black'):
        message_html = f"<span style='color: {color};'>{remove_ansi_escape_sequences(message.strip())}</span>"
        self.output_area.appendHtml(message_html)

    def clear_output(self):
        self.output_area.clear()

    def run_command(self, cmd, completion_message):
        process = QtCore.QProcess(self)
        process.setProgram("cmd.exe")
        process.setArguments(["/C", cmd])
        process.readyReadStandardOutput.connect(lambda:self.append_output(str(process.readAllStandardOutput(), 'utf-8')))
        process.readyReadStandardError.connect(lambda:self.append_output(str(process.readAllStandardError(), 'utf-8')))
        process.finished.connect(lambda exitCode, exitStatus:self.append_output(completion_message, 'red') if completion_message else None)
        process.start()

    def process_kill_processes(self):
        self.clear_output()
        current_process = psutil.Process()
        for proc in psutil.process_iter():
            if (proc.name() in ['python.exe', 'ffmpeg.exe']) and (proc.pid != current_process.pid):
                proc.kill()
        self.append_output("已杀掉所有Python和ffmpeg进程，除了当前进程。", 'red')

    def process_update_git(self):
        self.clear_output()
        self.run_command("git checkout . && git pull", "Git仓库更新完成。")

    def process_install_pip(self):
        self.clear_output()
        self.run_command(".\\dv3admin\\Scripts\\pip.exe install -r project\\req_new.txt", "Pip安装完成。")

    def process_database_migration(self):
        self.clear_output()
        self.run_command(".\\dv3admin\\python.exe manage.py makemigrations && .\\dv3admin\\python.exe manage.py migrate", "数据库迁移完成。")

    def process_start_django(self):
        self.clear_output()
        process = QtCore.QProcess(self)
        process.setProgram("cmd.exe")
        process.setArguments(["/C", ".\\dv3admin\\python.exe manage.py runserver 0.0.0.0:9000"])
        process.readyReadStandardOutput.connect(self.handle_django_output)
        process.readyReadStandardError.connect(lambda:self.append_output(str(process.readAllStandardError(), 'utf-8')))
        process.start()

    def handle_django_output(self):
        if not self.sender():
            return
        output_bytes = self.sender().readAllStandardOutput()
        output_str = bytes(output_bytes).decode('utf-8')
        self.append_output(output_str)
        if "development server at" in output_str:
            self.start_client_button.setEnabled(True)  # Enable the button when Django starts successfully

    def process_start_client(self):
        self.clear_output()
        process = QtCore.QProcess(self)
        process.setProgram("cmd.exe")
        process.setArguments(["/C", ".\\project\\vite-project.exe"])
        process.start()

        # 延时一定时间后假设客户端已经启动
        QtCore.QTimer.singleShot(1000, lambda:self.append_output("客户端正在启动中，请稍候...", 'green'))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qdarktheme.setup_theme(theme="light")
    launcher = Launcher()
    launcher.show()
    sys.exit(app.exec())
