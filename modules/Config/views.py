from django.http import StreamingHttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from modules.Script.f_config import STOP_FLAG_KEY
import asyncio
import json


@csrf_exempt
def stop_task(request):
    cache.set(STOP_FLAG_KEY, True)  # 设置停止标志
    return JsonResponse({"status":"stopping"})
