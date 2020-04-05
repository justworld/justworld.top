# justworld的自媒体
> 欢迎加入QQ群讨论：885675028

## 简介
这是网站[blog.justworld.top](https://blog.justworld.top)的源码, 基于django、vue2.x的前后端分离系统.  
后端使用Python3.6+Django+Mysql+Redis+ElasticSearch等技术, 前端基于[Bobbi的项目](https://github.com/llldddbbb/dbblog)进行修改.

## 项目结构
```shell
justworld.top
├── api   # 后端, API和管理后台
│   ├── apps 应用代码
│   └── core 架构基础代码, 包括数据库、API等
│   │   ├── database      # 自定义的一些Model、字段类, 数据库路由
│   │   ├── server  # 管理后台和API基类、授权、异常处理、分页、日志中间件等
│   │   ├── const.py         # 自定义的枚举类
│   │   ├── log_util.py     # 日志相关类
│   │   ├── monkey_patch.py     # 猴子补丁
│   └── settings 项目配置文件
│   └── sql 数据库变更sql
│   └── static 管理后台资源文件
│   └── utils 公共库
│   └── deploy.sh 部署执行脚本
│   └── dockerfile docker构建文件
│   └── entryponint.sh docker运行入口代码
│   └── manage_dev.py 开发环境
│   └── manage_prod.py 正式环境
│   └── requirements.txt 依赖库
│   └── uwsgi.ini uwsgi配置文件
├── web   # 前端
```
前端的详细架构介绍请看[Bobbi的项目](https://github.com/llldddbbb/dbblog)

## 运行
### 后端
项目后端环境
- Python 3.6
- Mysql
- Redis
- ElasticSearch
- 部署步骤：
    1. 使用virtualenv建立虚拟环境, 安装依赖： pip install -r requirements.txt
    2. 根据sql文件建数据库
    3. 开发环境运行：python3 manage_dev.py runserver
    4. 正式环境可以采用docker+nginx+uwsgi部署, 直接运行命令为：python3 manage_prod.py runserver

### 前端
- Node.js

- 部署步骤：
    1. 安装依赖： npm install
    2. 开发环境： npm run dev
    3. 正式环境打包： npm build


## 最后
感谢支持！欢迎访问我的[博客https://blog.justworld.top](https://blog.justworld.top), 以及公众号<br>![01杂谈.jpg](https://raw.githubusercontent.com/justworld/justworld.top/master/01%E6%9D%82%E8%B0%88.jpg)  <br><br>
生命值得为之奋斗！
