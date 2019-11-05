# -*- coding: utf-8 -*-
import os
from flask import Flask, request, g, redirect, url_for, render_template, flash
import sqlite3
import models

app = Flask(__name__)
app.config.from_object(__name__)
 
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'db.sqlite3'),
    SECRET_KEY='foo-baa',
))
 
def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con
 
 
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
 
 
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
 
@app.route('/')
def index():
    con = get_db()
    results = models.select_all(con)
    return render_template('index.html', results=results)
 
@app.route('/create')
def create():
    return render_template('edit.html')
 
 
@app.route('/analysis', methods=['POST'])
def analysis():
 
    title = request.form['title']
    desc = request.form['desc']
    data = request.form['data']
    img = models.create_scatter(data)
 
    con = get_db()
 
    pk = models.insert(con, title,desc, data, img)
    flash('登録処理が完了しました。')    
    return redirect(url_for('view', pk=pk)) 
 
@app.route('/delete/<pk>', methods=['POST'])
def delete(pk):
    con = get_db()
    models.delete(con, pk)
    flash('削除処理が完了しました。')    
    return redirect(url_for('index'))

@app.route('/view/<pk>')
def view(pk):
    con = get_db()
    result = models.select(con, pk)
    return render_template('view.html', result=result)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)