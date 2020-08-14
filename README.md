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
{"file":[{"字段名":"文件地址"}],"content":{"uid":"${uid}","token":"1","channelCode":"BOE","siteCode":"CN"}}
content 为附带参数，没有就去掉content字段
${xxx}引用变量值,${uid}引用变量名为uid的值

## update constant
update constant 添加更新公参，变量
{"common":{"uid":"data.uid","token":"data.token"},
"constants":{"uid":"data.uid","cid":"data.eboAppUserChildren[0].cid"}}
#### common 添加或更新公参
#### 例
请求响应为:
{"code":"0x00000000","data":{"token":"123456","cid":"U201801200052205"},"message":"【调用成功】","remark":"用户登录接口","status":"1"}

"common":{"uid":"data.cid","token":"data.token"}就是将公参中uid的值替换为U201801200052205、token的值替换为123456,如果公参中没有uid则在公参中添加一个uid字段值为U201801200052205

###constants 变量
#### 例
请求响应为:
{"code":"0x00000000","data":{"token":"123456","uid":"U201801200052205","eboAppUserChildren":[{"cid":"ut202007132233","name":"张三"}]},"message":"【调用成功】","remark":"用户登录接口","status":"1"}
"constants":{"uid":"data.uid","cid":"data.eboAppUserChildren[0].cid"}则是将U201801200052205存入变量uid中，ut202007132233存入变量cid中，如果不存在则新建

  [1]: http://kindergarten.ellabook.cn/f545b67327944b8a853491a5955d6e3e.png
  [2]: http://kindergarten.ellabook.cn/da5adf9789f44c9680946690b1f3362e.png
