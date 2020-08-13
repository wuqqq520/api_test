# -*- coding: UTF-8 -*-
import sendemail
import time

sample='''<tr style="background-color: {{tr_color}};color:#eeeeee;">
<td style="text-align:center;" onclick="detailed(this)"><div style="border:1px solid #000;height:11px;width:11px;line-height:10px;display:inline-block;text-align: center;margin:0 10px;">+</div></td>
<td>{{case_id}}</td>
<td>{{theme}}</td>
<td style="text-align:center;">{{time}}</td>
<td style="text-align:center;"><div class="result" style="background-color:{{color}};color: #ffffff">{{result}}</div></td>
</tr>
<tr style="display: none;">
<td colspan="5" class="tr2">
<div style="width:98%;border: 1px solid #777777;margin:5px;margin-left:5px;"><b style="margin:0 10px;">URL:</b><span>{{url}}</span><br></div>
<div style="width:98%;border: 1px solid #777777;margin-bottom:5px;margin-left:5px;"><b style="margin:0 10px;">headers:</b><span style="width:60%;word-break: break-all;word-wrap: break-word;">{{headers}}</span></div>
<div  style="width:98%;border: 1px solid #777777;margin-bottom:5px;margin-left:5px;">
<b style="margin: 10px;">BODY:</b>
<p style="width:98%;word-break: break-all;word-wrap: break-word;;margin:0 15px;">{{body}}</p>
</div>
<div style="width:98%;border: 1px solid #777777;margin:5px;"><b style="margin: 10px;">response:</b>
<p style="width:98%;word-break: break-all;word-wrap: break-word;margin:0 15px;">{{response}}</p>
</div>
</td>
</tr>'''

content='''<tr style="background-color: {{tr_color}};color:#eeeeee;">
<td>{{case_id}}</td>
<td>{{theme}}</td>
<td style="text-align:center;">{{time}}</td>
<td style="text-align:center;"><div class="result" style="background-color:{{color}};color: #ffffff">{{result}}</div></td>
</tr>'''

#----------------------------------------------------------------------




def char(s):
   m=max(s)
   if m>210:
      if (m/6)%10 !=0:
         x=m/6-(m/6)%10+10
      else:
         x=m/6
   else:
      if (m/6)%5 !=0:
         x=m/6-(m/6)%5+5
      else:
         x=m/6   
   proportion=x/35  
   r=list(map(lambda x: x / proportion, s))
   
   data={
   "y6":int(6*x),
   "y5":int(5*x),
   "y4":int(4*x),
   "y3":int(3*x),
   "y2":int(2*x),
   "y1":int(x),
   "column1_h":r[0],
   "column1_y":210-r[0]-0.5,
   "column2_h":r[1],
   "column2_y":210-r[1]-0.5,
   "column3_h":r[2],
   "column3_y":210-r[2]-0.5,
   "column4_h":r[3],
   "column4_y":210-r[3]-0.5,
   "column5_h":r[4],
   "column5_y":210-r[4]-0.5
   }   
   return data



def write_html(result_jscon):
   fileoperation = open('./Template/test_rebo.html', 'r',encoding='utf-8')
   operation = open('./Template/mail_rebo.html', 'r',encoding='utf-8')
   html_report=fileoperation.read()
   mail_report=operation.read()
   fileoperation.close()
   operation.close()
   chardata=char(result_jscon["statistics"])
   for rt in chardata:
      html_report=html_report.replace("{{"+rt+"}}",str(chardata[rt])) 
   report_file='./Test_report/'+time.strftime("%Y%m%d%H%M%S")+'.html'
   f=open(report_file,"w",encoding='utf-8')
   
   apilist=result_jscon["apilist"]
   report_content=""
   mail_content=""
   a=0
   for api in apilist:
      report_mould=sample.replace('{{url}}',api["url"])
      if a%2==1:
         report_mould=report_mould.replace('{{tr_color}}',"#303030")
         mail_mould=content.replace('{{tr_color}}',"#303030")
      else:
         report_mould=report_mould.replace('{{tr_color}}',"#2b2a2a")
         mail_mould=content.replace('{{tr_color}}',"#2b2a2a")
      report_mould=report_mould.replace('{{case_id}}',api["case_id"])
      
      mail_mould=mail_mould.replace('{{case_id}}',api["case_id"])
      mail_mould=mail_mould.replace('{{theme}}',api["theme"])
      mail_mould=mail_mould.replace('{{time}}',api["use_time"])
      
      report_mould=report_mould.replace('{{theme}}',api["theme"])
      report_mould=report_mould.replace('{{headers}}',api["headers"])
      report_mould=report_mould.replace('{{body}}',api["body"])
      response=api['response'].replace('\n','<br>')
      response=response.replace(' ','&nbsp;')
      report_mould=report_mould.replace('{{response}}',response)
      report_mould=report_mould.replace('{{time}}',api["use_time"])
      report_mould=report_mould.replace('{{result}}',api["result"])
      mail_mould=mail_mould.replace('{{result}}',api["result"])
      if api["result"]=="Pass":
         report_mould=report_mould.replace('{{color}}',"#008000")
         mail_mould=mail_mould.replace('{{color}}',"#008000")
      else:
         report_mould=report_mould.replace('{{color}}',"red")
         mail_mould=mail_mould.replace('{{color}}',"red")
      a=a+1
      report_content=report_content+report_mould
      mail_content=mail_content+mail_mould
   html_report=html_report.replace("<!-main body->",report_content) 
   mail_report=mail_report.replace("<!-main body->",mail_content) 
   sendemail.sendmail(mail_report)
   f.write(html_report)
   f.close()   
   
   