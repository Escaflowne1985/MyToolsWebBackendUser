# env manage.py/py
# -*- coding: UTF-8 -*-
'''
@Project ：manage.py 
@File    ：logs_handler.py
@IDE     ：PyCharm 
@Author  ：Mr数据杨
@Date    ：2024-09-27 8:01 
'''

import logging
import asyncio
from channels.layers import get_channel_layer


class WebSocketLogHandler(logging.Handler):
    """
    自定义日志处理器，通过 WebSocket 发送日志信息到前端。
    """

    async def async_emit(self, record):
        try:
            # 格式化日志记录
            log_entry = self.format(record)
            # 获取通道层
            channel_layer = get_channel_layer()

            # 调试输出，确保日志准备发送
            # print(f"[WebSocketLogHandler] Preparing to send log entry: {log_entry}")

            # 发送日志信息到 WebSocket 群组
            await channel_layer.group_send(
                "log_group",  # 确保群组名称正确
                {
                    'type':'log.message',
                    'message':log_entry,
                }
            )
            # print(f"[WebSocketLogHandler] Log entry sent: {log_entry}")

        except Exception as e:
            print(f"Error in WebSocketLogHandler: {str(e)}")

    def emit(self, record):
        # 检查是否有正在运行的事件循环
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # 如果事件循环已经在运行，则通过 create_task 调度异步任务
                loop.create_task(self.async_emit(record))
            else:
                # 如果没有正在运行的事件循环，创建一个新的事件循环并运行任务
                loop.run_until_complete(self.async_emit(record))
        except RuntimeError:
            # 如果 get_event_loop 失败，则创建一个新的事件循环
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)
            new_loop.run_until_complete(self.async_emit(record))
