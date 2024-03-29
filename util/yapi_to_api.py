import requests

def get_cat_info(project_id):
    """
    根据产品id获取各个类别接口
    :param project_id:
    :return:
    """

    url = f"http://36.7.144.246:6027/api/project/get?id={project_id}"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Cookie": "_yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEyNDgsImlhdCI6MTY4OTU2NTA5MCwiZXhwIjoxNjkwMTY5ODkwfQ.skDrxfFjGZ1ZdTCSngz3ASWQ6LL14D9KaqRhKBf0ImQ; _yapi_uid=1248"
      }

    response = requests.get(url, headers=headers)
    data = response.json()["data"]
    cat_list = data["cat"]

    result = []
    for cat in cat_list:
        cat_id = cat["_id"]
        cat_name = cat["name"]
        cat_dict = {"id_": cat_id, "name": cat_name}
        result.append(cat_dict)

    return result


import requests

def get_id_list(catid):
    url = f"http://36.7.144.246:6027/api/interface/list_cat?page=1&limit=20&catid={catid}"
    headers = {
        "Accept": "application/json, text/plain, */*",
           "Cookie": "_yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEyNDgsImlhdCI6MTY4OTU2NTA5MCwiZXhwIjoxNjkwMTY5ODkwfQ.skDrxfFjGZ1ZdTCSngz3ASWQ6LL14D9KaqRhKBf0ImQ; _yapi_uid=1248"

    }

    response = requests.get(url, headers=headers)
    data = response.json()["data"]
    id_list = [item["_id"] for item in data["list"]]

    return id_list


catid = 9583
id_list = get_id_list(catid)
print(id_list)

"""
获取所有接口信息流程
1、获取分类
2、获取接口id
3、获取接口详情
"""


# project_id = 1625
# cat_info = get_cat_info(project_id)
# print(cat_info)