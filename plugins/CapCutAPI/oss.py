import oss2
import os
from settings.local import OSS_CONFIG, MP4_OSS_CONFIG
from settings.local import COS_CONFIG, MP4_COS_CONFIG
import os
import oss2
from qcloud_cos import CosConfig, CosS3Client

# ========== 控制开关 ==========
CLOUD_VENDOR = "cos"  # 可选: "oss" 或 "cos"


def upload_to_oss(path: str) -> str:
    """上传文件到 OSS / COS，并返回公网可访问 URL"""
    if not os.path.isfile(path):
        raise FileNotFoundError(f"文件不存在: {path}")

    file_name = os.path.basename(path)

    # ================== 阿里云 OSS ==================
    if CLOUD_VENDOR == "oss":
        auth = oss2.Auth(OSS_CONFIG["access_key_id"], OSS_CONFIG["access_key_secret"])
        bucket = oss2.Bucket(auth, OSS_CONFIG["endpoint"], OSS_CONFIG["bucket_name"])

        object_name = file_name
        bucket.put_object_from_file(object_name, path)

        # 生成带签名的临时访问 URL（有效期 24h）
        url = bucket.sign_url("GET", object_name, 24 * 60 * 60)

    # ================== 腾讯云 COS ==================
    elif CLOUD_VENDOR == "cos":
        config = CosConfig(
            Region=COS_CONFIG["region"],
            SecretId=COS_CONFIG["secret_id"],
            SecretKey=COS_CONFIG["secret_key"],
            Scheme="https",
        )
        client = CosS3Client(config)

        # 拼接 Key（带 path_prefix）
        path_prefix = COS_CONFIG.get("tencent_path", "").strip("/")
        if path_prefix:
            object_name = f"{path_prefix}/{file_name}"
        else:
            object_name = file_name

        # 推荐用 upload_file，避免 MAZ 桶报错
        client.upload_file(
            Bucket=COS_CONFIG["bucket_name"],  # BucketName-Appid
            LocalFilePath=path,
            Key=object_name,
            PartSize=1,  # 分块大小（MB），默认 1MB
            MAXThread=5,  # 上传线程数
            EnableMD5=False,
        )

        # 拼接 URL
        if COS_CONFIG.get("domain"):
            # 使用自定义加速域名
            base_url = f"https://{COS_CONFIG['domain']}".rstrip("/")
            url = f"{base_url}/{object_name}"
        else:
            # 默认腾讯云 COS 域名
            url = f"https://{COS_CONFIG['bucket_name']}.cos.{COS_CONFIG['region']}.myqcloud.com/{object_name}"

    else:
        raise ValueError(f"不支持的云厂商: {CLOUD_VENDOR}")

    # 清理临时文件
    os.remove(path)

    return url



def upload_mp4_to_oss(path: str) -> str:
    """上传 MP4 文件（OSS 使用 V4 签名，COS 直接走 COS 客户端）"""
    object_name = os.path.basename(path)

    if CLOUD_VENDOR == "oss":
        # OSS V4 签名
        auth = oss2.AuthV4(MP4_OSS_CONFIG['access_key_id'], MP4_OSS_CONFIG['access_key_secret'])
        bucket = oss2.Bucket(
            auth,
            MP4_OSS_CONFIG['endpoint'],
            MP4_OSS_CONFIG['bucket_name'],
            region=MP4_OSS_CONFIG['region'],
            is_cname=True
        )
        bucket.put_object_from_file(object_name, path)
        url = bucket.sign_url('GET', object_name, 24 * 60 * 60, slash_safe=True)

    elif CLOUD_VENDOR == "cos":
        # COS 上传
        config = CosConfig(
            Region=COS_CONFIG['region'],
            SecretId=COS_CONFIG['secret_id'],
            SecretKey=COS_CONFIG['secret_key'],
            Scheme=COS_CONFIG['scheme'],
        )
        client = CosS3Client(config)
        with open(path, 'rb') as fp:
            client.put_object(
                Bucket=COS_CONFIG['bucket_name'],
                Body=fp,
                Key=object_name,
                StorageClass='STANDARD',
                EnableMD5=False
            )
        url = f"{COS_CONFIG['scheme']}://{COS_CONFIG['bucket_name']}.cos.{COS_CONFIG['region']}.myqcloud.com/{object_name}"

    else:
        raise ValueError(f"不支持的云厂商: {CLOUD_VENDOR}")

    os.remove(path)
    return url
