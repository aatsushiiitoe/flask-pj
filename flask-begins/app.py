# app.py
from flask import Flask, render_template, request, abort
from flaski.models import WikiContent
from flaski.database import db_session
from datetime import datetime
import form

app = Flask(__name__)

@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def index():

    s = "abc"
    lis = ["a1", "a2", "a3"]
    dic = {"name":"John", "age":24}
    bl = True
    contents = WikiContent.query.all()
    print(form.output_text().output_date(1)) # 外部ファイル呼び出し
    print ("debug:indexの処理")
    return render_template('index.html', s=s, lis=lis, dic=dic, bl=bl, contents=contents)


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        res = request.args.get('get_value')
    elif request.method == 'POST':
        res = request.form['post_value']

    return res

#/<title>を指定することで、index.htmlのtitle=content.titleを指定している。methods=["GET"]で、GETリクエストを指定。
@app.route("/<title>", methods=["GET"])
def show_content(title):
    """
    :param title:modelに対するクエリ文字列
    :return:
    """
    # wikicontentテーブルから、titleでフィルタ(where指定して取得) firstは1行だけ取得するの意味。
    # all()だと、結果を複数リスト形式で取得する。
    content = WikiContent.query.filter_by(title=title).first()
    if content is None:
        abort(404)
    # show_content.htmlを表示。引数にcontentを渡す。
    return render_template("show_content.html", content=content)





if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)