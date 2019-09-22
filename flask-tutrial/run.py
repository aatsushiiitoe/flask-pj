import os
from flask import Flask, redirect, url_for, render_template
 
app = Flask(__name__)
app.config.from_object(__name__)
 
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'db.sqlite3'),
    SECRET_KEY='foo-baa',
))
 
 ##ルーティング--------------------------------------------------
@app.route('/')
def index():
    """ 一覧画面 """
    return render_template('index.html', results={})
 
 
@app.route('/create')
def create():
    """ 新規作成画面 """
    return render_template('edit.html')
 
 
@app.route('/analysis', methods=['POST'])
def analysis():
    """ 分析実行処理 """
    return redirect(url_for('view', pk=0))
 
 
@app.route('/delete/<pk>')
def delete(pk):
    """ 結果削除処理 """
    return redirect(url_for('index'))
 
 
@app.route('/view/<pk>')
def view(pk):
    """ 結果参照処理 """
    return render_template('view.html', result={})
 
 ##サーバー起動
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)