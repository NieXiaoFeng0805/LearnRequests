# 结构目录

- api：代码存放地
- backup：备份、还原、初始化
- data：测试数据(数据驱动测试所需的数据文件)
- lib：第三方工具(生成测试报告文件)
- logs：日志
- reports：报告(存放测试报告)
- scripts：脚本文件(执行测试用例)
- config.py：配置文件(存放公共配置项)
- execute.py :生成测试报告
- utils.py : 工具文件,存放工具类、方法

# 接口测试(使用Unittest时,要运行整个类才能获取parameterized中的用例[会少一个self参数],不支持运行单个用例; pytest可以)

## 登录功能（数据驱动）

## 课程管理功能（业务场景测试）

注：需要获取登录态才能进行测试（获取cookie、token）

### 查询所有课程

### 新增课程

### 修改课程

### 更新课程状态