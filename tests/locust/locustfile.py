from locust import HttpLocust, TaskSet, task
import json

url = "/api/v1/device-status"

offlinejson = """{
    "msg_type": 4,
    "source": "dns:talaria-1234",
    "dest": "device-status/mac:112233445566/offline",
    "content_type": "json",
    "partner_ids": [
        "comcast"
    ],
    "metadata": {
        "/boot-time": "1542834188",
        "/hw-model": "DPC3941T",
        "fw-name": "DPC3941_3.1p15s1_PROD_sey",
        "/hw-last-reboot-reason": "HW",
        "/hw-manufacturer": "Cisco",
        "/hw-serial-number": "283448812",
        "/last-reconnect-reason": "spanish inquisition",
        "/protocol": "PARODUS-2.0-1.0.0-54-g0910dfa",
        "/trust": "123"
    },
    "payload": "ew0KICAgICAgICAiaWQiOiAibWFjOjQ4ZjdjMGQ3OTAyNCIsDQogICAgICAgICJ0cyI6ICIyMDE4LTExLTIxVDIxOjE5OjAyLjYxNDE5MTczNVoiLA0KICAgICAgICAiYnl0ZXMtc2VudCI6IDAsDQogICAgICAgICJtZXNzYWdlcy1zZW50IjogMSwNCiAgICAgICAgImJ5dGVzLXJlY2VpdmVkIjogMCwNCiAgICAgICAgIm1lc3NhZ2VzLXJlY2VpdmVkIjogMCwNCiAgICAgICAgImNvbm5lY3RlZC1hdCI6ICIyMDE4LTExLTIyVDIxOjE5OjAyLjYxNDE5MTczNVoiLA0KICAgICAgICAidXAtdGltZSI6ICIxNm00Ni42cyIsDQogICAgICAgICJyZWFzb24tZm9yLWNsb3NlIjogInBpbmcgbWlzcyINCiAgICB9"
}""" 

onlinejson = """{
    "msg_type": 4,
    "source": "dns:talaria-1234",
    "dest": "device-status/mac:112233445566/online",
    "content_type": "json",
    "partner_ids": [
        "comcast"
    ],
    "metadata": {
        "/boot-time": "1542834188",
        "/hw-model": "DPC3941T",
        "fw-name": "DPC3941_3.1p15s1_PROD_sey",
        "/hw-last-reboot-reason": "HW",
        "/hw-manufacturer": "Cisco",
        "/hw-serial-number": "283448812",
        "/last-reconnect-reason": "spanish inquisition",
        "/protocol": "PARODUS-2.0-1.0.0-54-g0910dfa",
        "/trust": "123"
    },
    "payload": "ew0KICAgICAgICAiaWQiOiAibWFjOjQ4ZjdjMGQ3OTAyNCIsDQogICAgICAgICJ0cyI6ICIyMDE4LTExLTIzVDIxOjE5OjAyLjYxNDE5MTczNVoiDQogICAgfQ=="
}"""


class UserBehavior(TaskSet):
    def on_start(self):
        # on_start is called when a Locust start before any task is scheduled 
        # print("on start")
        pass 
    def on_stop(self):
        # on_stop is called when the TaskSet is stopping 
        # print("on stop")
        pass
    @task(1)
    def sendonline(self):
        #update to get auth from environment or injected
        auth = "64 encoded supersecret password"
        r = self.client.post(url,headers={"X-Webpa-Signature":auth},data=onlinejson)

    @task(1)
    def sendoffline(self):
        #update to get auth from environment or injected
        auth = "64 encoded supersecret password"
        r = self.client.post(url,headers={"X-Webpa-Signature":auth},data=offlinejson)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 900
    max_wait = 1100
