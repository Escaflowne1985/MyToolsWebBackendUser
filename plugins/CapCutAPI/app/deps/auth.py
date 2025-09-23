# coding:utf-8
'''
@IDE     ：PyCharm
@Project ：capcut-mcp.py
@File    ：auth.py
@Author  ：Mr数据杨
@Date    ：2025/9/10
@Desc    :
'''

from typing import Optional
from fastapi import Header, HTTPException, status
from settings.local import FIXED_BEARER_TOKEN


# FastAPI 对 header 名大小写不敏感；参数名 jwt 对应请求头 JWT
async def require_fixed_token(jwt: Optional[str] = Header(default=None)):
    if not jwt:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="missing_jwt")
    if not FIXED_BEARER_TOKEN:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="server_token_not_configured")
    if jwt.strip() != FIXED_BEARER_TOKEN:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid_token")
