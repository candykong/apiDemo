from util.handle_yaml import Handle_yaml
from util.handle_mysql import handle_mysql

if __name__ == '__main__':
    # sql = Handle_yaml("./db/paopiStatus.yaml").read_yaml().get("sql")
    # result=handle_mysql.dbSelect(sql)
    # print(len(result))

    sql = Handle_yaml("./test.yaml").write_yaml('{"pageNum":1,"pageSize":10,"strategyStatus":null,"isRel":null,"strategyName":null,"strategyCode":null,"strategyType":"strategy_1"}')
