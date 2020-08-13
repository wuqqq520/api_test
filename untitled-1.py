#coding=utf-8
import time

print('/Test_report/'+time.strftime("%Y%m%d%H%M%S")+'.html')
report_file='./Test_report/'+time.strftime("%Y%m%d%H%M%S")+'.html'
f=open(report_file,"w",encoding='utf-8')
f.close()
