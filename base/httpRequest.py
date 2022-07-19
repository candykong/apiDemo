import requests
import yaml
import ast

class HttpRequest:

    def __init__(self,data:dict):
        """
        :param data:dict:接口信息
        :param method:请求方法 如get ,post
        :param json: 请求体，会根据请求是否为空，调用不同的方法
        :param form:
        """
        self.data=data
        self.method=self.data["method"]
        self.json=self.data["json"]
        self.form=self.data["form"]
        self.headers=self.data["headers"]
        self.env = yaml.safe_load(open("./config/env.yaml"))
        self.url = self.env["url"][self.env["default"]] + str(self.data["url"])

    def send(self):
        if (self.method == "get" and self.json == None):
            r = requests.get(url=self.url, headers=self.headers)

        elif (self.method == "get" and self.json != None):
            r = requests.get(url=self.url, headers=self.headers, params=self.json)

        elif (self.method == "post" and self.form == "json"):
            r = requests.post(url=self.url, headers=self.headers, json=self.json)

        elif (self.method == "post" and self.form == "json"):
            r = requests.post(url=self.url, headers=self.headers, json=self.json)

        elif (self.method == "post" and self.form == "multipart/form-data"):
            r = requests.post(url=self.url, headers=self.headers, files=ast.literal_eval(self.json))

        else:
            print("'暂时不支持该方法，请继续补充方法'")
            r = None
        return r