# 导入所需的模块
import json
import time
import datetime
from flask_cors import CORS
from flask import Flask, request, Response

app = Flask(__name__)
# 解决跨域问题
CORS(app, supports_credentials=True)


def get_data():
    # 获取当前时间，并转换为 JSON 格式
    dt_ms = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    return json.dumps({'time':dt_ms}, ensure_ascii=False)


@app.route('/sse')
def stream():
    data_id = request.args.get('data_id')
    print(data_id)
    return Response(eventStream(), mimetype="text/event-stream")


def build_message(message: str, event="message"):
    """
    构建消息
    :param message: 数据消息
    :param event: 事件，默认事件是“message”，可以根据自己的需求定制事件，对应前端的eventSource.addEventListener('message',()=>{}, false)中的message。
    :return:
    """
    head = "event:" + event + "\n" + "data:"
    tail = "\n\n"
    return head + message + tail


def eventStream():
    id = 0
    while True:
        id += 1
        # 睡眠
        time.sleep(1)

        str_out = build_message(get_data())

        print(str_out)
        # 构建迭代器
        yield str_out


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
