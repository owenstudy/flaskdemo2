#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 4/25/2021 11:47 AM
# @Author  : Owen_study
# @Email   : owen_study@126.com
# @File    : app.py
# @Software: PyCharm
# ===============================================
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return """
  <h1>Python Flask in Docker!</h1>
  <p>A sample web-app for running Flask inside Docker.</p>
  """
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    pass
