import requests

# url = 'http://localhost:6274/'
#
# mp4_path = 'C:/Users/Administrator/Documents/Downloads/jiebujie_00001-audio_dzhfk_1756369007.mp4'

# response = requests.post("http://127.0.0.1:9000/add_video", json={
#     "video_url": mp4_path,
#     "start": 0,
#     "end": 10,
#     "width": 1080,
#     "height": 1920
# })
#
# print(response.json())

# import requests
#
# response = requests.post("http://localhost:9000/add_text", json={
#     "text": "你好，世界！",
#     "start": 0,
#     "end": 3,
#     "font": "雅月体",
#     "font_color": "#FF0000",
#     "font_size": 30.0
# })
#
# print(response.json())


# response = requests.post("http://localhost:9000/save_draft", json={
#     "draft_id": "dfd_cat_1756709166_e5651f0c",
#     "draft_folder": "d:/"
# })
#
# print(response.json())


base_url = 'http://127.0.0.1:9000/'
part = 'create_draft'

data = {
    "height": "1080",
    "width": "1080"
}

headers = {
    "Content-Type": "application/json",
    # 如果你在服务端是检查固定字符串，就直接写死
    "JWT": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU3NTUwMDcyLCJpYXQiOjE3NTc0NjM2NzIsImp0aSI6IjE2OTg4YTFkMGIzNzQ1OGRhNDEwMDg2NWQyMTNmOWFhIiwidXNlcl9pZCI6MX0.iK7HVa8ijJ2XtQ1HQFsxjargmUD9RLXrwfv"
}

url = base_url + part
resp = requests.post(url, headers=headers, json=data)
print(resp.status_code, resp.text)
