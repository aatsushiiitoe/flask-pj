# -*- coding: utf-8 -*-
# 現在日付と時刻だけを出すプログラム

import datetime

class output_text :
    # 初期処理
    def __init__(self) :
        print("start")

    # 日付・時刻を出力する
    def output_date(self, mode = 0) :
        if mode == 1 :
            # 
            print(datetime.date.today())
        elif mode == 2 :
            print(datetime.datetime.today())
        else :
            print("none")