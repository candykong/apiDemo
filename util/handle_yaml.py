import yaml
import json


class Handle_yaml:
    def __init__(self,fileName):
        self.fileName=fileName

    def read_yaml(self,encoding='utf-8'):
        """读取yaml文件"""
        with open(self.fileName) as f:
            str = yaml.safe_load(f)
            return str


    def write_yaml(self,str,encoding='utf-8'):
        """字符串输入到yaml文件中"""
        data=json.loads(str)
        with open(self.fileName,encoding='utf-8',mode='w') as f:
            yml=yaml.safe_dump(data,stream=f,allow_unicode=True)
        return yml

    def get_uri(self):
        url=self.read_yaml().get("url")
        return url


