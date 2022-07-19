#!/usr/bin/python
# -*- coding：UTF-8 -*-

from util.handle_ini import Handle_ini
from util.handle_yaml import Handle_yaml

import pymysql.cursors


class Handle_mysql():
    def __init__(self,host,port,user,passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd

    def dbConnect(self):
        self.db = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            charset='utf8',)
        return self.db

    def dbSelect(self,sql):
        self.cursor = self.dbConnect().cursor()
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print(data)
        self.db.close()
        return data

#获取mysql的信息
mysqlConf=Handle_ini("./config/config.ini")
mysql_host=mysqlConf.getValue("Mysql-Database","host")
mysql_port=mysqlConf.getValue("Mysql-Database","port")
mysql_user=mysqlConf.getValue("Mysql-Database","user")
mysql_passwd=mysqlConf.getValue("Mysql-Database","passwd")
handle_mysql=Handle_mysql(mysql_host,int(mysql_port),mysql_user,mysql_passwd)













