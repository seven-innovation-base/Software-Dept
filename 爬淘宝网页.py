import requests
import re
from urllib.parse import quote
def getHTMLText(url):
    useragent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3702.0 Safari/537.36'
    cookie = 't=9e3b6e41c2151a6b2dada150351c43b6; cna=tGvhFIwk8QgCAXUdcZlmWV89; UM_distinctid=169d19d704759e-05027b913e9d62-33504275-144000-169d19d7048d00; thw=cn; tracknick=wjj12345892413; tg=0; enc=y10E8m19cHAjTWkfF9BAoYP6p56x8FOMSXdH6zttBU%2BLam26ZhbmPNVrKVeL4mrxysPb4qHWwwaxOM4TPyRxeg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=1343001878166935677; v=0; cookie2=1dfe26ebf1defa5d5d05c5674fe220f1; _tb_token_=feb337eeee43e; unb=3171816497; sg=373; _l_g_=Ug%3D%3D; skt=d8098ea4a0b23547; cookie1=UUplZ6%2FieO9JPUoexmcqDCJuIRA4p0rsq7DusLCtGzU%3D; csg=2761d1ab; uc3=vt3=F8dBy3ke1m5PBcscpRc%3D&id2=UNGR740Fe7z50g%3D%3D&nk2=FPMSl9RMQxR0yFxHFG4%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; existShop=MTU2MDQyOTcxNA%3D%3D; lgc=wjj12345892413; _cc_=URm48syIZQ%3D%3D; dnk=wjj12345892413; _nk_=wjj12345892413; cookie17=UNGR740Fe7z50g%3D%3D; mt=ci=96_1; l=bBLrtCBuvwJBMeTiBOfgNZMsA5_O2Qv88sPPhfr2pICP91C9XfKlWZh4ZY8pC3GVa6C6R38wmmB3BXTuoyUCg; uc1=cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=Vq8l%2BKCLjA%2Bl&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTaGOxZJnadYQ%3D%3D&tag=8&lng=zh_CN; isg=BC0t_wgtDI4e8-kZ0U7vfVhcKcmtn_pDbKfKTG8yakQz5k2YN9pxLHsw1LoA5nkU'
    headers = {'user-agent':useragent,'cookie':cookie}
    try:
        r = requests.get(url,headers = headers,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price , title])
    except:
        print("")
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods=input("请输入要搜索的东西名称")

    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + quote(goods)
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            print("ok")
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)

main()