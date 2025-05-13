# -*- coding: utf-8 -*-

"""
@Remark: 自定义的JsonResonpse文件
"""

from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage
from collections.abc import Iterable
from django.db.models.query import QuerySet


class SuccessResponse(Response):
    """
    标准响应成功的返回, SuccessResponse(data)或者SuccessResponse(data=data)
    (1)默认code返回2000, 不支持指定其他返回码
    """

    def __init__(self, data=None, msg='success', status=None, template_name=None, headers=None, exception=False,
                 content_type=None, page=1, limit=1, total=1):
        std_data = {
            "code": 2000,
            "page": page,
            "limit": limit,
            "total": total,
            "data": data,
            "msg": msg
        }
        super().__init__(std_data, status, template_name, headers, exception, content_type)


class DetailResponse(Response):
    """
    不包含分页信息的接口返回,主要用于单条数据查询
    (1)默认code返回2000, 不支持指定其他返回码
    """

    def __init__(self, data=None, msg='success', status=None, template_name=None, headers=None, exception=False,
                 content_type=None, ):
        std_data = {
            "code": 2000,
            "data": data,
            "msg": msg
        }
        super().__init__(std_data, status, template_name, headers, exception, content_type)


class ErrorResponse(Response):
    """
    标准响应错误的返回,ErrorResponse(msg='xxx')
    (1)默认错误码返回400, 也可以指定其他返回码:ErrorResponse(code=xxx)
    """

    def __init__(self, data=None, msg='error', code=400, status=None, template_name=None, headers=None,
                 exception=False, content_type=None):
        std_data = {
            "code": code,
            "data": data,
            "msg": msg
        }
        super().__init__(std_data, status, template_name, headers, exception, content_type)


class SuccessResponsePage(Response):
    """
    自动分页响应类。
    只要把 QuerySet 或 list 传给 data，并把 request 也传进来，就能完成：
    • 从 request.query_params 读 page、limit
    • 用 Django Paginator 做分页
    • 如果 data 是 QuerySet，分页后再调用 .values() 转 dict 列表
    • 自动填充 code/page/limit/total/data 四个字段
    """

    def __init__(self, data=None, msg='success', request=None,
                 status=None, template_name=None, headers=None,
                 exception=False, content_type=None):

        # 默认分页信息
        page = 1
        limit = 10
        total = 0
        result_data = data

        if request is not None and isinstance(data, Iterable) and not isinstance(data, (str, bytes, dict)):
            # 优先从 query_params 读取，若未提供再从 body 中读取
            raw_page = request.query_params.get("page") or request.data.get("page") or 1
            raw_limit = request.query_params.get("limit") or request.data.get("limit") or 10
            try:
                page = int(raw_page)
            except (TypeError, ValueError):
                page = 1
            try:
                limit = int(raw_limit)
            except (TypeError, ValueError):
                limit = 10

            paginator = Paginator(data, limit)
            try:
                page_obj = paginator.page(page)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)

            if isinstance(data, QuerySet):
                result_data = list(page_obj.object_list.values())
            else:
                result_data = list(page_obj.object_list)

            total = paginator.count
            page = page_obj.number
            limit = page_obj.paginator.per_page

        payload = {
            "code": 2000,
            "msg": msg,
            "page": page,
            "limit": limit,
            "total": total,
            "data": result_data
        }

        super().__init__(payload, status, template_name, headers, exception, content_type)
