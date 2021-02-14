import os
import click
from app import create_app, db
from app.models import User, Role, Follow, Comment, Permission, Post
from flask_migrate import Migrate, MigrateCommand

'''
在新版的flask中，不再使用manage执行服务器，shell等，而是改用flask命令。flask命令基于Click库实现
使用flask名字需要指定环境变量，set FLASK_APP=主模块名，FLASK_DEBUG=1可以开启调试。
注意flask命令只可以用于开发服务器，而不能用于生产服务器，执行后IDE并没有运行，而是自动调用flask的开发服务器
-----------------------------------------------------------------------------------------------------
flask run
运行开发服务器
-----------------------------------------------------------------------------------------------------
flask db
执行数据库迁移相关操作。flask db指令不能直接使用，需要获取Migrate实例。
-----------------------------------------------------------------------------------------------------
flask shell
开启一个交互式的python shell，用来访问或处理应用数据。该指令默认激活应用上下文，并导入应用实例。只有应用实例app是默认导入的，
如果需要导入其他对象，使用shell_context_processor装饰函数，返回一个字典对象，键值对表示额外导入的对象。
-----------------------------------------------------------------------------------------------------
自定义命令
flask命令基于Click库实现。
下列代码演示添加带有name参数的print-user命令：

import click
from flask import Flask
 
app = Flask(__name__)
 
@app.cli.command()
@click.argument("name")
def print_user(name):
    print("this is", name)
运行方式：flask print-user root。注意这里的指令是print-user，使用print_user会提示没有这个指令，
除非显示地在app.cli.command()中传入"print_user"。
-----------------------------------------------------------------------------------------------------
应用上下文
使用Flask应用的.cli.command()装饰器添加的命令在执行时自动推入应用上下文。
如果使用Click的command()装饰器添加命令，执行时不会自动推入应用上下文，要想达到同样的效果，增加with_appcontext装饰器：

import click
from flask import Flask, current_app
from flask.cli import with_appcontext
 
app = Flask(__name__)
 
@click.command()
@with_appcontext
def do_work():
    print("do work")
    print(current_app)
 
app.cli.add_command(do_work)
如果命令不需要在应用上下文中执行，可以显示地禁用：

@app.cli.command(with_appcontext=False)
def do_work():
    pass
-----------------------------------------------------------------------------------------------------
'''
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Follow=Follow,
                Post=Post, Comment=Comment, Permission=Permission)  # app=app 已经默认导入


@app.cli.command()  # 使用该装饰器的函数在执行时自动推入上下文
def test():
    """Run the unit tests."""
    import unittest
    tst = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tst)
