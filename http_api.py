#coding=utf-8
import requests
import json
from urllib import parse
from requests_toolbelt.multipart.encoder import MultipartEncoder 
import filetype
import time
import re



def body_form(data):
    Json=json.loads(data)  #json字符串→字典
    urlendata = parse.urlencode(Json) #将字典进行url编码
    return urlendata

def body_json(data):
    tp=type(data)
    if tp ==dict:
        return json.dumps(data)
    elif tp==str:
        return data

def body_multipart_from(data):
    tp=type(data)
    if tp==str:
        data=json.loads(data)   
    file=data['file'] 
    del data['file']
    for k in data:
        if type(data[k])==dict:
            data[k]=json.dumps(data[k])   
    for fl in file:
        for f in fl:
            of=mefile(fl[f]) 
            data[f]=(of[0],open(fl[f],"rb"),of[1])
    multipart_encoder = MultipartEncoder(fields=data)
    return multipart_encoder

def requ_post(url,head,data):
    headtyep=head['Content-Type']
    if "application/x-www-form-urlencoded" in headtyep:
        body=body_form(data)
    elif "application/json" in headtyep:
        body=body_json(data)
    elif "multipart/form-data" in headtyep:
        body=body_multipart_from(data)
        head['Content-Type']=body.content_type
    re=requests.post(url, data=body, headers=head,verify=False)
    if "multipart/form-data" in headtyep:
        body=str(body.fields)
        print(body)
    else:
        print(body)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return (re,body,head)

def mefile(filename):
    kind=filetype.guess(filename).mime
    name=re.split("[/\\\]",filename)[-1]
    return (name,kind)

def requ_get(url,head,data):
    body=json.loads(data)
    re=requests.get(url,headers=head,params=body)
    return re

#requ(url2, head2, content)


