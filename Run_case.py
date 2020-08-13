#coding=utf-8
import configure
import xlrd
import machining
import json
import re
import html
import Newreport


class Testing_work():
    def __init__(self):
        self.case_test=machining.machining() 
        
    def runcase(self,case):
        self.case_test.set_url(case[3])
        self.case_test.set_head(case[4])
        self.case_test.process(case[5])
        if case[2]=="POST":
            self.re=self.case_test.requ_post()
            dct=json.loads(self.re[0].text)
            respond=json.dumps(dct,indent=4,ensure_ascii=False)
            print(respond)
        undata=json.loads(case[6])
        self.updata(undata)
        results=self.Assertion(case[7])
        return(self.re[0].status_code,self.re[0].elapsed.total_seconds(),results,self.re[2],self.re[0].url,self.re[1],respond)
        
    def Assertion(self,string):
        data=self.case_test.manage_body(string)
        affirm=eval(data)
        if "status_code" in affirm:
            if affirm["status_code"]==self.re[0].status_code:
                results="Pass"
            else:
                results="Fail"
        elif "text" in affirm:
            text_affirm=affirm["text"]
            if "contain" in text_affirm:
                if text_affirm["contain"] in self.re[0].text:
                    results="Pass"
                else:
                    results="Fail"
            elif "equal" in text_affirm:
                if text_affirm["equal"]==self.re[0].text:
                    results="Pass"
                else:
                    results="Fail"
        elif "SubItem" in affirm:
            r = list(map(self.compare,affirm["SubItem"]))
            if False in r:
                results="Fail"
            else:
                results="Pass"
        else:
            if self.re[0].status_code ==200:
                results="Pass"
            else:
                results="Fail"
        return results
            
    def compare(self,a):
        if a[0]==a[1]:
            return True
        else:
            return False
    
    def updata(self,undata):
        self.rejson=json.loads(self.re[0].text)
        if "common" in undata:
            common=undata["common"]
            for key in common:
                cstr=self.ecstr(common[key])
                self.case_test.set_common(key, cstr)
        if "constants" in undata:
            constants=undata["constants"]
            for key in constants:
                cstr=self.ecstr(constants[key])
                self.case_test.set_constant(key, cstr)     
                
    def ecstr(self,string):
        keylist=re.split("[.\[\]]",string)
        keylist=list(filter(None, keylist))
        rej=self.rejson
        for val in keylist:
            if val.isdigit():
                rej=rej[int(val)]
            else:
                rej=rej[val]
        return rej         
 

if __name__ == '__main__':
    Testing=Testing_work()
    excel=xlrd.open_workbook(configure.case_file)
    table=excel.sheet_by_name(configure.case_sheet)
    nrows =table.nrows 
    result_jscon={"total":0,"Passnum":0,"Failnum":0,"statistics":[0,0,0,0,0],"apilist":[]}
    for x in range(5,nrows):
        case=table.row_values(x)
        Return_result=Testing.runcase(case)
        usetime=str(Return_result[1]*1000)
        result={"case_id":case[0],"theme":case[1],"url":Return_result[4],"headers":json.dumps(Return_result[3]),"body":Return_result[5],"status_code":Return_result[0],"use_time":usetime[:usetime.index(".")+3]+"ms","result":Return_result[2],"response":Return_result[6]}
        result_jscon["apilist"].append(result)
        result_jscon["total"]=result_jscon["total"]+1
        if Return_result[2]=="Pass":
            result_jscon["Passnum"]=result_jscon["Passnum"]+1
            usetime=Return_result[1]*1000 
            if usetime <200:
                result_jscon["statistics"][0]=result_jscon["statistics"][0]+1
            elif usetime>200 and usetime<1000:
                result_jscon["statistics"][1]=result_jscon["statistics"][1]+1
            elif usetime>1000 and usetime<2000:
                result_jscon["statistics"][2]=result_jscon["statistics"][2]+1
            elif usetime>2000:
                result_jscon["statistics"][3]=result_jscon["statistics"][3]+1           
        else: 
            result_jscon["Failnum"]=result_jscon["Failnum"]+1
            result_jscon["statistics"][4]=result_jscon["statistics"][4]+1
        print("=================================================================")
    Newreport.write_html(result_jscon)    

 






    
            
            
    
