# Flaskクラスをインポートする
from flask import Flask, render_template, url_for

# Flaskクラスをインスタンス化する
app = Flask(__name__)


# URLと実行する関数をマッピングする
@app.route("/")
def index():
    return "Hello, Flaskbook!!!"


@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!!"


# show_name エンドポイント
@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)


with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/kkk?page=ichiro
    print(url_for("show_name", name="kkk", page="2"))
