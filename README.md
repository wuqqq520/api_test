# api_test
# 实现流程
![此处输入图片的描述][1]


# 用例
![此处输入图片的描述][2]
每条用例都包含case id,title,metoh,url,Headers,body/params,update constant,Assertion 几个值
## case id,title,metoh,url
这几个参数就不说了
## Headers
Headers里必须包含Content-Type，它将决定请求正文的类型
## body/params
为了使用例更加直观，让基础差的人可以进行读写，x-www-form-urlencoded，json，multipart/form-data都采用JSON格式进行编写
### 例
#### x-www-form-urlencoded
   method%3della.readeruser.getUserAttribution%26content%3d%7b%22mobile%22%3a%2213550000001%22%7d%26channelCode%3dBOE%26siteCode%3dCN
   可以写成:
   
   {
    "method":"ella.readeruser.getUserAttribution",
    "content":{
        "mobile":"13550000001"
    },
    "channelCode":"BOE",
    "siteCode":"CN"
}
#### multipart/form-data 上传文件
{"file":[{"字段名":"文件地址"}],"content":{"uid":"U201810111117401323649","token":"1","channelCode":"BOE","siteCode":"CN"}}
content 为附带参数，没有就去掉content字段


  [1]: http://kindergarten.ellabook.cn/f545b67327944b8a853491a5955d6e3e.png
  [2]: http://kindergarten.ellabook.cn/da5adf9789f44c9680946690b1f3362e.png
