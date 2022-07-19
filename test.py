import requests
import yaml
import time
from base.commonApi import CommonApi
from base.httpRequest import HttpRequest
from testCase.testcase_base import Testcase_base
from testCase.test_remindMatterList import Test_remindMatterList
from util.commonTemplate import CommonTemplate
from util.handle_yaml import Handle_yaml


def get_remind():
    test_remindMatterList=Test_remindMatterList()
    test_remindMatterList.test_remindMatterList()

def get_token():
    testCae_base=Testcase_base()
    testCae_base.get_token()


def testget1():
    commonApi = CommonApi()
    data=yaml.safe_load(open("api/remindMatterList.yaml"))
    r=commonApi.send(data)
    print(r.text)

def testget2():
    data = yaml.safe_load(open("api/remindMatterList.yaml"))
    httpRequest=HttpRequest(data)
    r=httpRequest.send()
    print(r.text)

def testget():
    url="http://10.4.190.31:8081/fins-console-sso/user/remindMatterList"
    method="get"
    headers={"content-type": "application/json","token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJib2IiLCJleHAiOjE2NDg1Mzc1NzgsInVzZXJJZCI6ImZhbmd3MSJ9.Mt7rmWBZP43ExD--lSjow0yI3u1NAdhjrnCUJ6yL0O0"}
    json={"channel": "PC"}
    r = requests.get(url=url, headers=headers, params=json)
    print(r.text)

if __name__ == '__main__':
    #get_token()
    #get_remind()
    #get_login()
    # file = "log/"+time.strftime("%Y-%m-%d", time.localtime()) + ".txt"
    # print(file)
    # handle_yaml=Handle_yaml("data/login_data1.yaml")
    # #url=handle_yaml.get_uri()
    # #print(url)
    # description=handle_yaml.get_testCase_description()
    # print(description)

    token1 = {'token': '123456'}
    data2={'channel': 'channel'}
    # #data=yaml.safe_load(open("data/remindMatterList_data.yaml"))
    # #data = CommonTemplate().template("api/remindMatterList.yaml", data)
    # print(data)
    data2.update(token1)
    print(data2)

    data = {'token': '123456'}
    token = {'channel': 'channel'}

    data.update(token)
    print("更新字典 tinydict : ", data)



