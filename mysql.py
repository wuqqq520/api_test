#coding=utf-8
import pymysql
import datetime
import json


class sql:
    def __init__(self):
        self.client = pymysql.connect(
            host='47.98.119.49',
            port=3306,
            user='ellabook',
            password='Ellabook@13579',
            db='ellabook_boe',
            charset='utf8',
            # 设置自动提交命令，如不设置则无法提交命令进行增，改，删操作
            #autocommit=True
        )

    def execute(self,sql):
        # pymysql.cursors.DictCursor 将查询出来的结果制作成字典形式返回
        self.cursor_obj = self.client.cursor(pymysql.cursors.DictCursor)           
        #sql = "SELECT * FROM eb_boe_sn WHERE device_status='ACTIVATED' and sn_type='ELLA'"
        self.cursor_obj.execute(sql)
        # 提交后，通过cursor_obj.fetchall()获取查询游标后的全部的结果
        res = self.cursor_obj.fetchall() 
        self.cursor_obj.close()
        return res
    
    def close(self):
        self.client.close()    
        
        






