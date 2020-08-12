#coding=utf-8
import json
import http_api


########################################################################
class project:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.url=None
        self.common={}
        self.constants={}
        self.Headers={}
        
    def set_head(self,strhead):
        he=json.loads(strhead)
        for key in he:
            self.Headers[key]=he[key]
        
    def set_common(self,key,val):
        self.common[key]=val
        
    def set_constant(self,key,val):
        self.constants[key]=val
        
    def set_url(self,url):
        self.url=url
    def manage_body(self,data):
        for k in self.constants:
            data=data.replace("${"+k+"}",self.constants[k])    
        return data
    
    def process(self,data):
        for k in self.constants:
            data=data.replace("${"+k+"}",self.constants[k])
        body=eval(data)
        for k in self.common:
            if k not in body:
                body[k]=self.common[k]
        self.body=json.dumps(body)
        
    def requ_post(self):
        re=http_api.requ_post(self.url,self.Headers,self.body)
        return re
    
    def requ_get(self):
        re=http_api.requ_get(self.url, self.Headers, self.body)


