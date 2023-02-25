# -*- encoding: utf-8 -*-
# @Author: CarpeDiem
# @Date: 230213
# @Version: 1.0
# @Description: Flask基本使用

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)