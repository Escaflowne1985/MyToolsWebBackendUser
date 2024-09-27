# -*- coding: utf-8 -*-
from django.urls import path, re_path
from application.websocketConfig import MegCenter, LogWebSocket

websocket_urlpatterns = [
    path(r'ws/logs/', LogWebSocket.as_asgi()),  # 这里的 LogWebSocket 是你用于处理日志的 WebSocket 类
    path('ws/<str:service_uid>/', MegCenter.as_asgi()),  # consumers.DvadminWebSocket 是该路由的消费者
]
