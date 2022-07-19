一、框架组成部分 
1.base基础类，用来封装requests
2、util操作类，如处理yaml文件、ini文件、数据库、日志操作等等
3.config下配置环境和数据库等配置信息 
4.api完成编写接口请求信息
5.data存放测试数据，传参和期望值
6.testcase完成用例
7、report存放测试报告
8、log存放日志
9.lib存放第三方库
10、db用来放sql语句
10、run.py用来执行用例


二、依赖库 PyYaml requests pymysql pytest allure-pytest pytest_assume locust websocket jsonpath threadpool

三、使用allure运行 
1.运行生成结果pytest testCase/ --alluredir=./tmp/allure_results 
2.生成报告：allure generate ./tmp/allure_results/ -o ./report/ --clean 
3.打开报告：allure open -h 127.0.0.1 -p 8883 ./report/