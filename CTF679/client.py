# -*- coding: utf-8 -*-
import http.client
import uuid
import random
import json
import time
import ssl
import websocket


def fuck(flag, ws,ctf_is):
    conn = http.client.HTTPSConnection("security.bilibili.com")
    payload = "{\"flag\":\"" + flag + "\",\"ctf_id\":" + ctf_is + "}"
    headers = {
        'Host': ' security.bilibili.com',
        'Connection': ' keep-alive',
        'Accept': ' application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.111 Safari/537.36',
        'Content-Type': ' application/json;charset=UTF-8',
        'Origin': ' https://security.bilibili.com',
        'Sec-Fetch-Site': ' same-origin',
        'Sec-Fetch-Mode': ' cors',
        'Sec-Fetch-Dest': ' empty',
        'Referer': ' https://security.bilibili.com/sec1024/',
        'Accept-Encoding': ' gzip, deflate, br',
        'Accept-Language': ' zh-CN,zh;q=0.9',
        'Cookie': ""
    }
    conn.request("POST", "/sec1024/api/v1/flag", payload, headers)
    res = conn.getresponse()
    data = res.read()
    if data.decode("utf-8").find("Flag错误，请继续努力") == -1:
        if data.decode("utf-8").find("请勿频繁提交") == -1:
            print(data.decode("utf-8") + " " + payload)
            ws.send(data.decode("utf-8") + " 这是破解成功了？" + payload)
            exit()
        else:
            time.sleep(5)
            print(data.decode("utf-8") + " " + payload)
    else:
        print(data.decode("utf-8") + " " + payload)


def get_flag():
    flag = str(uuid.uuid4()).replace("-", "")
    temp = []
    length = len(flag)
    for n in range(length):
        if n % 8 == 0:
            temp.append(flag[n:n + 8])
    return '-'.join(temp)


def on_message(self, message):  # 第一个参数必须传递
    print(message)


def on_error(self, error):
    print(error)


def on_close(self):
    print("### closed ###")


def on_open(self):
    def run():
        for i in range(3):  # 可以死循环发送
            ws.send("1")

    thread.start_new_thread(run, ())  # 启动线程执行run()函数发送数据


###############################################################
url = 'ws://203.195.240.56:17001'
# 子服务器节点
# url = 'ws://106.225.220.241:17001'
ws = None
while True:  # 一直链接，直到连接上就退出循环
    time.sleep(2)
    try:
        ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
        ws.connect(url)
        print(ws)
        break
    except Exception as e:
        print('连接异常：', e)
        continue
while True:  # 连接上，退出第一个循环之后，此循环用于一直获取数据
    ws.send("1")
    print(fuck(ws.recv(), ws, "6"))
    ws.send("1")
    print(fuck(ws.recv(), ws, "7"))
    ws.send("1")
    print(fuck(ws.recv(), ws, "9"))
