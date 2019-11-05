# -*- coding: utf-8 -*-

"""
ビジネスロジックモジュール
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from matplotlib import pyplot as plt
import time
import io
 
 
def create_scatter(data):
    
 
    # 表示用URL
    url = "result/" + data
 
 
    return url

def insert(con, title, desc, data, img):
    """ INSERT処理 """
    cur = con.cursor()
    cur.execute('insert into results (title,desc, data, img) values (?,?, ?, ?)', [title,desc, data, img])
 
    pk = cur.lastrowid
    con.commit()
 
    return pk

def select(con, pk):
    """ 指定したキーのデータをSELECTする """
    cur = con.execute('select id, title, desc, data, img, created from results where id=?', (pk,))
    return cur.fetchone()

def select_all(con):
    """ SELECTする """
    cur = con.execute('select id, title,desc, data, img, created from results order by id desc')
    return cur.fetchall()

def delete(con, pk):
    """ 指定したキーのデータをDELETEする """
    cur = con.cursor()
    cur.execute('delete from results where id=?', (pk,))
    con.commit()